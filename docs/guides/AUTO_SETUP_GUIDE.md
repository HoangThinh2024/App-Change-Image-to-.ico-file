# 🤖 Auto-Update Tự Động - Hướng dẫn Sử dụng

## 🎯 Tổng quan

**Auto-Update Tự Động** sẽ tự động phát hiện GitHub repository và thiết lập update URL **mà không cần người dùng nhập thủ công**.

### ✨ Lợi ích

- ✅ **Không cần nhập URL** - Tự động phát hiện từ git
- ✅ **Tự động tạo config** - Không cần tạo file thủ công
- ✅ **Detect version** - Tự động lấy version từ git tag/pyproject.toml
- ✅ **One-click setup** - Chỉ cần chọn project folder là xong

## 🚀 Cách sử dụng

### Bước 1: Đảm bảo project có Git

Project của bạn cần có git repository và remote origin trỏ đến GitHub:

```bash
# Check git remote
git remote -v

# Kết quả mong đợi:
# origin  https://github.com/username/repo.git (fetch)
# origin  https://github.com/username/repo.git (push)
```

Nếu chưa có:

```bash
# Init git (nếu chưa có)
git init

# Add GitHub remote
git remote add origin https://github.com/username/your-repo.git

# Push code
git add .
git commit -m "Initial commit"
git push -u origin main
```

### Bước 2: Sử dụng MSI Builder GUI

1. **Mở MSI Builder:**
   ```powershell
   uv run python build_msi_gui.py
   ```

2. **Chọn Project Folder:**
   - Click nút "📁" bên cạnh "Thư mục dự án"
   - Chọn thư mục project của bạn

3. **Tự động phát hiện:**
   - GUI sẽ tự động:
     - Phát hiện file Python chính
     - Phát hiện GitHub repository
     - Tạo Update URL
     - Fill app name và version

4. **Kiểm tra Log:**
   ```
   ✓ Đã chọn thư mục: C:\your-project
   ✓ Tự động phát hiện file chính: main.py
   
   🔍 Đang phát hiện thông tin Git...
   ✓ Phát hiện GitHub: username/repo
   ✓ Update URL: https://raw.githubusercontent.com/...
   ✓ App Name: Your Project
   ✓ Version: 1.0.0
   ✓ Auto-Update đã được thiết lập tự động!
   ```

5. **Build như bình thường:**
   - Tick ✅ "Tích hợp Auto-Update" (đã auto-enabled)
   - Tick ✅ "Compress EXE với UPX" (optional)
   - Click "Build EXE" hoặc "Build MSI"

### Bước 3: Publish Update (khi có version mới)

Sử dụng helper script để tự động tạo và publish:

```powershell
uv run --no-project python publish_update.py
```

Script sẽ hỏi:
- Version mới (vd: 1.0.1)
- App name (auto-detected)
- Build directory (auto-detected)
- Changelog

Sau đó tự động:
1. Tạo ZIP package với checksum
2. Tạo version.json
3. Commit và push version.json
4. Tạo GitHub Release (nếu có `gh` CLI)

## 📋 Files được tạo tự động

### 1. update_config.py

Được tạo tự động trong project folder khi build:

```python
"""
Auto-generated Update Configuration
"""

# Auto-detected from git repository
UPDATE_URL = "https://raw.githubusercontent.com/username/repo/main/version.json"
APP_VERSION = "1.0.0"
APP_NAME = "Your App"

# GitHub Repository Info
GITHUB_OWNER = "username"
GITHUB_REPO = "repo"
RELEASE_URL_TEMPLATE = "https://github.com/username/repo/releases/download/v{version}/{filename}"
```

### 2. version.json

Được tạo bởi `publish_update.py`:

```json
{
  "version": "1.0.1",
  "release_date": "2024-11-11",
  "download_url": "https://github.com/user/repo/releases/download/v1.0.1/App-v1.0.1.zip",
  "checksum": "abc123...",
  "size": "5.2 MB",
  "changelog": "- New features\n- Bug fixes"
}
```

## 🔍 Auto-Detect Features

### Phát hiện GitHub Repository

Script tự động đọc `.git/config` để lấy:
- Remote origin URL
- Parse GitHub owner/repo
- Tạo update URL

### Phát hiện Version

Tự động detect từ:
1. **Git tags** - `git describe --tags`
2. **pyproject.toml** - `version = "1.0.0"`
3. **__init__.py** - `__version__ = "1.0.0"`
4. **setup.py** - `version="1.0.0"`

### Phát hiện App Name

Tự động từ:
1. **Repo name** - Chuyển đổi từ `my-app` → `My App`
2. **Folder name** - Nếu không có git

## 🛠️ Helper Scripts

### 1. auto_update_helper.py

**Chức năng:**
- Phát hiện git repository
- Parse GitHub URL
- Tạo update URL
- Detect version từ nhiều nguồn
- Tạo update_config.py

**Sử dụng:**
```powershell
# Test detection
uv run --no-project python auto_update_helper.py

# Detect specific project
uv run --no-project python auto_update_helper.py path/to/project
```

### 2. publish_update.py

**Chức năng:**
- Tạo ZIP package
- Tính checksum SHA256
- Tạo version.json
- Commit và push
- Tạo GitHub Release (với `gh` CLI)

**Sử dụng:**
```powershell
# Interactive mode
uv run --no-project python publish_update.py

# Sẽ hỏi các thông tin cần thiết
```

