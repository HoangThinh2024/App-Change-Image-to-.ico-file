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

### Cú pháp cơ bản / Basic syntax

```bash
python convert_to_ico.py <input_image> [output_ico]
```

### Ví dụ / Examples

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

## Tính năng / Features

- ✅ Hỗ trợ nhiều định dạng ảnh đầu vào / Support multiple input image formats (PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP)
- ✅ Tự động chuyển đổi sang RGBA để hỗ trợ trong suốt / Automatic RGBA conversion for transparency support
- ✅ Tạo icon với nhiều kích thước / Create icons with multiple sizes (16x16, 32x32, 48x48, 64x64, 128x128, 256x256)
- ✅ Giao diện dòng lệnh đơn giản / Simple command-line interface
- ✅ Xử lý lỗi rõ ràng / Clear error handling

## Kích thước icon mặc định / Default Icon Sizes

Chương trình tự động tạo icon với các kích thước sau:
- 16x16 pixels
- 32x32 pixels
- 48x48 pixels
- 64x64 pixels
- 128x128 pixels
- 256x256 pixels

## Giấy phép / License

MIT License - Xem file LICENSE để biết thêm chi tiết / See LICENSE file for details
