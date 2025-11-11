#!/usr/bin/env python3
"""
Build script for creating MSI installer
Script để tạo file MSI installer
"""

import os
import sys
import shutil
import subprocess


def clean_build_directories():
    """Clean previous build directories"""
    print("🧹 Cleaning previous build directories...")
    print("🧹 Đang dọn dẹp thư mục build cũ...")
    
    dirs_to_clean = ["build", "dist"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"   ✓ Removed {dir_name}/")
            except Exception as e:
                print(f"   ⚠ Warning: Could not remove {dir_name}/: {e}")


def check_dependencies():
    """Check if required dependencies are installed"""
    print("\n📦 Checking dependencies...")
    print("📦 Đang kiểm tra các thư viện cần thiết...")
    
    try:
        import cx_Freeze
        print(f"   ✓ cx_Freeze version {cx_Freeze.__version__} installed")
    except ImportError:
        print("   ❌ cx_Freeze not installed!")
        print("   Please run: pip install cx_Freeze")
        print("   Vui lòng chạy: pip install cx_Freeze")
        return False
    
    try:
        import PIL
        print(f"   ✓ Pillow installed")
    except ImportError:
        print("   ❌ Pillow not installed!")
        print("   Please run: pip install Pillow")
        print("   Vui lòng chạy: pip install Pillow")
        return False
    
    return True


def build_executable():
    """Build executable using cx_Freeze"""
    print("\n🔨 Building executable...")
    print("🔨 Đang build file executable...")
    
    try:
        subprocess.run(
            [sys.executable, "cx_freeze_setup.py", "build"],
            check=True
        )
        print("   ✓ Executable built successfully!")
        print("   ✓ Build executable thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error building executable: {e}")
        print(f"   ❌ Lỗi khi build executable: {e}")
        return False


def build_msi():
    """Build MSI installer"""
    print("\n📦 Building MSI installer...")
    print("📦 Đang tạo file MSI installer...")
    
    if sys.platform != "win32":
        print("   ⚠ Warning: MSI installer can only be built on Windows!")
        print("   ⚠ Cảnh báo: File MSI chỉ có thể được build trên Windows!")
        print("   You can still use the executable from the 'build' directory.")
        print("   Bạn vẫn có thể sử dụng file executable từ thư mục 'build'.")
        return False
    
    try:
        subprocess.run(
            [sys.executable, "cx_freeze_setup.py", "bdist_msi"],
            check=True
        )
        print("   ✓ MSI installer created successfully!")
        print("   ✓ Tạo file MSI installer thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error creating MSI: {e}")
        print(f"   ❌ Lỗi khi tạo file MSI: {e}")
        return False


def show_results():
    """Show build results"""
    print("\n" + "="*60)
    print("📁 Build Results / Kết quả build:")
    print("="*60)
    
    if os.path.exists("build"):
        print("\n✓ Executable files in 'build' directory:")
        print("✓ Các file executable trong thư mục 'build':")
        for root, dirs, files in os.walk("build"):
            for file in files:
                if file.endswith(".exe"):
                    full_path = os.path.join(root, file)
                    print(f"   • {full_path}")
    
    if os.path.exists("dist"):
        print("\n✓ MSI installer in 'dist' directory:")
        print("✓ File MSI installer trong thư mục 'dist':")
        for file in os.listdir("dist"):
            if file.endswith(".msi"):
                full_path = os.path.join("dist", file)
                print(f"   • {full_path}")
    
    print("\n" + "="*60)


def main():
    """Main build process"""
    # Check if GUI mode is requested
    if len(sys.argv) > 1 and sys.argv[1] in ['--gui', '-g', 'gui']:
        print("🚀 Khởi chạy GUI Mode...")
        print("🚀 Launching GUI Mode...")
        try:
            # Add parent directory to path to import from src/
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
            from src import build_msi_gui
            build_msi_gui.main()
        except ImportError as e:
            print(f"❌ Không thể tìm thấy build_msi_gui.py: {e}")
            print(f"❌ Cannot find build_msi_gui.py: {e}")
            sys.exit(1)
        return
    
    print("="*60)
    print("🚀 Image to ICO Converter - Build Script (CLI Mode)")
    print("🚀 Script build ứng dụng chuyển đổi ảnh sang .ico")
    print("\n💡 Tip: Chạy với '--gui' để mở giao diện đồ họa")
    print("💡 Tip: Run with '--gui' to open graphical interface")
    print("   Example: python build_msi.py --gui")
    print("="*60)
    
    # Clean previous builds
    clean_build_directories()
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Build failed: Missing dependencies")
        print("❌ Build thất bại: Thiếu các thư viện cần thiết")
        sys.exit(1)
    
    # Build executable
    if not build_executable():
        print("\n❌ Build failed: Could not create executable")
        print("❌ Build thất bại: Không thể tạo file executable")
        sys.exit(1)
    
    # Build MSI (only on Windows)
    build_msi()
    
    # Show results
    show_results()
    
    print("\n✅ Build process completed!")
    print("✅ Quá trình build hoàn tất!")


if __name__ == "__main__":
    main()