## 📸 Screenshot Workflow

```
1. Mở build_msi_gui.py
   ↓
2. Chọn project folder
   ↓
3. [TỰ ĐỘNG] Phát hiện Git info
   ↓
4. [TỰ ĐỘNG] Fill update URL
   ↓
5. [TỰ ĐỘNG] Fill app name/version
   ↓
6. Click Build
   ↓
7. [TỰ ĐỘNG] Copy auto_updater.py
   ↓
8. [TỰ ĐỘNG] Tạo update_config.py
   ↓
9. Build hoàn thành!
```

## 🎯 Use Cases

### Case 1: Project mới

```bash
# 1. Tạo GitHub repo
gh repo create my-app --public --clone

# 2. Init project
cd my-app
# ... code your app ...

# 3. Build với Auto-Update
uv run python build_msi_gui.py
# → Chọn folder my-app
# → Tất cả tự động setup!
```

### Case 2: Project có sẵn

```bash
# 1. Add git remote (nếu chưa có)
git remote add origin https://github.com/username/existing-project.git

# 2. Build
uv run python build_msi_gui.py
# → Chọn project folder
# → Auto-detect và setup
```

### Case 3: Update version mới

```bash
# 1. Build version mới
uv run python build_msi_gui.py
# → Version: 1.0.1

# 2. Publish update
uv run --no-project python publish_update.py
# → Nhập changelog
# → Tự động tạo release
```

## ⚙️ Cấu hình nâng cao

### Disable Auto-Detect

Nếu muốn nhập thủ công:

1. Bỏ tick ✅ "🤖 Tự động phát hiện từ Git"
2. Update URL field sẽ editable
3. Nhập URL thủ công

### Custom Update URL

Nếu không dùng GitHub:

```python
# Trong build_msi_gui.py, bỏ tick auto-detect và nhập:
UPDATE_URL = "https://your-server.com/updates/version.json"
```

### Multiple Branches

Mặc định dùng `main` branch. Để đổi:

```python
# Trong auto_update_helper.py
def generate_update_url(owner, repo, branch="develop"):  # ← Đổi branch
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/version.json"
```

## 🔧 Troubleshooting

### ❌ "Không phát hiện được GitHub repository"

**Nguyên nhân:**
- Project chưa có git
- Hoặc remote origin không trỏ đến GitHub

**Giải pháp:**
```bash
# Check git remote
git remote -v

# Add origin nếu chưa có
git remote add origin https://github.com/user/repo.git
```

### ❌ "Import auto_update_helper could not be resolved"

**Nguyên nhân:**
- File auto_update_helper.py không cùng thư mục

**Giải pháp:**
- Copy `auto_update_helper.py` vào thư mục project
- Hoặc chạy từ thư mục chứa file

### ❌ Version không được detect

**Giải pháp:**
```bash
# Tạo git tag
git tag v1.0.0
git push --tags

# Hoặc thêm vào pyproject.toml
[project]
version = "1.0.0"
```

## 📚 Best Practices

### 1. Version Management

```bash
# Luôn dùng git tags cho version
git tag v1.0.0
git tag v1.0.1
git push --tags
```

### 2. Changelog

```markdown
## Version 1.0.1 (2024-11-11)

### ✨ New Features
- Feature A
- Feature B

### 🐛 Bug Fixes
- Fix issue #1
- Fix crash

### ⚡ Improvements
- Performance boost
```

### 3. Testing Update Flow

```bash
# 1. Build local test
uv run python build_msi_gui.py

# 2. Create fake version.json
echo '{"version": "1.0.1", ...}' > version.json

# 3. Test app update
# Run your app → Should detect update
```

### 4. GitHub Releases

```bash
# Install GitHub CLI
winget install GitHub.cli

# Login
gh auth login

# Create release automatically
uv run --no-project python publish_update.py
```

## 🎓 Advanced Examples

### Example 1: Multi-Platform

```python
# Detect platform in update_config.py
import sys

if sys.platform == "win32":
    DOWNLOAD_URL_TEMPLATE = "...Windows.zip"
elif sys.platform == "darwin":
    DOWNLOAD_URL_TEMPLATE = "...macOS.zip"
else:
    DOWNLOAD_URL_TEMPLATE = "...Linux.zip"
```

### Example 2: Beta Channel

```python
# Trong version.json
{
  "version": "1.1.0-beta",
  "channel": "beta",
  "stable_version": "1.0.5"
}
```

### Example 3: Staged Rollout

```python
# Trong version.json
{
  "version": "1.1.0",
  "rollout_percentage": 50,  # Release to 50% users first
  "minimum_version": "1.0.0"
}
```

## 🌟 Summary

Với **Auto-Update Tự Động**:

- ✅ **Không cần config thủ công** - Tất cả tự động
- ✅ **Detect từ Git** - Chỉ cần có GitHub repo
- ✅ **Helper scripts** - publish_update.py tự động hóa release
- ✅ **Production ready** - Checksum, rollback, backup

**Workflow ngắn gọn:**

1. Push code lên GitHub
2. Chọn project trong build_msi_gui.py
3. Build (tự động setup update)
4. Publish với publish_update.py
5. Done! 🎉

---

**Questions?** Xem thêm:
- AUTO_UPDATE_GUIDE.md - Chi tiết về update system
- NEW_FEATURES.md - Tổng hợp tính năng
