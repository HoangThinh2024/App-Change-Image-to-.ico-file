# 🚀 Quick Start với uv

## Tại sao dùng uv?

**uv** là package manager Python thế hệ mới từ Astral (tác giả của Ruff):
- ⚡ **Nhanh hơn 10-100x** so với pip
- 🎯 **Đơn giản hơn**: Một công cụ cho mọi thứ
- 🔒 **Lockfile tự động**: Đảm bảo reproducible builds
- 🌐 **Cross-platform**: Windows, macOS, Linux
- 📦 **Không cần virtualenv**: uv tự quản lý

## Cài đặt uv

### Windows (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Hoặc với pip:
```bash
pip install uv
```

## Sử dụng với Project này

### 1. Clone repo:
```bash
git clone https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file.git
cd App-Change-Image-to-.ico-file
```

### 2. Sync dependencies (tự động cài đặt):
```bash
uv sync
```

### 3. Chạy ứng dụng:

**Image to ICO Converter:**
```bash
uv run python gui_app.py
```

**MSI Builder GUI:**
```bash
uv run python build_msi_gui.py
```

**CLI Converter:**
```bash
uv run python convert_to_ico.py image.png
```

### 4. Build MSI:
```bash
uv run python build_msi.py
# Hoặc với GUI:
uv run python build_msi.py --gui
```

## So sánh uv vs pip

| Tính năng | uv | pip |
|-----------|-----|-----|
| Tốc độ cài đặt | ⚡ 10-100x nhanh hơn | Chậm |
| Lockfile | ✅ Tự động | ❌ Cần pip-tools |
| Quản lý Python | ✅ Tích hợp | ❌ Cần pyenv |
| Cache | ✅ Thông minh | ⚠️ Cơ bản |
| Dependency resolution | ✅ Nhanh | ⚠️ Chậm |
| Virtual environment | ✅ Tự động | ❌ Cần tạo thủ công |

## Các lệnh uv thường dùng

```bash
# Sync dependencies (cài đặt từ pyproject.toml)
uv sync

# Thêm package mới
uv add pillow

# Xóa package
uv remove pillow

# Cập nhật tất cả packages
uv sync --upgrade

# Chạy script
uv run python script.py

# Chạy command trong venv
uv run pytest

# Hiển thị packages đã cài
uv pip list

# Freeze dependencies
uv pip freeze
```

## Migration từ pip sang uv

### Nếu bạn đang dùng pip:

**Trước đây:**
```bash
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate trên Windows
pip install -r requirements.txt
python gui_app.py
```

**Với uv (đơn giản hơn):**
```bash
uv sync
uv run python gui_app.py
```

### Không cần requirements.txt nữa!

uv đọc trực tiếp từ `pyproject.toml`:
- ✅ Tiêu chuẩn Python hiện đại
- ✅ Metadata đầy đủ hơn
- ✅ Lockfile tự động
- ✅ Quản lý dev dependencies

## Troubleshooting

### uv: command not found
```bash
# Thêm uv vào PATH (Windows)
$env:Path += ";$HOME\.cargo\bin"

# Hoặc restart terminal sau khi cài
```

### uv sync failed
```bash
# Clean cache và thử lại
uv clean
uv sync
```

### Vẫn muốn dùng pip?
```bash
# Không vấn đề gì! Project vẫn hỗ trợ pip
pip install -r requirements.txt
python gui_app.py
```

## Lợi ích cho Project này

1. **Build nhanh hơn**: uv giúp cài cx_Freeze và dependencies nhanh chóng
2. **Reproducible**: Lockfile đảm bảo build giống nhau trên mọi máy
3. **Modern**: Theo chuẩn Python hiện đại (pyproject.toml)
4. **Đơn giản**: Ít bước hơn, ít lỗi hơn

## Tài liệu

- uv Documentation: https://docs.astral.sh/uv/
- GitHub: https://github.com/astral-sh/uv
- Astral Blog: https://astral.sh/blog

## Kết luận

**uv** là tương lai của Python package management. Nó:
- ⚡ Cực kỳ nhanh
- 🎯 Dễ sử dụng
- 🔒 An toàn và đáng tin cậy
- 🆓 Hoàn toàn miễn phí và open source

Thử ngay hôm nay! 🚀
