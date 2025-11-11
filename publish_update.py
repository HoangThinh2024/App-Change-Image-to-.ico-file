#!/usr/bin/env python3
"""
Publish Update Helper
Tự động tạo version.json và publish update lên GitHub
"""

import os
import sys
import json
import hashlib
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime


def calculate_checksum(file_path):
    """
    Tính SHA256 checksum của file
    
    Args:
        file_path: Path đến file
        
    Returns:
        str: SHA256 hash
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_file_size_formatted(file_path):
    """
    Lấy kích thước file định dạng đẹp
    
    Args:
        file_path: Path đến file
        
    Returns:
        str: Kích thước (vd: "5.2 MB")
    """
    size_bytes = os.path.getsize(file_path)
    
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"


def create_update_package(build_dir, version, app_name):
    """
    Tạo package ZIP cho update
    
    Args:
        build_dir: Thư mục chứa build output
        version: Version string
        app_name: Tên ứng dụng
        
    Returns:
        Path: Path đến file ZIP hoặc None
    """
    build_path = Path(build_dir)
    
    if not build_path.exists():
        print(f"❌ Không tìm thấy thư mục build: {build_dir}")
        return None
    
    # Tạo tên file ZIP
    zip_name = f"{app_name}-v{version}.zip"
    zip_path = build_path.parent / zip_name
    
    print(f"\n📦 Đang tạo update package: {zip_name}")
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(build_path):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(build_path)
                    zipf.write(file_path, arcname)
                    print(f"   + {arcname}")
        
        print(f"\n✓ Đã tạo: {zip_path}")
        print(f"  Kích thước: {get_file_size_formatted(zip_path)}")
        
        return zip_path
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo ZIP: {e}")
        return None


def generate_version_json(version, zip_path, changelog, app_name, github_owner=None, github_repo=None):
    """
    Tạo file version.json
    
    Args:
        version: Version string
        zip_path: Path đến ZIP file
        changelog: Nội dung changelog
        app_name: Tên ứng dụng
        github_owner: GitHub owner (optional)
        github_repo: GitHub repo (optional)
        
    Returns:
        dict: Version info
    """
    # Tính checksum
    checksum = calculate_checksum(zip_path)
    size = get_file_size_formatted(zip_path)
    
    # Tạo download URL
    if github_owner and github_repo:
        download_url = f"https://github.com/{github_owner}/{github_repo}/releases/download/v{version}/{zip_path.name}"
    else:
        download_url = f"https://example.com/releases/{zip_path.name}"
    
    # Tạo version info
    version_info = {
        "version": version,
        "release_date": datetime.now().strftime("%Y-%m-%d"),
        "download_url": download_url,
        "checksum": checksum,
        "size": size,
        "changelog": changelog,
        "minimum_version": "1.0.0",
        "critical": False,
        "notes": {
            "vi": f"Phiên bản {version} của {app_name}",
            "en": f"Version {version} of {app_name}"
        }
    }
    
    return version_info


def save_version_json(version_info, output_path="version.json"):
    """
    Lưu version info ra file JSON
    
    Args:
        version_info: Dict chứa version info
        output_path: Path đến file output
        
    Returns:
        bool: Success status
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(version_info, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Đã tạo {output_path}")
        print(f"\nNội dung:")
        print(json.dumps(version_info, indent=2, ensure_ascii=False))
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi khi lưu JSON: {e}")
        return False


def git_commit_and_push(file_path, commit_message):
    """
    Commit và push file lên git
    
    Args:
        file_path: Path đến file
        commit_message: Commit message
        
    Returns:
        bool: Success status
    """
    try:
        # Add file
        subprocess.run(['git', 'add', file_path], check=True)
        
        # Commit
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        
        # Push
        subprocess.run(['git', 'push'], check=True)
        
        print(f"✓ Đã commit và push {file_path}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"⚠ Lỗi Git: {e}")
        return False


def create_github_release(version, changelog, zip_path, github_owner, github_repo):
    """
    Tạo GitHub Release (yêu cầu GitHub CLI)
    
    Args:
        version: Version string
        changelog: Changelog text
        zip_path: Path đến ZIP file
        github_owner: GitHub owner
        github_repo: GitHub repo
        
    Returns:
        bool: Success status
    """
    try:
        # Check if gh CLI is available
        subprocess.run(['gh', '--version'], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE, 
                      check=True)
        
        # Create release
        tag = f"v{version}"
        title = f"{github_repo} v{version}"
        
        print(f"\n📤 Đang tạo GitHub Release: {tag}")
        
        cmd = [
            'gh', 'release', 'create', tag,
            str(zip_path),
            '--title', title,
            '--notes', changelog,
            '--repo', f"{github_owner}/{github_repo}"
        ]
        
        subprocess.run(cmd, check=True)
        
        print(f"✓ Đã tạo GitHub Release: {tag}")
        print(f"  URL: https://github.com/{github_owner}/{github_repo}/releases/tag/{tag}")
        
        return True
        
    except FileNotFoundError:
        print("\n⚠ GitHub CLI (gh) chưa được cài đặt")
        print("💡 Cài đặt: https://cli.github.com/")
        print("💡 Hoặc tạo Release thủ công trên GitHub")
        return False
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi khi tạo Release: {e}")
        return False


def interactive_publish():
    """
    Interactive publish workflow
    """
    print("\n" + "="*70)
    print("📦 Publish Update Helper")
    print("="*70)
    
    # Auto-detect project info
    try:
        from auto_update_helper import detect_project_info, auto_detect_version
        
        project_dir = Path.cwd()
        info = detect_project_info(project_dir)
        
        if info['has_git']:
            print(f"\n✓ Phát hiện Git repository")
            if info['owner'] and info['repo']:
                print(f"  GitHub: {info['owner']}/{info['repo']}")
        
        auto_version = auto_detect_version(project_dir)
        
    except ImportError:
        info = {'owner': None, 'repo': None, 'app_name': None}
        auto_version = None
    
    # Get inputs
    print("\n📝 Thông tin Release:")
    
    # Version
    if auto_version:
        version = input(f"Version [{auto_version}]: ").strip() or auto_version
    else:
        version = input("Version (vd: 1.0.1): ").strip()
    
    if not version:
        print("❌ Version là bắt buộc!")
        return False
    
    # App name
    if info['app_name']:
        app_name = input(f"App Name [{info['app_name']}]: ").strip() or info['app_name']
    else:
        app_name = input("App Name: ").strip() or "MyApp"
    
    # Build directory
    build_dir = input("Thư mục build [build/exe.win-amd64-3.11]: ").strip()
    if not build_dir:
        # Try to find build directory
        possible_dirs = list(Path("build").glob("exe.*"))
        if possible_dirs:
            build_dir = str(possible_dirs[0])
        else:
            build_dir = "build/exe.win-amd64-3.11"
    
    # Changelog
    print("\n📝 Changelog (nhấn Enter 2 lần để kết thúc):")
    changelog_lines = []
    while True:
        line = input()
        if not line:
            if changelog_lines and not changelog_lines[-1]:
                break
        changelog_lines.append(line)
    
    changelog = "\n".join(changelog_lines).strip()
    if not changelog:
        changelog = f"Release version {version}"
    
    print("\n" + "="*70)
    print("🚀 Bắt đầu publish...")
    print("="*70)
    
    # Step 1: Create ZIP package
    zip_path = create_update_package(build_dir, version, app_name)
    if not zip_path:
        return False
    
    # Step 2: Generate version.json
    version_info = generate_version_json(
        version, 
        zip_path, 
        changelog, 
        app_name,
        info['owner'],
        info['repo']
    )
    
    if not save_version_json(version_info):
        return False
    
    # Step 3: Commit version.json
    print("\n📤 Git operations...")
    commit_msg = f"Update version.json to v{version}"
    git_commit_and_push("version.json", commit_msg)
    
    # Step 4: Create GitHub Release (if possible)
    if info['owner'] and info['repo']:
        create_github_release(
            version,
            changelog,
            zip_path,
            info['owner'],
            info['repo']
        )
    
    print("\n" + "="*70)
    print("✅ HOÀN TẤT!")
    print("="*70)
    print(f"\n📦 Package: {zip_path}")
    print(f"📄 Version JSON: version.json")
    print(f"🔗 Checksum: {version_info['checksum'][:16]}...")
    
    if info['owner'] and info['repo']:
        print(f"\n💡 Các bước tiếp theo:")
        print(f"   1. Kiểm tra GitHub Release đã được tạo")
        print(f"   2. Verify download URL hoạt động")
        print(f"   3. Test auto-update trên ứng dụng")
    else:
        print(f"\n💡 Các bước thủ công:")
        print(f"   1. Upload {zip_path} lên server/GitHub Release")
        print(f"   2. Cập nhật download_url trong version.json")
        print(f"   3. Commit và push version.json")
    
    return True


# CLI
if __name__ == "__main__":
    try:
        success = interactive_publish()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Đã hủy")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        sys.exit(1)
