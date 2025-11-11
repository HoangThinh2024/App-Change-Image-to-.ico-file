# 🚀 Quick Start Guide - Hướng dẫn Nhanh

**Thời gian: 5-10 phút** | **Dành cho: End-User & Developer** | **Level: Beginner**

---

## � For End-Users (Người dùng Cuối)

### ⚡ Không cần Python! Chỉ cần download và dùng

#### Option 1: MSI Installer (Khuyến nghị) ⭐

**Download:** `image-to-ico-converter-1.0.0-win64.msi` từ [Releases](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/releases)

**Cài đặt:**
1. **Double-click** file MSI
2. **Click** "Next" → "Install" → "Finish"
3. **Launch** từ Start Menu: "App Change Image To .Ico File"

✅ **Ưu điểm:**
- Cài đặt chuyên nghiệp
- Start Menu shortcut
- Dễ gỡ cài đặt (Control Panel → Programs)
- Không cần Python

**Sử dụng:**
1. Launch app từ Start Menu
2. Click "Browse Image" → Chọn ảnh
3. Click "Convert to ICO" → Chọn nơi lưu
4. Hoàn thành!

#### Option 2: Portable ZIP 📁

**Download:** `App-Change-Image-to-Ico-Portable.zip` từ [Releases](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/releases)

**Sử dụng:**
1. **Giải nén** ZIP vào bất kỳ folder nào
2. **Double-click** `App Change Image To .Ico File.exe`
3. Dùng ngay, không cần cài đặt!

✅ **Ưu điểm:**
- Không cần cài đặt
- Portable - chạy từ USB được
- Không động đến registry
- Không cần Python

**🎯 Bạn chọn gì?**
- **Dùng lâu dài trên PC** → Chọn MSI Installer
- **Dùng tạm thời/USB** → Chọn Portable ZIP

---

## 🛠️ For Developers (Nhà phát triển)

### Bước 1: Cài đặt Python

**Windows:**
```powershell
# Download Python từ python.org hoặc dùng winget
winget install Python.Python.3.11
```

**Kiểm tra cài đặt:**
```powershell
python --version
# Hoặc
py --version
```

### Bước 2: Cài đặt UV (Khuyến nghị - Nhanh hơn 10-100x)

```powershell
# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Kiểm tra:**
```powershell
uv --version
```

### Bước 3: Clone Repository

```powershell
# Download ZIP từ GitHub hoặc clone:
git clone https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file.git
cd App-Change-Image-to-.ico-file
```

### Bước 4: Cài đặt Dependencies

**Với UV (Khuyến nghị):**
```powershell
uv sync
```

**Với pip (Cách truyền thống):**
```powershell
pip install -r requirements.txt
```

## 🎨 Sử dụng Image to ICO Converter

### GUI - Giao diện Đồ họa

```powershell
# Với UV
uv run python src/gui_app.py

# Với Python thông thường
python src/gui_app.py
```

**Hoặc dùng script:**
```powershell
scripts\run_converter.bat
```

### Các bước sử dụng:

1. **Chọn ảnh:** Click "Browse Image" → Chọn file ảnh (PNG, JPG, BMP...)
2. **Xem trước:** Ảnh hiển thị với zoom controls
3. **Chọn nơi lưu:** Click "Browse Output" → Chọn vị trí lưu file .ico
4. **Convert:** Click "Convert to ICO" → Đợi vài giây → Hoàn thành!

### Tính năng:

- ✅ **Zoom In/Out**: Phóng to/thu nhỏ ảnh preview
- ✅ **Fit to Window**: Fit ảnh vừa màn hình
- ✅ **Drag to Resize**: Kéo góc cửa sổ để resize
- ✅ **Multi-size ICO**: Tự động tạo ICO với nhiều kích thước (16x16, 32x32, 48x48, 256x256)

## 🏗️ Sử dụng MSI Builder

### GUI - Build Installer

```powershell
# Với UV
uv run python src/build_msi_gui.py

# Với Python thông thường
python src/build_msi_gui.py
```

**Hoặc dùng script:**
```powershell
scripts\run_builder.bat
```

### Các bước build:

1. **Chọn Project:**
   - Click "📁" bên cạnh "Thư mục dự án"
   - Chọn folder chứa code Python của bạn

2. **Tự động phát hiện:**
   - File Python chính tự động được detect
   - GitHub repo tự động được detect (nếu có)
   - Update URL tự động được tạo

3. **Điền thông tin:**
   - **App Name**: Tên ứng dụng (tự động từ repo)
   - **Version**: Phiên bản (1.0.0, 1.0.1...)
   - **Author**: Tên tác giả
   - **Description**: Mô tả ngắn

4. **Chọn Icon (Optional):**
   - Click "🖼️" để chọn file .ico
   - Hoặc dùng Image Converter để tạo icon

5. **Tùy chọn:**
   - ✅ **Tự động dọn dẹp** - Xóa file build cũ
   - ✅ **Tạo shortcut** - Desktop shortcut
   - ✅ **Optimize code** - Giảm kích thước
   - ✅ **Compress EXE** - Nén với UPX (giảm 50-70%)
   - ✅ **Auto-Update** - Tích hợp tự động cập nhật

6. **Build:**
   - Click **"Build EXE"** - Chỉ tạo file .exe
   - Click **"Build MSI"** - Chỉ tạo installer .msi
   - Click **"Build All"** - Tạo cả hai

### Kết quả:

```
your-project/
├── build/
│   └── exe.win-amd64-3.11/
│       └── YourApp.exe          ← File EXE
│
└── dist/
    └── YourApp-1.0.0-win64.msi  ← File MSI Installer
