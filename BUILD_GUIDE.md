# 🏗️ MSI Builder GUI - Hướng dẫn sử dụng

## 📋 Tổng quan

**MSI Builder GUI** là công cụ mạnh mẽ giúp bạn build ứng dụng Python thành file EXE và MSI installer với giao diện đồ họa trực quan.

## ✨ Tính năng chính

### 🎯 Tính năng cơ bản:
- ✅ Build file EXE từ Python script
- ✅ Build file MSI installer (chỉ trên Windows)
- ✅ Giao diện đồ họa thân thiện, dễ sử dụng
- ✅ Hỗ trợ thêm icon cho ứng dụng (.ico)
- ✅ Tự động dọn dẹp file build cũ
- ✅ Hiển thị log build real-time

### 🚀 Tính năng nâng cao:
- ✅ **Tương thích với mọi dự án Python** (không chỉ app hiện tại)
- ✅ **Quản lý icon**: Thêm icon tùy chỉnh cho ứng dụng
- ✅ **Dọn dẹp tự động**: Xóa file build cũ, file rác sau khi build
- ✅ **Lưu/Load cấu hình**: Tiết kiệm thời gian cho các lần build sau
- ✅ **Build log chi tiết**: Theo dõi quá trình build real-time
- ✅ **Tùy chỉnh đầy đủ**: Tên app, version, author, description, v.v.

## 🚀 Cách sử dụng

### Khởi chạy GUI:
```bash
# Cách 1: Chạy file GUI trực tiếp
python build_msi_gui.py

# Cách 2: Chạy qua build_msi.py với tham số --gui
python build_msi.py --gui
python build_msi.py -g
python build_msi.py gui
```

### Khởi chạy CLI (Command Line):
```bash
# Chạy build trực tiếp (không có GUI)
python build_msi.py
```

## 📖 Hướng dẫn chi tiết

### Bước 1: Cài đặt dự án
1. **Chọn thư mục dự án**: Click "📁 Browse" để chọn thư mục chứa dự án Python
2. **Chọn file Python chính**: File `.py` chính của ứng dụng (tự động phát hiện nếu có)

### Bước 2: Thông tin ứng dụng
Điền các thông tin cần thiết:
- **Tên ứng dụng**: Tên hiển thị của app (VD: "MyApp", "ImageConverter")
- **Phiên bản**: Version number (VD: "1.0.0", "2.1.5")
- **Tác giả**: Tên tác giả/công ty
- **Mô tả**: Mô tả ngắn gọn về ứng dụng

### Bước 3: Icon ứng dụng (Tùy chọn)
1. Click "🖼️ Browse" để chọn file icon (.ico)
2. Hoặc để trống nếu không cần icon
3. **💡 Tip**: Sử dụng **Image to ICO Converter** để tạo icon từ ảnh PNG/JPG

### Bước 4: Tùy chọn build
Chọn các tùy chọn phù hợp:
- ✅ **Tự động dọn dẹp file build cũ**: Xóa thư mục build/dist cũ trước khi build
- ✅ **Tạo shortcut trên Desktop**: Tự động tạo shortcut khi cài đặt
- ✅ **Optimize code**: Giảm kích thước file output

### Bước 5: Build ứng dụng
Chọn một trong các nút sau:
- **🔨 Build EXE**: Chỉ build file EXE
- **📦 Build MSI**: Chỉ build file MSI installer (Windows only)
- **🚀 Build All**: Build cả EXE và MSI

### Các chức năng tiện ích:
- **🧹 Clean Build Files**: Xóa tất cả file build cũ
- **📂 Open Build Folder**: Mở thư mục build trong File Explorer
- **💾 Save Config**: Lưu cấu hình hiện tại để sử dụng lần sau

## 📁 Cấu trúc thư mục sau khi build

```
your-project/
├── build/                      # Chứa file EXE
│   └── exe.win-amd64-3.x/
│       └── YourApp.exe
├── dist/                       # Chứa file MSI
│   └── YourApp-1.0.0-amd64.msi
├── setup.py                    # File cấu hình build (tự động tạo)
└── build_config.json           # File lưu cấu hình (nếu đã Save)
```

## 🧹 Dọn dẹp file build

### Tự động:
- Bật tùy chọn "Tự động dọn dẹp file build cũ" trước khi build

