# 🔄 Auto-Update Guide - Hướng dẫn Tự động Cập nhật

## 📋 Tổng quan

Hệ thống Auto-Update cho phép ứng dụng tự động cập nhật mà **không cần người dùng xóa và cài đặt lại**. Ứng dụng sẽ tự động kiểm tra, tải về và cài đặt phiên bản mới.

## ✨ Tính năng chính

- ✅ **Kiểm tra phiên bản tự động** - Tự động phát hiện khi có phiên bản mới
- ✅ **Download thông minh** - Tải về với progress bar và hỗ trợ tiếp tục
- ✅ **Verify tính toàn vẹn** - Kiểm tra checksum SHA256 đảm bảo file không bị lỗi
- ✅ **Backup tự động** - Sao lưu phiên bản cũ trước khi cập nhật
- ✅ **Rollback khi lỗi** - Khôi phục về phiên bản cũ nếu cập nhật thất bại
- ✅ **GUI thân thiện** - Giao diện đẹp với progress bar và thông tin chi tiết

## 🗜️ Compression với UPX

### Lợi ích của UPX Compression

- **Giảm 50-70% dung lượng** file EXE
- **KHÔNG làm mất tính năng** - Chương trình chạy bình thường
- **KHÔNG cần giải nén** - Windows tự động xử lý
- **Tăng tốc độ tải** - File nhỏ hơn = download nhanh hơn

### Cài đặt UPX

#### Windows:
```powershell
# Tải UPX từ GitHub
# Visit: https://github.com/upx/upx/releases

# Hoặc dùng Chocolatey
choco install upx

# Hoặc dùng Scoop
scoop install upx
```

#### Kiểm tra cài đặt:
```powershell
upx --version
```

### Sử dụng trong MSI Builder GUI

1. Mở **build_msi_gui.py**
2. Tick vào ✅ **"🗜️ Compress EXE với UPX (giảm 50-70%)"**
3. Build như bình thường
4. Chương trình sẽ tự động nén sau khi build xong

### Compression thủ công:

```powershell
# Nén với best compression
upx --best --lzma your_app.exe

# Nén nhanh
upx --fast your_app.exe

# Decompress (nếu cần)
upx -d your_app.exe
```

## 🏗️ Cách thiết lập Auto-Update

### Bước 1: Tích hợp vào ứng dụng

Khi build với **build_msi_gui.py**, tick vào:
- ✅ **"🔄 Tích hợp Auto-Update"**
- Nhập **Update URL** (URL đến file `version.json`)

Ví dụ URL:
```
https://example.com/myapp/version.json
https://raw.githubusercontent.com/username/repo/main/version.json
https://yourserver.com/updates/version.json
```

### Bước 2: Thêm code vào ứng dụng chính

Trong file Python chính của bạn (VD: `gui_app.py`):

```python
import tkinter as tk
from auto_updater import check_and_prompt_update

class MyApp:
    def __init__(self, root):
        self.root = root
        # ... setup UI của bạn ...
        
        # Kiểm tra update khi khởi động
        self.check_for_updates()
    
    def check_for_updates(self):
        """Kiểm tra và prompt update nếu có"""
        try:
            from update_config import UPDATE_URL, APP_VERSION, APP_NAME
            
            # Check ngay khi khởi động
            check_and_prompt_update(
                parent_window=self.root,
                current_version=APP_VERSION,
                update_url=UPDATE_URL,
                app_name=APP_NAME
            )
        except ImportError:
            # Không có auto-update được tích hợp
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
```

### Bước 3: Tạo Update Server

#### Option 1: Sử dụng GitHub Releases (Miễn phí)

1. **Tạo repository trên GitHub**

2. **Tạo file `version.json` trong repo:**
```json
{
  "version": "1.1.0",
  "release_date": "2024-11-11",
  "download_url": "https://github.com/username/myapp/releases/download/v1.1.0/MyApp-v1.1.0.zip",
  "checksum": "abc123def456...",
  "size": "5.2 MB",
  "changelog": "- Thêm tính năng ABC\n- Sửa lỗi XYZ\n- Cải thiện hiệu suất",
  "minimum_version": "1.0.0",
  "critical": false
}
```

3. **Tạo Release mới:**
   - Vào **Releases** → **Create a new release**
   - Tag version: `v1.1.0`
   - Upload file ZIP chứa update
   - Publish release

4. **Lấy URL:**
   - Click chuột phải vào file ZIP → Copy link
   - Dán vào `download_url` trong `version.json`

5. **Tính checksum:**
```powershell
# Windows PowerShell
Get-FileHash -Algorithm SHA256 MyApp-v1.1.0.zip
```