```

## 📦 Ví dụ Đầy đủ

### Ví dụ 1: Convert Logo → ICO cho Website

```powershell
# 1. Chạy Image Converter
uv run python src/gui_app.py

# 2. Chọn file: logo.png
# 3. Chọn output: favicon.ico
# 4. Click Convert
# 5. Upload favicon.ico lên website
```

### Ví dụ 2: Build App Python thành EXE

Giả sử bạn có app Python đơn giản:

```python
# my_app/main.py
import tkinter as tk

root = tk.Tk()
root.title("My App")
tk.Label(root, text="Hello World!").pack(pady=20)
root.mainloop()
```

**Build steps:**

```powershell
# 1. Chạy MSI Builder
uv run python src/build_msi_gui.py

# 2. Chọn folder: my_app/
# 3. File chính: main.py (auto-detect)
# 4. App Name: My App
# 5. Version: 1.0.0
# 6. Click "Build EXE"

# 7. Kết quả: my_app/build/exe.../MyApp.exe
```

### Ví dụ 3: Build với Auto-Update

```powershell
# 1. Push code lên GitHub
git init
git remote add origin https://github.com/username/my-app.git
git add .
git commit -m "Initial commit"
git push -u origin main

# 2. Chạy MSI Builder
uv run python src/build_msi_gui.py

# 3. Chọn project folder
# → Auto-detect GitHub repo
# → Auto-fill Update URL

# 4. Tick ✅ Auto-Update
# 5. Click Build

# 6. App của bạn có tự động update!
```

## 🎯 Common Tasks

### Task: Convert nhiều ảnh cùng lúc

**Dùng CLI:**

```powershell
# Convert 1 file
python src/convert_to_ico.py input.png output.ico

# Convert nhiều files (loop)
$images = Get-ChildItem *.png
foreach ($img in $images) {
    python src/convert_to_ico.py $img.Name "$($img.BaseName).ico"
}
```

### Task: Build nhiều project

**Sử dụng saved config:**

```powershell
# 1. Build project A
# 2. Click "Save Config"
# 3. File build_config.json được tạo

# 4. Copy config cho project khác
Copy-Item project-a/build_config.json project-b/

# 5. Build project B - settings tự động load
```

### Task: Update app version mới

```powershell
# 1. Build version mới (vd: 1.0.1)
uv run python src/build_msi_gui.py

# 2. Publish update
uv run python tools/publish_update.py
# → Nhập changelog
# → Tự động tạo release

# 3. Users tự động nhận update!
```

## 🆘 Troubleshooting

### ❌ "Python is not recognized"

**Fix:**
```powershell
# Cài lại Python và check "Add to PATH"
winget install Python.Python.3.11

# Hoặc dùng py launcher
py --version
py src/gui_app.py
```

### ❌ "ModuleNotFoundError: No module named 'PIL'"

**Fix:**
```powershell
# Cài đặt dependencies
uv sync

# Hoặc
pip install Pillow
```

### ❌ "UPX not found" khi compress

**Fix:**
```powershell
# Cài UPX
choco install upx

# Hoặc download: https://upx.github.io/
# Extract và thêm vào PATH
```

### ❌ Build failed - "cx_Freeze not found"

**Fix:**
```powershell
# Cài cx_Freeze
uv pip install cx-Freeze

# Hoặc
pip install cx-Freeze
```

## 📚 Next Steps

Sau khi làm quen với Quick Start:

### Cho End-User:
1. **Image Converter**: Đọc [docs/user-guide/image-converter.md](../user-guide/image-converter.md)
2. **MSI Builder**: Đọc [docs/user-guide/msi-builder.md](../user-guide/msi-builder.md)
3. **FAQ**: Xem [docs/FAQ.md](../FAQ.md)

### Cho Developer:
1. **Architecture**: Đọc [docs/developer-guide/architecture.md](../developer-guide/architecture.md)
2. **API Reference**: Xem [docs/developer-guide/api-reference.md](../developer-guide/api-reference.md)
3. **Examples**: Xem code trong [examples/](../../examples/)

## 💡 Tips & Tricks

### Tip 1: Keyboard Shortcuts

**Image Converter:**
- `Ctrl + O`: Open image
- `Ctrl + S`: Save as ICO
- `Ctrl + +`: Zoom in
- `Ctrl + -`: Zoom out
- `Ctrl + 0`: Reset zoom
- `Ctrl + F`: Fit to window

### Tip 2: Batch Processing

**Convert folder ảnh:**
```powershell
# PowerShell script
Get-ChildItem -Filter *.png | ForEach-Object {
    python src/convert_to_ico.py $_.FullName "$($_.BaseName).ico"
}
```

### Tip 3: Custom Icon Sizes

**Sửa trong `src/convert_to_ico.py`:**
```python
# Dòng 15-16
sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
```

### Tip 4: Quick Launch

**Tạo Desktop shortcut:**
```powershell
# Windows
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\Image Converter.lnk")
$Shortcut.TargetPath = "uv"
$Shortcut.Arguments = "run python src/gui_app.py"
$Shortcut.WorkingDirectory = "C:\path\to\App-Change-Image-to-.ico-file"
$Shortcut.Save()
```

## 🎓 Video Tutorials

Coming soon:
- [ ] Image Converter Basic Usage (5 min)
- [ ] MSI Builder Step-by-Step (10 min)
- [ ] Auto-Update Setup (15 min)
- [ ] Advanced Features (20 min)

## 📞 Getting Help

- **Quick Questions**: [docs/FAQ.md](../FAQ.md)
- **Bug Reports**: [GitHub Issues](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/discussions)
- **Email**: (your-email@example.com)

---

**Chúc bạn sử dụng thành công! 🎉**

Nếu gặp vấn đề, đừng ngại tạo issue trên GitHub hoặc xem thêm documentation chi tiết.
