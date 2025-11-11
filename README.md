# App-Change-Image-to-.ico-file
Chương trình chuyển đổi file ảnh thành file .ico

## Mô tả / Description

Chương trình Python đơn giản để chuyển đổi các file ảnh (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP) sang định dạng .ico với nhiều kích thước.

A simple Python program to convert image files (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP) to .ico format with multiple sizes.

## Cài đặt / Installation

### Yêu cầu / Requirements
- Python 3.7 trở lên / Python 3.7 or higher
- Pillow library

### Cài đặt thư viện / Install dependencies

```bash
pip install -r requirements.txt
```

Hoặc / Or:

```bash
pip install Pillow
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
- ✅ Hỗ trợ nhiều định dạng ảnh đầu vào / Support multiple input image formats (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP)
- ✅ Xem trước ảnh trước khi chuyển đổi / Preview image before conversion
- ✅ Tự động chuyển đổi sang RGBA để hỗ trợ trong suốt / Automatic RGBA conversion for transparency support
- ✅ Tạo icon với nhiều kích thước / Create icons with multiple sizes (16x16, 32x32, 48x48, 64x64, 128x128, 256x256)
- ✅ Giao diện dòng lệnh đơn giản / Simple command-line interface
- ✅ Xử lý lỗi rõ ràng / Clear error handling
- ✅ Hỗ trợ build file MSI installer cho Windows / Support building MSI installer for Windows

## Kích thước icon mặc định / Default Icon Sizes

Chương trình tự động tạo icon với các kích thước sau:
- 16x16 pixels
- 32x32 pixels
- 48x48 pixels
- 64x64 pixels
- 128x128 pixels
- 256x256 pixels

## Build MSI Installer (Chỉ dành cho Windows / Windows Only)

### Yêu cầu / Requirements
- Windows operating system
- Python 3.7 trở lên / Python 3.7 or higher
- cx_Freeze (sẽ được cài tự động / will be installed automatically)

### Cách build / How to build

1. Cài đặt tất cả dependencies / Install all dependencies:
```bash
pip install -r requirements.txt
```

2. Chạy script build / Run the build script:
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