6. **Update URL sẽ là:**
```
https://raw.githubusercontent.com/username/myapp/main/version.json
```

#### Option 2: Sử dụng Web Server riêng

1. **Cấu trúc thư mục:**
```
/var/www/myapp/
├── version.json          # Thông tin phiên bản
├── updates/
│   ├── v1.1.0/
│   │   └── update.zip
│   ├── v1.2.0/
│   │   └── update.zip
```

2. **Cập nhật `version.json`** sau mỗi lần release

3. **Update URL:**
```
https://yourserver.com/myapp/version.json
```

### Bước 4: Tạo Update Package

#### Cách 1: ZIP thủ công

```powershell
# Sau khi build, zip thư mục build
cd your_project\build\exe.win-amd64-3.11
Compress-Archive -Path * -DestinationPath MyApp-v1.1.0.zip
```

#### Cách 2: Script tự động

Tạo file `create_update_package.py`:
```python
import os
import zipfile
import hashlib
from pathlib import Path

def create_update_package(build_dir, output_name, version):
    """Create update package with checksum"""
    
    # Create ZIP
    zip_path = f"{output_name}-v{version}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, build_dir)
                zipf.write(file_path, arcname)
    
    # Calculate checksum
    sha256_hash = hashlib.sha256()
    with open(zip_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    checksum = sha256_hash.hexdigest()
    file_size = os.path.getsize(zip_path)
    
    print(f"✓ Created: {zip_path}")
    print(f"  Size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
    print(f"  SHA256: {checksum}")
    
    return zip_path, checksum, file_size

if __name__ == "__main__":
    build_dir = "build/exe.win-amd64-3.11"
    output_name = "MyApp"
    version = "1.1.0"
    
    create_update_package(build_dir, output_name, version)
```

## 📝 Template `version.json`

```json
{
  "version": "1.1.0",
  "release_date": "2024-11-11",
  "download_url": "https://github.com/user/repo/releases/download/v1.1.0/update.zip",
  "checksum": "sha256_hash_here",
  "size": "5.2 MB",
  "changelog": "- Tính năng mới ABC\n- Sửa lỗi XYZ\n- Cải thiện hiệu suất",
  "minimum_version": "1.0.0",
  "critical": false,
  "notes": {
    "vi": "Phiên bản này cải thiện đáng kể hiệu suất.",
    "en": "This version significantly improves performance."
  }
}
```

### Giải thích các trường:

- **version**: Phiên bản mới (bắt buộc)
- **release_date**: Ngày phát hành
- **download_url**: URL tải về file update (bắt buộc)
- **checksum**: SHA256 hash để verify tính toàn vẹn
- **size**: Dung lượng file (hiển thị cho user)
- **changelog**: Nội dung cập nhật (hiển thị trong dialog)
- **minimum_version**: Phiên bản tối thiểu để update
- **critical**: `true` = bắt buộc update ngay
- **notes**: Ghi chú đa ngôn ngữ

## 🔄 Quy trình Update tự động

```
1. App khởi động
   ↓
2. Kiểm tra version.json từ server
   ↓
3. So sánh version hiện tại vs version mới
   ↓
4. Nếu có update → Hiển thị dialog
   ↓
5. User nhấn "Cập nhật ngay"
   ↓
6. Download update package
   ↓
7. Verify checksum SHA256
   ↓
8. Backup phiên bản hiện tại
   ↓
9. Extract và copy file mới
   ↓
10. Restart ứng dụng
```

## 🔧 Troubleshooting

### Lỗi: "Cannot find auto_updater module"

**Nguyên nhân:** Chưa tích hợp auto-update vào build

**Giải pháp:**
1. Mở `build_msi_gui.py`
2. Tick vào ✅ "🔄 Tích hợp Auto-Update"
3. Build lại

### Lỗi: "Connection timeout"

**Nguyên nhân:** Không kết nối được đến update server

**Giải pháp:**
- Kiểm tra internet connection
- Kiểm tra URL có đúng không
- Kiểm tra server có hoạt động không

### Lỗi: "Checksum mismatch"

**Nguyên nhân:** File download bị lỗi hoặc checksum sai

**Giải pháp:**
- Tính lại checksum của file ZIP
- Cập nhật lại `version.json`
- Upload lại file nếu cần

### Lỗi: UPX không nén được

**Nguyên nhân:** File DLL hoặc EXE đặc biệt không tương thích

**Giải pháp:**
- Bỏ tick "🗜️ Compress EXE với UPX"
- Hoặc nén thủ công với options khác:
```powershell
upx --force your_app.exe
```

