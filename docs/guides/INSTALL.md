# 🚀 Cài đặt nhanh với uv

## Chỉ 3 bước:

### 1️⃣ Cài uv (nếu chưa có)

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2️⃣ Sync dependencies

```bash
uv sync
```

### 3️⃣ Chạy app

```bash
# Image Converter
uv run python gui_app.py

# MSI Builder
uv run python build_msi_gui.py
```

## ✅ Xong!

**Lợi ích:**
- ⚡ Nhanh hơn pip **10-100x**
- 🎯 Đơn giản hơn (không cần venv)
- 🔒 Lockfile tự động

---

**Vẫn muốn dùng pip?** Không sao cả:
```bash
pip install -r requirements.txt
python gui_app.py
```

Xem thêm: [UV_QUICKSTART.md](UV_QUICKSTART.md)
