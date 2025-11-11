# App-Change-Image-to-.ico-file
Chương trình chuyển đổi file ảnh thành file .ico

## Mô tả / Description

Chương trình Python đơn giản để chuyển đổi các file ảnh (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP) sang định dạng .ico với nhiều kích thước.

A simple Python program to convert image files (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP) to .ico format with multiple sizes.

## Cài đặt / Installation

### Yêu cầu / Requirements
- Python 3.7 trở lên / Python 3.7 or higher
- [uv](https://github.com/astral-sh/uv) (khuyến nghị / recommended) hoặc / or pip

### Cài đặt uv (nếu chưa có) / Install uv (if not installed)

```bash
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Cài đặt thư viện / Install dependencies

**Với uv (Khuyến nghị / Recommended):**

```bash
# Sync tất cả dependencies
uv sync

# Hoặc cài đặt trực tiếp
uv pip install -e .

# Hoặc chỉ cài packages cần thiết
uv pip install Pillow cx-Freeze
```

**Với pip (Truyền thống / Traditional):**

```bash
pip install -r requirements.txt

# Hoặc
pip install Pillow cx-Freeze
```

## Cách sử dụng / Usage

### 1. Sử dụng giao diện đồ họa (GUI) / Using Graphical User Interface (GUI)

Chạy ứng dụng GUI với giao diện thân thiện / Run the GUI application with user-friendly interface:

```bash
python gui_app.py
```

![GUI Screenshot](https://github.com/user-attachments/assets/95bef040-626d-46f3-b38a-7d56134fe10b)

Giao diện GUI cung cấp / The GUI interface provides:
- ✅ Chọn file ảnh dễ dàng / Easy file selection
- ✅ Xem trước ảnh trước khi chuyển đổi / Preview image before conversion
- ✅ Chọn vị trí lưu file / Choose output location
- ✅ Giao diện thân thiện người dùng / User-friendly interface
- ✅ Hỗ trợ song ngữ Việt-Anh / Bilingual support (Vietnamese-English)

### 2. Sử dụng từ dòng lệnh / Command Line Usage

##### Cú pháp cơ bản / Basic syntax

```bash
python convert_to_ico.py <input_image> [output_ico]
```

#### Ví dụ / Examples

1. Chuyển đổi ảnh với tên file tự động / Convert image with automatic filename:
```bash
python convert_to_ico.py image.png
# Tạo file: image.ico / Creates: image.ico
```

2. Chỉ định tên file đầu ra / Specify output filename:
```bash
python convert_to_ico.py photo.jpg my_icon.ico
# Tạo file: my_icon.ico / Creates: my_icon.ico
```

3. Chuyển đổi từ các định dạng khác / Convert from other formats:
```bash
python convert_to_ico.py picture.bmp
python convert_to_ico.py image.gif favicon.ico
python convert_to_ico.py photo.webp
```

### 3. Sử dụng như một module Python / Use as a Python Module

```python
from convert_to_ico import convert_image_to_ico

# Chuyển đổi cơ bản / Basic conversion
convert_image_to_ico('input.png')

# Chỉ định tên file đầu ra / Specify output filename
convert_image_to_ico('input.jpg', 'output.ico')

# Chỉ định kích thước tùy chỉnh / Custom sizes
convert_image_to_ico('input.png', 'custom.ico', sizes=[(32, 32), (64, 64)])
```

Xem file `example_usage.py` để biết thêm ví dụ / See `example_usage.py` for more examples.

## Tính năng / Features

- ✅ Giao diện đồ họa (GUI) thân thiện / User-friendly graphical interface (GUI)
- ✅ **Phóng to/thu nhỏ và kéo dãn cửa sổ** / **Zoom in/out and resizable window**
- ✅ Hỗ trợ nhiều định dạng ảnh đầu vào / Support multiple input image formats (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP)
- ✅ Xem trước ảnh trước khi chuyển đổi / Preview image before conversion
- ✅ Tự động chuyển đổi sang RGBA để hỗ trợ trong suốt / Automatic RGBA conversion for transparency support
- ✅ Tạo icon với nhiều kích thước / Create icons with multiple sizes (16x16, 32x32, 48x48, 64x64, 128x128, 256x256)
- ✅ Giao diện dòng lệnh đơn giản / Simple command-line interface
- ✅ Xử lý lỗi rõ ràng / Clear error handling
- ✅ **MSI Builder GUI - Công cụ build ứng dụng chuyên nghiệp** / **MSI Builder GUI - Professional app builder tool**

## Kích thước icon mặc định / Default Icon Sizes

Chương trình tự động tạo icon với các kích thước sau:
- 16x16 pixels
- 32x32 pixels
- 48x48 pixels
- 64x64 pixels
- 128x128 pixels
- 256x256 pixels

## Build MSI Installer (Chỉ dành cho Windows / Windows Only)

## 🏗️ MSI Builder GUI - Công cụ Build Chuyên Nghiệp / Professional Build Tool

**MSI Builder GUI** là công cụ mạnh mẽ giúp build bất kỳ ứng dụng Python nào thành file EXE và MSI installer với giao diện đồ họa trực quan.

**MSI Builder GUI** is a powerful tool that helps build any Python application into EXE and MSI installer with an intuitive graphical interface.

### ✨ Tính năng MSI Builder / MSI Builder Features

- ✅ **Giao diện đồ họa trực quan** / Intuitive graphical interface
- ✅ **Tương thích với mọi dự án Python** / Compatible with any Python project
- ✅ **Quản lý icon ứng dụng** / Application icon management
- ✅ **Tự động dọn dẹp file build** / Automatic build files cleanup
- ✅ **Dọn dẹp file rác sau build** / Clean up junk files after build
- ✅ **Lưu/Load cấu hình** / Save/Load configuration
- ✅ **Build log real-time** / Real-time build logging
- ✅ **Tùy chỉnh đầy đủ** / Full customization options
- ✅ **Hỗ trợ nhiều loại ứng dụng** / Support multiple app types

### 🚀 Cách sử dụng MSI Builder / How to Use MSI Builder

#### Khởi chạy GUI / Launch GUI:

```bash
# Cách 1: Chạy file GUI trực tiếp
python build_msi_gui.py

# Cách 2: Chạy qua build_msi.py
python build_msi.py --gui

# Cách 3: Sử dụng batch file (Windows)
run_builder_gui.bat
```

#### Khởi chạy CLI (Command Line):

```bash
python build_msi.py
```

### 📖 Các bước build với GUI / Build Steps with GUI

1. **Chọn dự án** / Select project
   - Chọn thư mục dự án Python
   - Chọn file Python chính (.py)

2. **Cấu hình ứng dụng** / Configure application
   - Điền tên ứng dụng, version, tác giả
   - Thêm mô tả
   - (Tùy chọn) Thêm icon .ico

3. **Tùy chọn build** / Build options
   - Tự động dọn dẹp file build cũ
   - Tạo shortcut trên Desktop
   - Optimize code

4. **Build** / Build
   - Build EXE: Nhanh, để test
   - Build MSI: Để phân phối
   - Build All: Build cả hai

5. **Kết quả** / Results
   - Mở thư mục build để xem file output
   - File EXE trong `build/`
   - File MSI trong `dist/`

### 🎨 Tạo Icon cho ứng dụng / Create Application Icon

Sử dụng **Image to ICO Converter** (trong project này):

1. Chạy `python gui_app.py`
2. Chọn ảnh PNG/JPG bất kỳ
3. Convert sang .ico
4. Sử dụng file .ico trong MSI Builder

### 🧹 Dọn dẹp file build / Clean Build Files

MSI Builder GUI tự động dọn dẹp:
- Thư mục `build/`
- Thư mục `dist/`
- Thư mục `__pycache__/`
- File `*.egg-info/`

Click nút **🧹 Clean Build Files** hoặc bật tùy chọn "Tự động dọn dẹp" trước khi build.

### 📚 Hướng dẫn chi tiết / Detailed Guide

Xem file **BUILD_GUIDE.md** để biết hướng dẫn chi tiết về:
- Cách sử dụng với các dự án khác
- Troubleshooting
- Tips & Tricks
- Advanced features

### 🎯 Demo với các ứng dụng khác / Demo with Other Applications

Chạy file demo để xem cách build các loại ứng dụng khác:

```bash
python demo_builder_usage.py
```

Demo bao gồm:
- ✅ Calculator app
- ✅ Notepad app
- ✅ Todo List app

### Build thủ công / Manual Build (Legacy)

### Yêu cầu / Requirements

- Windows operating system
- Python 3.7 trở lên / Python 3.7 or higher
- uv hoặc pip / uv or pip
- cx_Freeze (sẽ được cài tự động / will be installed automatically)

### Cách build / How to build

**Với uv (Khuyến nghị / Recommended):**

1. Cài đặt tất cả dependencies / Install all dependencies:

```bash
uv sync
```

2. Chạy script build / Run the build script:

```bash
uv run python build_msi.py
```

**Với pip (Truyền thống / Traditional):**

1. Cài đặt dependencies:

```bash
pip install -r requirements.txt
```

2. Chạy build:

```bash
python build_msi.py
```

3. File MSI sẽ được tạo trong thư mục `dist/` / MSI file will be created in `dist/` directory

### Build thủ công / Manual build

Nếu bạn muốn build thủ công / If you want to build manually:

```bash
# Build executable only
python setup.py build

# Build MSI installer
python setup.py bdist_msi
```

### Kết quả / Results
- **build/** - Chứa các file executable / Contains executable files
- **dist/** - Chứa file MSI installer / Contains MSI installer file

## Giấy phép / License

MIT License - Xem file LICENSE để biết thêm chi tiết / See LICENSE file for details
