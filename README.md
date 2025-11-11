# 🎨 App Change Image to .ICO File

> **Professional Python toolkit for image conversion, application building, and automated updates**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![uv](https://img.shields.io/badge/uv-compatible-brightgreen.svg)](https://github.com/astral-sh/uv)

## 📋 Overview | Tổng quan

This project provides a complete suite of tools for Python developers and end-users:

- **🎨 Image to ICO Converter** - Convert images to .ico format with GUI/CLI
- **🏗️ MSI Builder** - Build professional EXE/MSI installers for Python apps
- **🔄 Auto-Updater** - Automatic update system for your applications
- **🤖 Auto-Setup** - Automatic GitHub detection and configuration

---

### **Đây là bộ công cụ chuyên nghiệp bao gồm:**

- **🎨 Chuyển đổi ảnh sang ICO** - GUI và CLI, hỗ trợ nhiều định dạng
- **🏗️ Build MSI Installer** - Tạo file cài đặt chuyên nghiệp cho Python app
- **🔄 Tự động cập nhật** - Hệ thống update tự động cho ứng dụng
- **🤖 Tự động thiết lập** - Phát hiện GitHub và config tự động

## ✨ Key Features | Tính năng Chính

### 🎨 Image Converter

- ✅ **Multi-format support**: PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP → ICO
- ✅ **GUI with zoom controls**: Zoom in/out, fit to window, drag to resize
- ✅ **CLI for automation**: Batch processing và scripting
- ✅ **Multi-size ICO**: Auto-generate 16x16, 32x32, 48x48, 256x256

### 🏗️ MSI Builder

- ✅ **One-click build**: Build EXE/MSI with simple GUI
- ✅ **Auto-detect**: Tự động phát hiện main script, GitHub repo, version
- ✅ **Icon management**: Browse và integrate .ico files
- ✅ **Auto-cleanup**: Tự động dọn dẹp file build/temp
- ✅ **Compression**: UPX compression giảm 50-70% kích thước
- ✅ **Multi-project**: Lưu/load config cho nhiều project

### 🔄 Auto-Update System

- ✅ **Automatic version check**: Kiểm tra update tự động
- ✅ **Smart download**: Progress bar, resume support
- ✅ **Checksum verification**: SHA256 integrity check
- ✅ **Backup & rollback**: An toàn với tự động rollback
- ✅ **GitHub integration**: Direct integration với GitHub Releases

### 🤖 Auto-Setup

- ✅ **Git detection**: Tự động phát hiện GitHub repository
- ✅ **Config generation**: Auto-generate update_config.py
- ✅ **Version detection**: Từ git tags, pyproject.toml, __init__.py
- ✅ **Zero-config**: Không cần người dùng nhập URL thủ công

## 🚀 Quick Start | Bắt đầu Nhanh

### Installation | Cài đặt

```powershell
# 1. Clone repository
git clone https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file.git
cd App-Change-Image-to-.ico-file

# 2. Install UV (recommended) | Cài UV (khuyến nghị)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 3. Install dependencies | Cài dependencies
uv sync

# OR with pip | HOẶC dùng pip
pip install -r requirements.txt
```

### Usage | Sử dụng

#### For End-Users | Cho Người dùng

```powershell
# Image Converter GUI
uv run python src/gui_app.py

# MSI Builder GUI
uv run python src/build_msi_gui.py

# Or use batch scripts | Hoặc dùng scripts
scripts\run_converter.bat
scripts\run_builder.bat
```

#### For Developers | Cho Developers

```powershell
# Auto-detect project info
uv run --no-project python src/auto_update_helper.py

# Publish update
uv run --no-project python tools/publish_update.py

# Run examples
uv run python examples/example_usage.py
```

## 📁 Project Structure | Cấu trúc Dự án

```
App-Change-Image-to-.ico-file/
├── 📂 src/                      # Source code
│   ├── gui_app.py               # Image Converter GUI
│   ├── convert_to_ico.py        # Converter CLI
│   ├── build_msi_gui.py         # MSI Builder GUI
│   ├── auto_updater.py          # Auto-Update Module
│   └── auto_update_helper.py    # Auto-Setup Helper
│
├── 📂 docs/                     # Documentation
│   ├── user-guide/              # For end-users
│   ├── developer-guide/         # For developers
│   └── *.md                     # Technical guides
│
├── 📂 examples/                 # Code examples
├── 📂 tools/                    # Utility tools
├── 📂 scripts/                  # Shell scripts
│
├── 📄 README.md                 # This file
├── 📄 STRUCTURE.md              # Structure explanation
└── 📄 pyproject.toml            # Project config
```

**📖 Chi tiết:** Xem [STRUCTURE.md](STRUCTURE.md)

## 📚 Documentation | Tài liệu

### For End-Users | Cho Người dùng

- **🚀 [Quick Start Guide](docs/user-guide/quick-start.md)** - Bắt đầu trong 5 phút
- **🎨 [Image Converter Guide](docs/user-guide/image-converter.md)** - Chi tiết Image Converter
- **🏗️ [MSI Builder Guide](docs/user-guide/msi-builder.md)** - Chi tiết MSI Builder
- **❓ [FAQ](docs/FAQ.md)** - Câu hỏi thường gặp

### For Developers | Cho Developers

- **🏛️ [Architecture](docs/developer-guide/architecture.md)** - System architecture
- **📖 [API Reference](docs/developer-guide/api-reference.md)** - API documentation
- **🔧 [Extending](docs/developer-guide/extending.md)** - Extend & customize
- **🤝 [Contributing](docs/developer-guide/contributing.md)** - Contribution guide

### Technical Deep-Dive | Kỹ thuật Chi tiết

- **🔄 [Auto-Update Guide](docs/AUTO_UPDATE_GUIDE.md)** - Auto-update system (500+ lines)
- **🤖 [Auto-Setup Guide](docs/AUTO_SETUP_GUIDE.md)** - Automatic configuration
- **🏗️ [Build Guide](docs/BUILD_GUIDE.md)** - Building & deployment
- **⚡ [UV Quickstart](docs/UV_QUICKSTART.md)** - UV package manager

## 🎯 Use Cases | Các trường hợp Sử dụng

### For End-Users | Cho Người dùng

```powershell
# Convert logo to favicon
uv run python src/gui_app.py
# → Select logo.png
# → Save as favicon.ico
# → Upload to website

# Build your Python app to EXE
uv run python src/build_msi_gui.py
# → Select your project folder
# → Click "Build EXE"
# → Share your_app.exe!
```

### For Developers | Cho Developers

```python
# Add auto-update to your app
from auto_updater import check_and_prompt_update

# At app startup
check_and_prompt_update(
    root_window,
    current_version="1.0.0",
    update_url="https://raw.githubusercontent.com/user/repo/main/version.json",
    app_name="MyApp"
)
```

**📖 Xem thêm examples:** [examples/](examples/)

## 🛠️ Requirements | Yêu cầu

### System | Hệ thống

- **OS**: Windows 10/11, macOS 10.14+, Linux
- **Python**: 3.8 or higher
- **RAM**: 2 GB minimum, 4 GB recommended
- **Disk**: 100 MB for installation

### Dependencies | Thư viện

- `Pillow >= 10.0.0` - Image processing
- `cx-Freeze >= 6.15.0` - Building executables
- `requests >= 2.31.0` - HTTP requests (for auto-update)
- `packaging >= 23.0` - Version comparison

**Tự động cài đặt:** `uv sync` hoặc `pip install -r requirements.txt`

## 🎓 Learning Path | Lộ trình Học

### Beginner | Người mới bắt đầu

1. **README.md** (5 min) - You are here!
2. **[Quick Start](docs/user-guide/quick-start.md)** (10 min) - Hands-on tutorial
3. **[Image Converter Guide](docs/user-guide/image-converter.md)** (15 min)
4. **[MSI Builder Guide](docs/user-guide/msi-builder.md)** (20 min)

### Advanced User | Người dùng Nâng cao

1. **[Auto-Update Guide](docs/AUTO_UPDATE_GUIDE.md)** (30 min)
2. **[Auto-Setup Guide](docs/AUTO_SETUP_GUIDE.md)** (20 min)
3. **[Build Guide](docs/BUILD_GUIDE.md)** (25 min)

### Developer | Nhà phát triển

1. **[STRUCTURE.md](STRUCTURE.md)** (10 min)
2. **[Architecture](docs/developer-guide/architecture.md)** (30 min)
3. **[API Reference](docs/developer-guide/api-reference.md)** (40 min)
4. **[Examples](examples/)** (code review)
5. **[Extending](docs/developer-guide/extending.md)** (custom features)

## 🤝 Contributing | Đóng góp

We welcome contributions! | Chúng tôi hoan nghênh mọi đóng góp!

**Cách contribute:**

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

**📖 Chi tiết:** [Contributing Guide](docs/developer-guide/contributing.md)

## 🐛 Bug Reports & Feature Requests

- **🐛 Bug Reports**: [GitHub Issues](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)
- **💡 Feature Requests**: [GitHub Discussions](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/discussions)
- **❓ Questions**: Check [FAQ](docs/FAQ.md) first

## 📜 License | Giấy phép

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Tóm tắt:** Bạn có thể tự do sử dụng, sửa đổi và phân phối code này.

## 🌟 Star History

If you find this project useful, please give it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=HoangThinh2024/App-Change-Image-to-.ico-file&type=Date)](https://star-history.com/#HoangThinh2024/App-Change-Image-to-.ico-file&Date)

## 📞 Contact | Liên hệ

- **Author**: HoangThinh2024
- **GitHub**: [@HoangThinh2024](https://github.com/HoangThinh2024)
- **Repository**: [App-Change-Image-to-.ico-file](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file)

## 🙏 Acknowledgments | Lời cảm ơn

- **Pillow** - Powerful image processing library
- **cx_Freeze** - Python to executable conversion
- **UV** - Ultra-fast Python package manager
- **GitHub** - Hosting and collaboration platform

## 📈 Project Stats

- **Lines of Code**: 5000+
- **Documentation**: 3000+ lines
- **Examples**: 10+ code examples
- **Tests**: Unit tests for all modules
- **Supported Formats**: 7+ image formats
- **Supported Platforms**: Windows, macOS, Linux

---

<div align="center">

**Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)**

**⭐ Star this repo if you find it helpful! ⭐**

[🚀 Quick Start](docs/user-guide/quick-start.md) • 
[📚 Documentation](docs/) • 
[🐛 Report Bug](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues) • 
[💡 Request Feature](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/discussions)

</div>