## 📊 Best Practices

### 1. Version Numbering
Sử dụng **Semantic Versioning** (SemVer):
```
MAJOR.MINOR.PATCH
1.0.0 → 1.0.1 → 1.1.0 → 2.0.0
```

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### 2. Testing Updates

Trước khi release:
1. Test trên máy local
2. Test với 1-2 beta users
3. Monitor lỗi trong 24h đầu
4. Release rộng rãi

### 3. Backup Strategy

- Luôn giữ backup của 2-3 phiên bản gần nhất
- Test rollback process
- Document rollback procedure

### 4. Update Frequency

- **Patch**: Mỗi 1-2 tuần (bug fixes)
- **Minor**: Mỗi 1-2 tháng (features)
- **Major**: Mỗi 6-12 tháng (big changes)

### 5. Changelog Format

```markdown
## Version 1.1.0 (2024-11-11)

### ✨ Tính năng mới
- Thêm chức năng XYZ
- Cải thiện UI/UX

### 🐛 Sửa lỗi
- Fix crash khi ABC
- Fix memory leak

### ⚡ Cải thiện
- Tăng tốc độ 20%
- Giảm dung lượng RAM
```

## 🔒 Security Notes

### Bảo mật Update Process

1. **Sử dụng HTTPS** cho update URL
2. **Verify checksum** trước khi install
3. **Code signing** cho EXE (optional)
4. **Không lưu credentials** trong code

### Ví dụ code signing (Windows):

```powershell
# Cần certificate từ CA authority
signtool sign /f mycert.pfx /p password /t http://timestamp.digicert.com MyApp.exe
```

## 📚 Resources

- **UPX Homepage**: https://upx.github.io/
- **GitHub Releases API**: https://docs.github.com/en/rest/releases
- **Semantic Versioning**: https://semver.org/
- **Python Packaging**: https://packaging.python.org/

## 🎯 Example Projects

### Project 1: Image to ICO Converter

```python
# gui_app.py
import tkinter as tk
from auto_updater import check_and_prompt_update

APP_VERSION = "1.0.0"
APP_NAME = "ImageToICO"
UPDATE_URL = "https://example.com/imagetoico/version.json"

class ImageConverter:
    def __init__(self, root):
        self.root = root
        # ... setup UI ...
        
        # Check updates on startup
        self.root.after(1000, self.check_updates)
    
    def check_updates(self):
        check_and_prompt_update(
            self.root, 
            APP_VERSION, 
            UPDATE_URL, 
            APP_NAME
        )
```

### Project 2: Multi-window App

```python
# main.py
def main():
    root = tk.Tk()
    
    # Show splash screen
    splash = SplashScreen(root)
    
    # Check for updates while loading
    def check_and_start():
        from auto_updater import check_and_prompt_update
        check_and_prompt_update(root, "1.0.0", UPDATE_URL, "MyApp")
        splash.destroy()
        # Start main app
        MainApp(root)
    
    root.after(2000, check_and_start)
    root.mainloop()
```

## 💡 Tips & Tricks

### Tip 1: Silent Update Check
Kiểm tra update im lặng (không hiện dialog nếu không có):

```python
from auto_updater import AutoUpdater

updater = AutoUpdater("1.0.0", UPDATE_URL, "MyApp")
update_info = updater.check_for_updates(silent=True)

if update_info:
    # Có update → show notification
    show_notification("Có phiên bản mới!")
```

### Tip 2: Scheduled Update Check
Kiểm tra update mỗi N giờ:

```python
import threading
import time

def periodic_update_check():
    while True:
        time.sleep(3600)  # Check every hour
        updater.check_for_updates(silent=True)

threading.Thread(target=periodic_update_check, daemon=True).start()
```

### Tip 3: Update Notification Badge
Hiện badge khi có update:

```python
def show_update_badge(menu):
    """Add red dot to menu"""
    update_info = updater.check_for_updates(silent=True)
    if update_info:
        menu.add_command(
            label="🔴 Cập nhật có sẵn",
            command=show_update_dialog
        )
```

## 🚀 Quick Start Checklist

- [ ] Cài đặt UPX (optional, cho compression)
- [ ] Tích hợp auto-update vào build
- [ ] Thiết lập update server (GitHub/Web)
- [ ] Tạo `version.json`
- [ ] Thêm update check code vào app
- [ ] Test update flow
- [ ] Build và release phiên bản mới
- [ ] Monitor logs và feedback

---

**Chúc bạn thành công với Auto-Update! 🎉**

Nếu có thắc mắc, tham khảo file `auto_updater.py` hoặc mở issue trên GitHub.
