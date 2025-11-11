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

### For End-Users | Cho Người dùng Cuối

**📦 Đã có file MSI/EXE?** Chỉ cần:

```powershell
# Option 1: MSI Installer (Recommended)
# 1. Double-click: image-to-ico-converter-1.0.0-win64.msi
# 2. Follow installation wizard
# 3. Launch from Start Menu

# Option 2: Portable ZIP
# 1. Extract: App-Change-Image-to-Ico-Portable.zip
# 2. Double-click: "App Change Image To .Ico File.exe"
# 3. No installation needed!
```

**💡 Không cần Python, không cần dependencies!**

---

### For Developers | Cho Nhà phát triển

#### Installation | Cài đặt

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

#### Usage | Sử dụng

```powershell
# Image Converter GUI
uv run python src/gui_app.py

# MSI Builder GUI
uv run python src/build_msi_gui.py

# Or use batch scripts | Hoặc dùng scripts
scripts\run_converter.bat
scripts\run_builder.bat
```

#### Building Distribution | Build phân phối

```powershell
# Build MSI installer and Portable ZIP
uv run python src/build_msi_gui.py

# Or build manually
uv run python cx_freeze_setup.py build         # Build EXE
uv run python cx_freeze_setup.py bdist_msi     # Build MSI

# Output files in dist/
# - image-to-ico-converter-1.0.0-win64.msi (MSI Installer)
# - App-Change-Image-to-Ico-Portable.zip (Portable version)
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

- **🔄 [Auto-Update Guide](docs/guides/AUTO_UPDATE_GUIDE.md)** - Auto-update system (500+ lines)
- **🤖 [Auto-Setup Guide](docs/guides/AUTO_SETUP_GUIDE.md)** - Automatic configuration
- **🏗️ [Build Guide](docs/guides/BUILD_GUIDE.md)** - Building & deployment
- **⚡ [UV Quickstart](docs/guides/UV_QUICKSTART.md)** - UV package manager

## 🎯 Use Cases | Các trường hợp Sử dụng

### 📦 For End-Users | Người dùng Cuối

**Scenario 1: Convert logo to favicon**
```powershell
# If using MSI installed version:
Start Menu → "App Change Image To .Ico File"
# → Select logo.png
# → Save as favicon.ico
# → Upload to website

# If using portable ZIP:
Double-click "App Change Image To .Ico File.exe"
# → Same steps as above
```

**Scenario 2: Batch convert multiple images**
```powershell
# Drag & drop multiple image files into the app
# All files will be converted to .ico format
```

### 🛠️ For Python Developers | Nhà phát triển Python

**Scenario 1: Build your Python app to standalone EXE**
```powershell
# Launch MSI Builder GUI
uv run python src/build_msi_gui.py
# → Auto-detects your project info (GitHub, version, icon)
# → Click "Build MSI" or "Build EXE"
# → Get professional installer/executable
# → Share with users without Python!

# Output in dist/ folder:
# - your-app-1.0.0-win64.msi (MSI Installer)
# - Portable ZIP (if created)
```

**Scenario 2: Add auto-update to your app**
```python
# Add to your main app file
from auto_updater import check_and_prompt_update

# At app startup
check_and_prompt_update(
    root_window,
    current_version="1.0.0",
    update_url="https://raw.githubusercontent.com/user/repo/main/version.json",
    app_name="MyApp"
)
# → Automatic version checking
# → Download and install updates
# → Backup and rollback support
```

**Scenario 3: Programmatic image conversion**
```python
from convert_to_ico import convert_image_to_ico

# Single file conversion
convert_image_to_ico("logo.png", "favicon.ico")

# Batch conversion
import os
for file in os.listdir("images/"):
    if file.endswith((".png", ".jpg")):
        convert_image_to_ico(f"images/{file}", f"icons/{file}.ico")
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

### 👥 For End-Users | Người dùng Cuối

**New to the app?** Start here:

1. **📦 [Quick Start](docs/user-guide/quick-start.md)** (5 min)
   - Download MSI or Portable ZIP
   - Install and launch
   - Convert your first image

2. **🎨 [Image Converter Guide](docs/user-guide/image-converter.md)** (15 min)
   - Advanced features
   - Batch conversion
   - Tips & tricks

3. **❓ [FAQ](docs/FAQ.md)** (10 min)
   - Common questions
   - Troubleshooting
   - Best practices

**Total time: ~30 minutes to become proficient!**

---

### 🛠️ For Python Developers | Nhà phát triển

**Want to build your own apps?**

1. **📦 [Quick Start](docs/user-guide/quick-start.md)** (10 min)
   - Setup development environment
   - Run from source code
   - Test features

2. **🏗️ [MSI Builder Guide](docs/user-guide/msi-builder.md)** (20 min)
   - Build standalone EXE
   - Create MSI installer
   - Distribution basics

3. **📦 [Distribution Guide](docs/guides/DISTRIBUTION_GUIDE.md)** (30 min)
   - Advanced build options
   - Testing before release
   - Publishing workflow

4. **🔄 [Auto-Update Guide](docs/guides/AUTO_UPDATE_GUIDE.md)** (30 min)
   - Add auto-update to your app
   - Version management
   - Release automation

**Total time: ~90 minutes to build & distribute your first app!**

---

### 👨‍💻 For Advanced Developers | Chuyên gia

**Want to extend or contribute?**

1. **📁 [STRUCTURE.md](STRUCTURE.md)** (10 min)
   - Project organization
   - File structure
   - Module overview

2. **🏛️ [Architecture](docs/developer-guide/architecture.md)** (30 min)
   - System design
   - Component interaction
   - Design patterns

3. **📖 [API Reference](docs/developer-guide/api-reference.md)** (40 min)
   - Complete API documentation
   - Code examples
   - Integration guide

4. **💻 [Examples](examples/)** (30 min)
   - Code review
   - Use cases
   - Best practices

5. **🔧 [Extending](docs/developer-guide/extending.md)** (45 min)
   - Custom features
   - Plugin development
   - Advanced customization

6. **🤝 [Contributing](docs/developer-guide/contributing.md)** (20 min)
   - Contribution workflow
   - Code standards
   - Pull request process

**Total time: ~3 hours to master the codebase!**

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
