# 📁 Project Structure - Cấu trúc Dự án

## 🗂️ Tổng quan

```
App-Change-Image-to-.ico-file/
│
├── 📂 src/                          # Source code chính
│   ├── gui_app.py                   # Image to ICO Converter GUI
│   ├── convert_to_ico.py            # ICO Converter CLI
│   ├── build_msi_gui.py             # MSI Builder GUI
│   ├── auto_updater.py              # Auto-Update Module
│   └── auto_update_helper.py        # Auto-Update Helper
│
├── 📂 docs/                         # Documentation
│   ├── 📂 user-guide/               # Hướng dẫn cho End-User
│   │   ├── image-converter.md       # Hướng dẫn Image Converter
│   │   ├── msi-builder.md           # Hướng dẫn MSI Builder
│   │   └── quick-start.md           # Quick Start cho người mới
│   │
│   ├── 📂 developer-guide/          # Hướng dẫn cho Developer
│   │   ├── architecture.md          # Kiến trúc hệ thống
│   │   ├── api-reference.md         # API Documentation
│   │   ├── extending.md             # Mở rộng chức năng
│   │   └── contributing.md          # Đóng góp cho project
│   │
│   ├── AUTO_UPDATE_GUIDE.md         # Chi tiết Auto-Update
│   ├── AUTO_SETUP_GUIDE.md          # Auto-Setup Guide
│   ├── BUILD_GUIDE.md               # Build & Deployment
│   ├── UV_QUICKSTART.md             # UV Package Manager
│   └── FAQ.md                       # Câu hỏi thường gặp
│
├── 📂 examples/                     # Ví dụ code
│   ├── example_usage.py             # Ví dụ cơ bản
│   ├── example_auto_update.py       # Ví dụ Auto-Update
│   ├── demo.py                      # Demo app
│   └── demo_builder_usage.py        # Demo MSI Builder
│
├── 📂 tools/                        # Tools & Utilities
│   ├── publish_update.py            # Publish Update Tool
│   └── setup_dev.py                 # Dev Environment Setup
│
├── 📂 scripts/                      # Scripts tiện ích
│   ├── run_converter.bat            # Chạy Image Converter (Windows)
│   ├── run_builder.bat              # Chạy MSI Builder (Windows)
│   └── install_deps.bat             # Cài đặt dependencies
│
├── 📂 tests/                        # Unit tests
│   ├── test_converter.py
│   ├── test_builder.py
│   └── test_updater.py
│
├── 📄 README.md                     # README chính (tổng quan)
├── 📄 STRUCTURE.md                  # File này - giải thích cấu trúc
├── 📄 CHANGELOG.md                  # Lịch sử thay đổi
├── 📄 LICENSE                       # Giấy phép MIT
│
├── 📄 pyproject.toml                # Python project config
├── 📄 requirements.txt              # Dependencies
├── 📄 .python-version               # Python version cho uv
├── 📄 .gitignore                    # Git ignore rules
│
└── 📄 version.json.example          # Template version.json

```

## 📚 Chi tiết từng thư mục

### 📂 `src/` - Source Code

Chứa tất cả source code chính của project:

- **`gui_app.py`** - Image to ICO Converter với GUI
  - Giao diện đồ họa để convert ảnh
  - Zoom, resize, preview
  - Export multi-size ICO
  
- **`convert_to_ico.py`** - CLI version của converter
  - Command-line interface
  - Batch processing
  - Script integration

- **`build_msi_gui.py`** - MSI Builder GUI
  - Build EXE/MSI installer
  - Icon management
  - Auto-cleanup
  - Auto-Update integration
  
- **`auto_updater.py`** - Auto-Update Module
  - Core update logic
  - Download & verify
  - Backup & rollback
  
- **`auto_update_helper.py`** - Helper cho Auto-Update
  - Auto-detect Git info
  - Generate configs
  - Version detection

### 📂 `docs/` - Documentation

#### 📂 `docs/user-guide/` - Cho End-User

Hướng dẫn đơn giản, dễ hiểu cho người dùng cuối:

- **`quick-start.md`** - Bắt đầu nhanh (5 phút)
- **`image-converter.md`** - Hướng dẫn chi tiết Image Converter
- **`msi-builder.md`** - Hướng dẫn chi tiết MSI Builder

#### 📂 `docs/developer-guide/` - Cho Developer

Tài liệu kỹ thuật cho developers:

- **`architecture.md`** - Kiến trúc hệ thống
- **`api-reference.md`** - API docs & code examples
- **`extending.md`** - Mở rộng & customize
- **`contributing.md`** - Guidelines để contribute

#### 📄 Các guides khác

- **`AUTO_UPDATE_GUIDE.md`** - Deep dive vào Auto-Update
- **`AUTO_SETUP_GUIDE.md`** - Setup tự động
- **`BUILD_GUIDE.md`** - Build & deployment
- **`UV_QUICKSTART.md`** - UV package manager
- **`FAQ.md`** - Câu hỏi thường gặp

### 📂 `examples/` - Code Examples

Ví dụ code ready-to-use:

- **`example_usage.py`** - Ví dụ cơ bản
- **`example_auto_update.py`** - 5 ví dụ integrate Auto-Update
- **`demo.py`** - Demo app đơn giản
- **`demo_builder_usage.py`** - Demo MSI Builder API

### 📂 `tools/` - Tools & Utilities

Command-line tools:

- **`publish_update.py`** - Tự động publish updates
  - Tạo ZIP package
  - Generate version.json
  - Upload to GitHub Release

