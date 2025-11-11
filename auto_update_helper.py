#!/usr/bin/env python3
"""
Auto-Update Helper
Tự động phát hiện GitHub repository và tạo cấu hình update
"""

import os
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse


def get_git_remote_url(project_dir=None):
    """
    Lấy remote URL từ git config
    
    Args:
        project_dir: Thư mục project (mặc định: current dir)
        
    Returns:
        str: Remote URL hoặc None
    """
    if project_dir is None:
        project_dir = Path.cwd()
    else:
        project_dir = Path(project_dir)
    
    git_config = project_dir / ".git" / "config"
    
    if not git_config.exists():
        return None
    
    try:
        with open(git_config, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm remote origin URL
        match = re.search(r'\[remote "origin"\].*?url\s*=\s*(.+?)(?:\n|$)', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        return None
    except Exception as e:
        print(f"⚠ Không thể đọc git config: {e}")
        return None


def parse_github_url(git_url):
    """
    Parse GitHub URL thành owner/repo
    
    Args:
        git_url: Git remote URL
        
    Returns:
        tuple: (owner, repo) hoặc (None, None)
    """
    if not git_url:
        return None, None
    
    # Xử lý SSH URL: git@github.com:owner/repo.git
    ssh_match = re.match(r'git@github\.com:(.+?)/(.+?)(?:\.git)?$', git_url)
    if ssh_match:
        return ssh_match.group(1), ssh_match.group(2)
    
    # Xử lý HTTPS URL: https://github.com/owner/repo.git
    https_match = re.match(r'https?://github\.com/(.+?)/(.+?)(?:\.git)?$', git_url)
    if https_match:
        return https_match.group(1), https_match.group(2)
    
    return None, None


def generate_update_url(owner, repo, branch="main"):
    """
    Tạo update URL từ GitHub repo
    
    Args:
        owner: GitHub username/org
        repo: Repository name
        branch: Branch chứa version.json (default: main)
        
    Returns:
        str: URL đến version.json
    """
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/version.json"


def detect_project_info(project_dir=None):
    """
    Tự động phát hiện thông tin project từ git
    
    Args:
        project_dir: Thư mục project
        
    Returns:
        dict: Thông tin project {owner, repo, update_url, app_name}
    """
    if project_dir is None:
        project_dir = Path.cwd()
    else:
        project_dir = Path(project_dir)
    
    result = {
        'owner': None,
        'repo': None,
        'update_url': None,
        'app_name': None,
        'has_git': False
    }
    
    # Lấy git URL
    git_url = get_git_remote_url(project_dir)
    if git_url:
        result['has_git'] = True
        owner, repo = parse_github_url(git_url)
        
        if owner and repo:
            result['owner'] = owner
            result['repo'] = repo
            result['update_url'] = generate_update_url(owner, repo)
            result['app_name'] = repo.replace('-', ' ').title()
    
    # Fallback: Dùng tên thư mục làm app name
    if not result['app_name']:
        result['app_name'] = project_dir.name.replace('-', ' ').replace('_', ' ').title()
    
    return result


def get_latest_git_tag(project_dir=None):
    """
    Lấy tag mới nhất từ git
    
    Args:
        project_dir: Thư mục project
        
    Returns:
        str: Version tag (vd: "1.0.0") hoặc None
    """
    if project_dir is None:
        project_dir = Path.cwd()
    
    try:
        result = subprocess.run(
            ['git', 'describe', '--tags', '--abbrev=0'],
            cwd=project_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            tag = result.stdout.strip()
            # Remove 'v' prefix if exists
            if tag.startswith('v'):
                tag = tag[1:]
            return tag
    except Exception:
        pass
    
    return None


def read_version_from_file(project_dir=None):
    """
    Đọc version từ các file thông dụng
    
    Args:
        project_dir: Thư mục project
        
    Returns:
        str: Version hoặc None
    """
    if project_dir is None:
        project_dir = Path.cwd()
    else:
        project_dir = Path(project_dir)
    
    # Check pyproject.toml
    pyproject = project_dir / "pyproject.toml"
    if pyproject.exists():
        try:
            with open(pyproject, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('version'):
                        match = re.search(r'version\s*=\s*"(.+?)"', line)
                        if match:
                            return match.group(1)
        except Exception:
            pass
    
    # Check __init__.py
    init_file = project_dir / "__init__.py"
    if init_file.exists():
        try:
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'__version__\s*=\s*["\'](.+?)["\']', content)
                if match:
                    return match.group(1)
        except Exception:
            pass
    
    # Check setup.py
    setup_file = project_dir / "setup.py"
    if setup_file.exists():
        try:
            with open(setup_file, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'version\s*=\s*["\'](.+?)["\']', content)
                if match:
                    return match.group(1)
        except Exception:
            pass
    
    return None


def auto_detect_version(project_dir=None):
    """
    Tự động phát hiện version từ nhiều nguồn
    
    Args:
        project_dir: Thư mục project
        
    Returns:
        str: Version hoặc "1.0.0" (default)
    """
    # Try git tag first
    version = get_latest_git_tag(project_dir)
    if version:
        return version
    
    # Try version files
    version = read_version_from_file(project_dir)
    if version:
        return version
    
    # Default
    return "1.0.0"


def create_update_config(project_dir, output_file="update_config.py"):
    """
    Tạo file update_config.py tự động
    
    Args:
        project_dir: Thư mục project
        output_file: Tên file output
        
    Returns:
        bool: Success status
    """
    project_dir = Path(project_dir)
    info = detect_project_info(project_dir)
    version = auto_detect_version(project_dir)
    
    if not info['update_url']:
        print("⚠ Không phát hiện được GitHub repository")
        print("💡 Đảm bảo project có git remote origin trỏ đến GitHub")
        return False
    
    config_content = f'''"""
Auto-generated Update Configuration
Tự động tạo bởi Auto-Update Helper
"""

# Tự động phát hiện từ git repository
UPDATE_URL = "{info['update_url']}"
APP_NAME = "{info['app_name']}"
APP_VERSION = "{version}"

# GitHub Info
GITHUB_OWNER = "{info['owner']}"
GITHUB_REPO = "{info['repo']}"

# Release URL Template
RELEASE_URL_TEMPLATE = "https://github.com/{info['owner']}/{info['repo']}/releases/download/v{{version}}/{{filename}}"
'''
    
    output_path = project_dir / output_file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(config_content)
        
        print(f"✓ Đã tạo {output_file}")
        print(f"  App Name: {info['app_name']}")
        print(f"  Version: {version}")
        print(f"  Update URL: {info['update_url']}")
        return True
    except Exception as e:
        print(f"❌ Lỗi khi tạo config: {e}")
        return False


def print_setup_instructions(project_dir=None):
    """
    In hướng dẫn setup cho user
    
    Args:
        project_dir: Thư mục project
    """
    info = detect_project_info(project_dir)
    
    print("\n" + "="*70)
    print("📝 HƯỚNG DẪN THIẾT LẬP AUTO-UPDATE")
    print("="*70)
    
    if info['has_git'] and info['update_url']:
        print("\n✅ Phát hiện GitHub repository:")
        print(f"   Owner: {info['owner']}")
        print(f"   Repo: {info['repo']}")
        print(f"   Update URL: {info['update_url']}")
        
        print("\n📋 Các bước tiếp theo:")
        print("\n1️⃣  Tạo file version.json trong repo:")
        print(f"   - Tạo file 'version.json' ở root của repo")
        print(f"   - Commit và push lên GitHub")
        
        print("\n2️⃣  Khi release phiên bản mới:")
        print(f"   - Build ứng dụng với build_msi_gui.py")
        print(f"   - Tạo GitHub Release với tag (vd: v1.0.1)")
        print(f"   - Upload file ZIP/EXE vào Release")
        print(f"   - Cập nhật version.json với thông tin mới")
        
        print("\n3️⃣  Ứng dụng sẽ tự động:")
        print(f"   - Kiểm tra {info['update_url']}")
        print(f"   - Download update từ GitHub Releases")
        print(f"   - Cài đặt mà không cần người dùng làm gì")
        
    else:
        print("\n⚠ KHÔNG phát hiện được GitHub repository")
        print("\nĐể sử dụng Auto-Update tự động, bạn cần:")
        print("1. Init git repository: git init")
        print("2. Add remote GitHub: git remote add origin https://github.com/user/repo.git")
        print("3. Push code lên GitHub")
        print("4. Chạy lại script này")
    
    print("\n" + "="*70)


# CLI Interface
if __name__ == "__main__":
    import sys
    
    print("\n🔄 Auto-Update Helper")
    print("Tự động phát hiện và cấu hình Auto-Update\n")
    
    # Lấy project directory
    if len(sys.argv) > 1:
        project_dir = Path(sys.argv[1])
    else:
        project_dir = Path.cwd()
    
    if not project_dir.exists():
        print(f"❌ Thư mục không tồn tại: {project_dir}")
        sys.exit(1)
    
    print(f"📁 Project: {project_dir.absolute()}\n")
    
    # Phát hiện thông tin
    info = detect_project_info(project_dir)
    version = auto_detect_version(project_dir)
    
    print("🔍 Kết quả phát hiện:")
    print(f"   App Name: {info['app_name']}")
    print(f"   Version: {version}")
    print(f"   Git: {'✓' if info['has_git'] else '✗'}")
    
    if info['has_git']:
        print(f"   GitHub: {info['owner']}/{info['repo']}" if info['owner'] else "   GitHub: ✗")
        print(f"   Update URL: {info['update_url']}" if info['update_url'] else "   Update URL: ✗")
    
    # Tạo config nếu có thể
    if info['update_url']:
        print("\n📝 Tạo update_config.py...")
        create_update_config(project_dir)
    
    # In hướng dẫn
    print_setup_instructions(project_dir)
