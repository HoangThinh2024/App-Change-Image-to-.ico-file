# 🏗️ MSI Builder - Complete User Guide

> **Build professional EXE and MSI installers for your Python applications**

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Basic Workflow](#basic-workflow)
5. [Advanced Features](#advanced-features)
6. [Auto-Update Integration](#auto-update-integration)
7. [Compression with UPX](#compression-with-upx)
8. [Multi-Project Management](#multi-project-management)
9. [Troubleshooting](#troubleshooting)
10. [FAQ](#faq)

---

## Overview

MSI Builder là công cụ GUI mạnh mẽ để build Python applications thành EXE hoặc MSI installers chuyên nghiệp, với tính năng auto-update và compression tích hợp.

### What Can It Do?

- **Build EXE**: Single executable file cho Windows
- **Build MSI**: Professional installer với Start Menu integration
- **Auto-Update**: Tích hợp hệ thống update tự động
- **Compression**: Giảm 50-70% kích thước với UPX
- **Auto-Detect**: Tự động phát hiện GitHub repo và config
- **Multi-Project**: Quản lý nhiều projects cùng lúc

---

## Features

### ✅ Core Features

- **One-Click Build**: Build EXE/MSI with simple button click
- **Auto-Detect Main Script**: Tự động tìm main.py, app.py, gui_app.py, v.v.
- **Icon Integration**: Browse và embed .ico files
- **Version Management**: Auto-detect từ Git tags hoặc manual input
- **Dependency Management**: Auto-include packages
- **Build Cleanup**: Tự động xóa temp files

### ✅ Auto-Update System

- **GitHub Integration**: Tự động phát hiện GitHub repository
- **Auto-Config**: Generate update_config.py tự động
- **Version Check**: Built-in update checker
- **Zero Manual Config**: Không cần nhập URL thủ công

### ✅ Compression

- **UPX Integration**: Automatic compression với UPX
- **Size Reduction**: 50-70% smaller EXE files
- **Performance**: Minimal impact on execution speed
- **Optional**: Enable/disable compression per build

### ✅ Multi-Project Support

- **Save Configs**: Lưu config cho từng project
- **Load Configs**: Nhanh chóng switch between projects
- **Recent Projects**: Quick access to recent builds

---

## Getting Started

### Prerequisites

```powershell
# 1. Python 3.8+
python --version

# 2. Install dependencies
uv sync
# OR
pip install -r requirements.txt

# 3. Install UPX (optional, for compression)
# Download from: https://upx.github.io/
# Extract to: C:\upx\ hoặc add to PATH
```

### Launch MSI Builder

```powershell
# Method 1: Using UV (recommended)
uv run python src/build_msi_gui.py

# Method 2: Using Python directly
python src/build_msi_gui.py

# Method 3: Using batch script
scripts\run_builder.bat
```

---

## Basic Workflow

### Interface Overview

```
╔═══════════════════════════════════════════════╗
║  MSI Builder - Build Python Apps              ║
╠═══════════════════════════════════════════════╣
║  Project Folder:  [____________] [Browse]     ║
║  Main Script:     [____________] [Browse]     ║
║  App Name:        [MyApp_______]              ║
║  Version:         [1.0.0_______]              ║
║  Company:         [MyCompany___]              ║
║  Icon Path:       [____________] [Browse]     ║
║  ☑ Enable Auto-Update                         ║
║  ☑ Auto-Detect Update URL                     ║
║  Update URL:      [https://...] (readonly)    ║
║  ☑ Compress with UPX                          ║
║  Build Type:      ● EXE  ○ MSI                ║
╠═══════════════════════════════════════════════╣
║  [Build EXE]  [Save Config]  [Load Config]   ║
╚═══════════════════════════════════════════════╝
```

### Step-by-Step: Build Your First EXE

#### Step 1: Select Project

1. Click **"Browse"** next to "Project Folder"
2. Navigate to your Python project directory
3. Select folder containing your main script
4. GUI auto-detects main script (e.g., `main.py`, `app.py`)

**Auto-Detection:**
- Main script: `main.py`, `app.py`, `gui_app.py`, `__main__.py`
- GitHub repo: From `.git/config`
- Version: From git tags, `pyproject.toml`, `__init__.py`

#### Step 2: Configure App Details

Fill in the fields:

- **App Name**: Your application name (e.g., "MyAwesomeApp")
  - Used for: EXE filename, Start Menu shortcut
  - Auto-generated from project folder name

- **Version**: Version number (e.g., "1.0.0")
  - Format: `MAJOR.MINOR.PATCH` (semantic versioning)
  - Auto-detected from Git tags if available

- **Company**: Your company/developer name
  - Used for: Installer metadata, Start Menu folder

- **Icon Path**: Path to .ico file (optional)
  - Click "Browse" to select
  - Leave empty for default Python icon
  - Tip: Use Image Converter to create ICO!

#### Step 3: Enable Auto-Update (Optional)

✅ **Check "Enable Auto-Update"**
- Adds update checker to your app
- Shows update notification on startup

✅ **Check "Auto-Detect Update URL"** (default)
- Automatically detects GitHub repository
- Generates update URL: `https://raw.githubusercontent.com/{owner}/{repo}/main/version.json`
- Update URL field is readonly (auto-filled)

**Manual Override:**
- Uncheck "Auto-Detect Update URL"
- Enter custom update URL manually

#### Step 4: Enable Compression (Optional)

✅ **Check "Compress with UPX"**
- Reduces EXE size by 50-70%
- Requires UPX installed (see [Compression](#compression-with-upx))
- Minimal performance impact

#### Step 5: Choose Build Type

**EXE (Recommended for simple apps):**
- Single `.exe` file
- Portable, no installation needed
- Fast build time (~30-60 seconds)

**MSI (For professional distribution):**
- Windows installer package
- Start Menu integration
- Add/Remove Programs entry
- Professional appearance
- Longer build time (~2-5 minutes)

#### Step 6: Build!

1. Click **"Build EXE"** or **"Build MSI"**
2. Wait for build process (progress shown)
3. Success message appears
4. Output files in `dist/` folder

**Output Files:**

```
your_project/
├── build/           # Temporary build files (auto-deleted)
├── dist/
│   ├── MyApp.exe    # Your executable!
│   └── ...          # Or MyApp.msi for MSI builds
└── setup.py         # Auto-generated build script
```

---

## Advanced Features

### Auto-Detect Update Configuration

When you select a Git repository as project folder:

1. **Auto-Detection Triggers:**
   - Reads `.git/config`
   - Parses GitHub URL (SSH or HTTPS)
   - Extracts owner and repo name
   - Generates update URL

2. **Auto-Generated Files:**
   - `update_config.py` in project folder
   - Contains: `UPDATE_URL`, `CURRENT_VERSION`, `APP_NAME`

3. **Update URL Format:**
   ```
   https://raw.githubusercontent.com/{owner}/{repo}/main/version.json
   ```

**Example:**

```python
# Auto-generated update_config.py
UPDATE_URL = "https://raw.githubusercontent.com/user/myapp/main/version.json"
CURRENT_VERSION = "1.0.0"
APP_NAME = "MyAwesomeApp"
```

### Include Additional Files

By default, MSI Builder includes:
- Main script and dependencies
- Python standard library
- Installed packages (from requirements.txt)

**To include data files:**

```python
# Create include_files.txt in project folder
resources/
data/
config.ini
README.md
```

MSI Builder will auto-detect and include these files.

### Custom Build Options

**Advanced users:** Edit `setup.py` before building

```python
# Customize setup.py
executables = [
    Executable(
        script="main.py",
        base="Win32GUI",  # No console window
        icon="icon.ico",
        target_name="MyApp.exe",
        shortcut_name="My Awesome App",
        shortcut_dir="ProgramMenuFolder",
    )
]

build_options = {
    "packages": ["tkinter", "requests"],
    "excludes": ["test", "unittest"],
    "include_files": [
        ("resources", "resources"),
        ("config.ini", "config.ini"),
    ],
    "optimize": 2,
}
```

---

## Auto-Update Integration

### How It Works

1. **Build Time:**
   - MSI Builder generates `update_config.py`
   - Embeds auto-updater module in EXE
   - Configures update URL and version

2. **Runtime:**
   - Your app checks for updates on startup
   - Compares current version with server version
   - Shows update notification if available
   - Downloads and applies update automatically

### Setup Update Server

**Option 1: GitHub (Recommended)**

```powershell
# 1. Create version.json in repo root
{
  "version": "1.0.1",
  "download_url": "https://github.com/user/repo/releases/download/v1.0.1/MyApp.zip",
  "checksum": "sha256hash",
  "changelog": "Bug fixes and improvements",
  "release_date": "2024-01-15"
}

# 2. Commit and push
git add version.json
git commit -m "Update version to 1.0.1"
git push

# 3. Your app auto-detects:
# https://raw.githubusercontent.com/user/repo/main/version.json
```

**Option 2: Use Publish Tool**

```powershell
# Auto-publish updates with tool
uv run --no-project python tools/publish_update.py

# Follow prompts:
# - Version number
# - Files to include
# - Changelog
# - Auto-create GitHub Release
```

### Testing Auto-Update

```powershell
# 1. Build app with auto-update
# 2. Run built EXE
# 3. Check console output:

[Auto-Update] Checking for updates...
[Auto-Update] Current version: 1.0.0
[Auto-Update] Latest version: 1.0.1
[Auto-Update] Update available!

# 4. Click "Update Now" in GUI
# 5. App downloads and applies update
# 6. Restart to use new version
```

---

## Compression with UPX

### What is UPX?

- **UPX** = Ultimate Packer for eXecutables
- **Compression**: Reduces EXE size by 50-70%
- **Runtime**: Decompresses in memory (no disk space needed)
- **Performance**: Minimal impact (<5% slower startup)

### Installation

**Method 1: Manual**

```powershell
# 1. Download UPX from https://upx.github.io/
# 2. Extract to C:\upx\
# 3. Add to PATH:
$env:PATH += ";C:\upx"

# 4. Verify installation
upx --version
```

**Method 2: Chocolatey**

```powershell
choco install upx
```

**Method 3: Scoop**

```powershell
scoop install upx
```

### Usage in MSI Builder

✅ **Check "Compress with UPX"** in GUI

**What happens:**
- Build process runs normally
- After EXE is created, UPX compresses it
- Progress shown: `Compressing with UPX...`
- Output: Compressed EXE (50-70% smaller)

**Example:**

```
Before UPX:  MyApp.exe  (15 MB)
After UPX:   MyApp.exe  (5 MB)  ← 67% reduction!
```

### Performance Impact

- **Startup Time**: +0.1-0.5 seconds (first run)
- **Runtime**: No difference
- **Memory**: Same as uncompressed
- **Antivirus**: May flag compressed EXEs (false positive)

**Tips:**
- Test compressed EXE on target systems
- If antivirus flags, submit as false positive
- For sensitive apps, disable compression

---

## Multi-Project Management

### Save Configuration

After setting up a project:

1. Click **"Save Config"**
2. Enter config name (e.g., "MyApp_Production")
3. Config saved to `configs/MyApp_Production.json`

**Saved Settings:**
- Project folder
- Main script
- App name, version, company
- Icon path
- Auto-update settings
- Compression settings

### Load Configuration

To build another project:

1. Click **"Load Config"**
2. Select config file (e.g., `MyApp_Production.json`)
3. All settings restored
4. Click **"Build EXE"**

### Recent Projects

MSI Builder remembers recent projects:
- Last 5 projects shown in dropdown
- Quick access without loading config

---

## Troubleshooting

### Problem: "Main script not found"

**Cause:** No main Python script detected

**Solutions:**
- Ensure file is named `main.py`, `app.py`, or `gui_app.py`
- Manually select script with "Browse" button
- Check file has `.py` extension

### Problem: "Build failed: Module not found"

**Cause:** Missing dependencies

**Solutions:**

```powershell
# Install dependencies in project
cd your_project
pip install -r requirements.txt

# Or install globally
pip install missing_module_name
```

### Problem: "UPX not found"

**Cause:** UPX not installed or not in PATH

**Solutions:**
- Install UPX (see [Compression](#compression-with-upx))
- Add UPX to system PATH
- Or uncheck "Compress with UPX"

### Problem: "Auto-detect failed"

**Cause:** Project is not a Git repository

**Solutions:**
- Initialize Git: `git init`
- Add remote: `git remote add origin https://github.com/user/repo.git`
- Or uncheck "Auto-Detect" and enter URL manually

### Problem: "MSI build fails"

**Cause:** cx_Freeze MSI issues

**Solutions:**

```powershell
# Build EXE first, then MSI manually
python setup.py build
python setup.py bdist_msi

# Or use EXE instead (simpler)
# Change Build Type to EXE
```

### Problem: "Built app crashes on startup"

**Cause:** Missing files or dependencies

**Solutions:**
- Check `build.log` in project folder
- Add missing files to `include_files.txt`
- Ensure all dependencies in `requirements.txt`
- Test in virtual environment first

### Problem: "Icon not showing"

**Cause:** ICO file invalid or path incorrect

**Solutions:**
- Verify ICO file opens in image viewer
- Use absolute path to ICO
- Regenerate ICO with Image Converter
- Leave blank to use default icon

---

## FAQ

### Q: How long does building take?

**A:**
- **EXE**: 30-60 seconds (typical)
- **MSI**: 2-5 minutes (includes EXE build + MSI packaging)
- **With UPX**: +10-30 seconds for compression

### Q: Can I distribute the EXE?

**A:** Yes! EXE is standalone:
- No Python installation needed
- All dependencies included
- Share via email, USB, download link

### Q: What about antivirus warnings?

**A:** Common with packaged Python apps:
- **False positive**: Not actually malware
- **UPX compression**: May trigger heuristics
- **Solutions:**
  - Submit to antivirus vendors as false positive
  - Code-sign your EXE (requires certificate)
  - Build without UPX compression

### Q: How to update built app?

**A:** Two methods:

**1. With Auto-Update:**
- Update `version.json` on server
- Users get update notification
- Click "Update Now" to apply

**2. Manual:**
- Build new EXE with new version
- Distribute new EXE to users
- Users replace old EXE

### Q: Can I build for Mac/Linux?

**A:** This tool is Windows-focused:
- **EXE**: Windows only
- **MSI**: Windows only
- **For Mac**: Use `py2app`
- **For Linux**: Use `PyInstaller`

### Q: How to reduce EXE size?

**A:** Several strategies:
1. ✅ Enable UPX compression (50-70% reduction)
2. Exclude unnecessary packages
3. Use `--optimize 2` flag
4. Remove unused files
5. Use virtual environment (fewer packages)

### Q: Where are build files?

**A:**
```
your_project/
├── build/          # Temp files (auto-deleted)
├── dist/           # Output EXE/MSI
├── setup.py        # Build script
└── update_config.py # Auto-update config
```

### Q: Can I customize setup.py?

**A:** Yes!
1. Let MSI Builder generate `setup.py`
2. Edit `setup.py` manually
3. Run build from command line:
   ```powershell
   python setup.py build
   python setup.py bdist_msi
   ```

### Q: How to include data files?

**A:** Create `include_files.txt`:

```
# include_files.txt
resources/
images/logo.png
config.ini
README.txt
```

MSI Builder auto-includes these files.

---

## Examples

### Example 1: Simple GUI App

```powershell
# Project structure:
my_app/
├── main.py         # Your GUI app
├── requirements.txt
└── icon.ico

# Build steps:
1. Open MSI Builder
2. Browse to my_app/
3. Fill: App Name = "MyApp", Version = "1.0.0"
4. Select icon.ico
5. Build Type = EXE
6. Click "Build EXE"

# Result: dist/MyApp.exe (ready to share!)
```

### Example 2: App with Auto-Update

```powershell
# Project structure (Git repo):
my_app/
├── .git/           # Git repository
├── main.py
├── requirements.txt
└── icon.ico

# Build steps:
1. Open MSI Builder
2. Browse to my_app/ (Git repo detected!)
3. ✅ Enable Auto-Update
4. ✅ Auto-Detect Update URL (auto-filled)
5. Click "Build EXE"

# Result:
# - dist/MyApp.exe (with auto-updater)
# - update_config.py (generated)

# Next: Publish updates with tools/publish_update.py
```

### Example 3: Professional MSI Installer

```powershell
# Build steps:
1. Open MSI Builder
2. Configure:
   - App Name: "Professional App"
   - Version: "1.0.0"
   - Company: "MyCompany Inc."
   - Icon: company_logo.ico
3. Build Type = MSI
4. ✅ Compress with UPX
5. Click "Build MSI"

# Result:
# - dist/ProfessionalApp-1.0.0-win64.msi
# - Installs to Program Files
# - Start Menu shortcut
# - Add/Remove Programs entry
```

---

## Best Practices

### Development Workflow

```
1. Develop & Test
   ↓
2. Update version number
   ↓
3. Build EXE (test build)
   ↓
4. Test built EXE
   ↓
5. Build MSI (production)
   ↓
6. Distribute / Publish Update
```

### Version Numbering

Use **Semantic Versioning**:
- `1.0.0` = Major.Minor.Patch
- `1.0.1` = Bug fix
- `1.1.0` = New features
- `2.0.0` = Breaking changes

### Icon Guidelines

- **Size**: 256x256 or larger source
- **Format**: .ico with multiple sizes (16, 32, 48, 256)
- **Design**: Simple, recognizable at small sizes
- **Tool**: Use Image Converter to create ICO

### Testing

Before distribution:
1. ✅ Test EXE on clean system (no Python)
2. ✅ Test all features work
3. ✅ Test auto-update (if enabled)
4. ✅ Scan with antivirus
5. ✅ Test MSI install/uninstall

---

## Next Steps

After mastering MSI Builder:

1. **🔄 [Auto-Update Guide](../AUTO_UPDATE_GUIDE.md)** - Deep dive into updates
2. **🤖 [Auto-Setup Guide](../AUTO_SETUP_GUIDE.md)** - Advanced automation
3. **📚 [Developer Guide](../developer-guide/)** - For customization
4. **🛠️ [Examples](../../examples/)** - Code samples

---

## Performance Tips

- **Faster builds**: Use virtual environment (fewer packages)
- **Smaller EXE**: Enable UPX compression
- **Faster startup**: Disable UPX if slow
- **Parallel builds**: Use separate project folders

---

**💡 Pro Tip:** Save configs for each project! Switch projects instantly with "Load Config".

**❓ Need Help?** Check [FAQ](../FAQ.md) or open an [issue](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)

---

<div align="center">

**[⬅️ Back: Image Converter](image-converter.md)** • **[➡️ Next: Developer Guide](../developer-guide/)**

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

</div>