### Thủ công:
- Click nút **🧹 Clean Build Files** trong GUI
- Hoặc xóa thủ công các thư mục: `build/`, `dist/`, `__pycache__/`, `*.egg-info/`

## 🎨 Tạo Icon cho ứng dụng

### Cách 1: Sử dụng Image to ICO Converter GUI
1. Mở `gui_app.py` (Image to ICO Converter)
2. Chọn ảnh PNG/JPG/... của bạn
3. Convert sang .ico
4. Sử dụng file .ico vừa tạo trong MSI Builder

### Cách 2: Sử dụng công cụ online
- [ICO Convert](https://icoconvert.com/)
- [ConvertICO](https://convertio.co/png-ico/)

## 🔧 Tương thích với nhiều dự án

MSI Builder GUI được thiết kế để làm việc với **BẤT KỲ dự án Python nào**, không chỉ riêng Image to ICO Converter:

### Ví dụ các dự án có thể build:
- ✅ Ứng dụng Tkinter GUI
- ✅ Ứng dụng PyQt/PySide
- ✅ Game Pygame
- ✅ Web server Flask/Django (với một số điều chỉnh)
- ✅ Command-line tools
- ✅ Data processing scripts
- ✅ Automation tools

### Điều kiện:
- Dự án phải có file Python chính (entry point)
- Đã cài đặt đầy đủ dependencies
- Có thể chạy được trên Python 3.x

## 📦 Yêu cầu hệ thống

### Dependencies:

**Với uv (Khuyến nghị - Nhanh hơn 10-100x):**

```bash
# Cài đặt uv
# Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sau đó sync dependencies:
uv sync

# Hoặc cài đặt thủ công:
uv pip install cx-Freeze Pillow
```

**Với pip (Truyền thống):**

```bash
pip install cx_Freeze
pip install Pillow  # Nếu dự án sử dụng xử lý ảnh
```

### Hệ điều hành:
- **Windows**: Hỗ trợ đầy đủ (EXE + MSI)
- **Linux/Mac**: Chỉ hỗ trợ build EXE

## ❓ Troubleshooting

### Lỗi: "uv not found"

**Cài đặt uv (Khuyến nghị):**

```bash
# Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Lỗi: "cx_Freeze not installed"

**Với uv:**

```bash
uv pip install cx-Freeze
```

**Với pip:**

```bash
pip install cx_Freeze
```

### Lỗi: "Cannot find main script"
- Kiểm tra đường dẫn file Python chính
- Đảm bảo file tồn tại và có phần mở rộng .py

### Lỗi: "Build failed"
- Xem log chi tiết trong cửa sổ Output
- Kiểm tra dependencies của dự án
- Thử clean build files và build lại

### File MSI quá lớn:
- Bật tùy chọn "Optimize code"
- Loại bỏ các dependencies không cần thiết
- Sử dụng virtual environment

## 💡 Tips & Tricks

1. **Lưu cấu hình**: Luôn click "💾 Save Config" sau khi cấu hình xong để không phải nhập lại lần sau

2. **Icon chất lượng cao**: Sử dụng ảnh PNG 256x256 hoặc lớn hơn để tạo icon đẹp

3. **Test trước khi phát hành**: 
   - Build EXE trước để test nhanh
   - Build MSI sau khi đã test kỹ

4. **Virtual Environment**: Build từ virtual environment để tránh include thư viện không cần thiết

5. **Clean build**: Thường xuyên clean để tránh lỗi cache

## 🎯 Use Cases

### Case 1: Build app cho khách hàng
1. Chọn project của bạn
2. Điền đầy đủ thông tin app (tên, version, author)
3. Thêm icon chuyên nghiệp
4. Build MSI để gửi cho khách hàng

### Case 2: Quick test trong quá trình phát triển
1. Load config đã lưu
2. Build EXE nhanh
3. Test ngay trong thư mục build

### Case 3: Build nhiều version
1. Thay đổi version number
2. Save config với tên khác
3. Build và giữ lại nhiều version

## 📞 Support

Nếu gặp vấn đề hoặc có góp ý, vui lòng:
- Kiểm tra phần Troubleshooting ở trên
- Xem log chi tiết trong Output window
- Tham khảo tài liệu cx_Freeze: https://cx-freeze.readthedocs.io/

## 📝 License

Công cụ này thuộc về dự án Image to ICO Converter.