- **`setup_dev.py`** - Setup môi trường dev
  - Install dependencies
  - Configure git hooks
  - Setup pre-commit

### 📂 `scripts/` - Shell Scripts

Scripts tiện ích cho Windows:

- **`run_converter.bat`** - Launch Image Converter
- **`run_builder.bat`** - Launch MSI Builder  
- **`install_deps.bat`** - Cài đặt dependencies

### 📂 `tests/` - Unit Tests

Test coverage cho tất cả modules:

- **`test_converter.py`** - Tests cho converter
- **`test_builder.py`** - Tests cho builder
- **`test_updater.py`** - Tests cho updater

## 🎯 Use Cases

### 1. End-User muốn convert ảnh

```bash
# Option 1: GUI
python src/gui_app.py

# Option 2: Batch script
scripts/run_converter.bat
```

### 2. Developer muốn build MSI

```bash
# Option 1: GUI
python src/build_msi_gui.py

# Option 2: Batch script
scripts/run_builder.bat
```

### 3. Developer muốn tìm hiểu code

```
1. Đọc docs/developer-guide/architecture.md
2. Xem examples/example_usage.py
3. Đọc docs/developer-guide/api-reference.md
4. Xem source trong src/
```

### 4. Developer muốn contribute

```
1. Đọc docs/developer-guide/contributing.md
2. Fork repo
3. Make changes
4. Submit PR
```

## 🔄 Migration từ cấu trúc cũ

File mapping từ root → `src/`:

```
Root                    →  src/
─────────────────────────────────────
gui_app.py              →  src/gui_app.py
convert_to_ico.py       →  src/convert_to_ico.py
build_msi_gui.py        →  src/build_msi_gui.py
auto_updater.py         →  src/auto_updater.py
auto_update_helper.py   →  src/auto_update_helper.py
```

Documentation mapping:

```
Root                    →  docs/
─────────────────────────────────────
AUTO_UPDATE_GUIDE.md    →  docs/AUTO_UPDATE_GUIDE.md
AUTO_SETUP_GUIDE.md     →  docs/AUTO_SETUP_GUIDE.md
BUILD_GUIDE.md          →  docs/BUILD_GUIDE.md
UV_*.md                 →  docs/UV_*.md
```

Examples mapping:

```
Root                    →  examples/
─────────────────────────────────────
example_usage.py        →  examples/example_usage.py
example_auto_update.py  →  examples/example_auto_update.py
demo*.py                →  examples/demo*.py
```

Tools mapping:

```
Root                    →  tools/
─────────────────────────────────────
publish_update.py       →  tools/publish_update.py
```

## 📖 Documentation Hierarchy

```
README.md (Tổng quan)
    │
    ├─→ docs/user-guide/quick-start.md      (Cho người mới)
    │   ├─→ docs/user-guide/image-converter.md
    │   └─→ docs/user-guide/msi-builder.md
    │
    ├─→ docs/developer-guide/architecture.md (Cho dev)
    │   ├─→ docs/developer-guide/api-reference.md
    │   ├─→ docs/developer-guide/extending.md
    │   └─→ docs/developer-guide/contributing.md
    │
    └─→ docs/AUTO_UPDATE_GUIDE.md           (Technical deep-dive)
        └─→ docs/AUTO_SETUP_GUIDE.md
```

## 🚀 Quick Commands

```bash
# End-User Commands
uv run python src/gui_app.py              # Launch Image Converter
uv run python src/build_msi_gui.py        # Launch MSI Builder

# Developer Commands  
uv run python tools/publish_update.py     # Publish update
uv run python tools/setup_dev.py          # Setup dev environment
uv run pytest tests/                      # Run tests

# Scripts (Windows)
scripts\run_converter.bat                 # Quick launch converter
scripts\run_builder.bat                   # Quick launch builder
scripts\install_deps.bat                  # Install dependencies
```

## 💡 Benefits của cấu trúc mới

### ✅ Tổ chức rõ ràng
- Source code tách biệt trong `src/`
- Documentation có cấu trúc trong `docs/`
- Examples dễ tìm trong `examples/`

### ✅ Dễ maintain
- Mỗi component có README riêng
- Clear separation of concerns
- Easy to find & update

### ✅ User-friendly
- End-users có guides đơn giản
- Developers có technical docs
- Quick-start cho người mới

### ✅ Scalable
- Dễ thêm modules mới vào `src/`
- Dễ thêm docs vào `docs/`
- Dễ thêm examples vào `examples/`

## 🎓 Learning Path

### Cho End-User:
```
1. README.md (5 min)
2. docs/user-guide/quick-start.md (10 min)
3. docs/user-guide/image-converter.md (15 min)
4. docs/user-guide/msi-builder.md (20 min)
```

### Cho Developer:
```
1. README.md (5 min)
2. STRUCTURE.md (10 min)
3. docs/developer-guide/architecture.md (20 min)
4. docs/developer-guide/api-reference.md (30 min)
5. examples/example_usage.py (code review)
6. docs/developer-guide/extending.md (custom features)
```

## 📞 Getting Help

- **Quick questions**: docs/FAQ.md
- **User issues**: docs/user-guide/
- **Dev questions**: docs/developer-guide/
- **Bug reports**: GitHub Issues
- **Feature requests**: GitHub Discussions

---

**Cấu trúc này giúp project:**
- ✅ Professional & organized
- ✅ Easy to navigate
- ✅ Friendly cho both users & developers
- ✅ Scalable & maintainable
