# 📦 Distribution Guide | Hướng dẫn Phân phối

> **Complete guide for building and distributing your application to end-users**

This guide covers how to build standalone EXE/MSI installers for distribution to end-users who don't have Python installed.

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Build](#quick-build)
- [Build Options](#build-options)
- [Distribution Formats](#distribution-formats)
- [Testing Before Release](#testing-before-release)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

This project uses **cx_Freeze** to convert Python applications into standalone executables that work on Windows without requiring Python installation.

### What You Can Build:

1. **EXE (Executable)** - Single application folder with all dependencies
2. **MSI (Installer)** - Professional Windows installer package
3. **Portable ZIP** - Compressed EXE folder for USB/portable use

### Requirements:

- Python 3.8+
- cx_Freeze >= 6.15.0 (auto-installed via `uv sync`)
- Windows 10/11 (for building Windows installers)

---

## ⚡ Quick Build

### Option 1: Using MSI Builder GUI (Recommended)

```powershell
# Launch the GUI builder
uv run python src/build_msi_gui.py
```

**Steps:**
1. **Auto-detect** - App automatically detects:
   - Main Python script (e.g., `src/gui_app.py`)
   - Project version from git/pyproject.toml
   - GitHub repository URL
   - Icon file (if exists)

2. **Review & Customize** - Verify/edit:
   - Application name
   - Version number
   - Author name
   - Icon path

3. **Build** - Click one of:
   - **"Build EXE"** - Creates standalone executable folder
   - **"Build MSI"** - Creates MSI installer package
   - **"Build Both"** - Creates both EXE and MSI

4. **Wait** - Build process takes 1-3 minutes

5. **Done!** - Output files are in `dist/` folder

### Option 2: Using Command Line

```powershell
# Build EXE only
uv run python cx_freeze_setup.py build

# Build MSI only
uv run python cx_freeze_setup.py bdist_msi

# Clean and rebuild
Remove-Item -Path "build" -Recurse -Force -ErrorAction SilentlyContinue
uv run python cx_freeze_setup.py build
```

---

## 🔧 Build Options

### Customizing Build Configuration

Edit `cx_freeze_setup.py` to customize:

```python
# Application metadata
name="Your App Name",
version="1.0.0",
description="Your app description",
author="Your Name",

# Build options
build_exe_options = {
    "packages": ["tkinter", "PIL", "your_package"],
    "include_files": [
        ("assets/", "assets/"),  # Include asset folder
        ("config.json", "config.json"),  # Include config
    ],
    "excludes": ["unittest", "email", "http"],  # Exclude unused modules
    "optimize": 2,  # Optimization level (0-2)
}

# MSI options
bdist_msi_options = {
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\YourApp",
    "install_icon": "assets/icon.ico",
}
```

### Using MSI Builder GUI to Generate Setup

The GUI builder (`src/build_msi_gui.py`) auto-generates `cx_freeze_setup.py` with:

- **Auto-detected packages** - Scans imports in your code
- **Smart includes** - Includes necessary files (icons, configs)
- **Optimized excludes** - Excludes unused standard library modules
- **Best practices** - Pre-configured for minimal size and fast startup

---

## 📦 Distribution Formats

### 1. EXE Folder (Standalone)

**Location:** `build/exe.win-amd64-3.11/`

**Structure:**
```
exe.win-amd64-3.11/
├── App Change Image To .Ico File.exe    # Main executable
├── python311.dll                         # Python runtime
├── lib/                                  # Python libraries (frozen)
│   ├── library.zip                       # Compiled .pyc files
│   └── ...
├── share/                                # Tcl/Tk files (if using tkinter)
│   ├── tcl8.6/
│   └── tk8.6/
└── *.dll                                 # Runtime dependencies
```

**Usage:**
- Can be run directly from this folder
- Must keep all files together
- Can be zipped for distribution

**Pros:**
- ✅ No installation needed
- ✅ Portable (USB drive, network share)
- ✅ Easy to update (just replace files)

**Cons:**
- ❌ Many files to manage
- ❌ No Start Menu integration
- ❌ No uninstaller

### 2. MSI Installer

**Location:** `dist/image-to-ico-converter-1.0.0-win64.msi`

**Features:**
- Professional Windows Installer wizard
- Installs to `C:\Program Files\YourApp\`
- Creates Start Menu shortcuts
- Adds to Windows "Programs and Features"
- Includes uninstaller

**Installation Process:**
1. Double-click MSI file
2. Follow installation wizard
3. Choose install location (default: Program Files)
4. Click "Install"
5. Launch from Start Menu

**Pros:**
- ✅ Professional appearance
- ✅ Easy installation for users
- ✅ Start Menu integration
- ✅ Clean uninstallation
- ✅ Windows UAC prompts (trusted)

**Cons:**
- ❌ Requires admin rights
- ❌ Larger file size (~20 MB)
- ❌ Installation required (not portable)

### 3. Portable ZIP

**Location:** `dist/App-Change-Image-to-Ico-Portable.zip`

**Contents:**
- Complete EXE folder (compressed)
- All dependencies included
- Ready to extract and run

**Usage:**
1. Extract ZIP anywhere
2. Run `App Change Image To .Ico File.exe`
3. No installation, no registry changes

**Pros:**
- ✅ Single file to download
- ✅ No installation needed
- ✅ Portable across systems
- ✅ Easy to share

**Cons:**
- ❌ Larger download (~20 MB compressed)
- ❌ Must extract before use
- ❌ No Start Menu integration

---

## 📊 Comparison Table

| Feature | EXE Folder | MSI Installer | Portable ZIP |
|---------|-----------|--------------|--------------|
| **File Size** | ~50 MB | ~20 MB | ~20 MB |
| **Installation** | None | Required | None |
| **Portability** | ✅ Yes | ❌ No | ✅ Yes |
| **Start Menu** | ❌ No | ✅ Yes | ❌ No |
| **Admin Rights** | ❌ No | ✅ Yes | ❌ No |
| **Uninstaller** | ❌ No | ✅ Yes | ❌ No |
| **Professional** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Distribution** | Email/Share | Download | Download |

### Recommendation:

- **For internal/personal use** → EXE Folder or Portable ZIP
- **For public release** → MSI Installer
- **For enterprise** → MSI Installer (easier IT deployment)
- **For casual users** → Portable ZIP (easiest)

---

## ✅ Testing Before Release

### 1. Test on Clean System

**Why:** Ensure app works without Python/dependencies installed

**How:**
```powershell
# Option A: Use Windows Sandbox
# 1. Enable Windows Sandbox (Windows Features)
# 2. Copy EXE/MSI to Sandbox
# 3. Test installation and running

# Option B: Use Virtual Machine
# 1. Create clean Windows VM
# 2. Install from MSI
# 3. Test all features
```

### 2. Verify File Sizes

```powershell
# Check build output sizes
Get-ChildItem -Path "dist" | Select-Object Name, @{Name="Size (MB)";Expression={[math]::Round($_.Length/1MB, 2)}}

# Expected sizes:
# MSI: ~15-25 MB (depending on dependencies)
# ZIP: ~15-25 MB (compressed EXE folder)
```

### 3. Test All Features

**Checklist:**
- [ ] Application launches without errors
- [ ] GUI displays correctly
- [ ] Image conversion works (all formats)
- [ ] File dialogs work (open/save)
- [ ] Zoom controls work (if applicable)
- [ ] Auto-update checks (if enabled)
- [ ] Error messages display properly
- [ ] Application closes cleanly

### 4. Test Installation (MSI)

```powershell
# Install MSI
msiexec /i dist\your-app-1.0.0-win64.msi

# Check installation
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | 
    Where-Object {$_.DisplayName -like "*Your App*"}

# Test uninstall
# Control Panel → Programs → Uninstall
```

### 5. Check for Missing DLLs

```powershell
# Run from build directory
cd build\exe.win-amd64-3.11
& ".\App Change Image To .Ico File.exe"

# If you see "DLL not found" errors:
# 1. Check cx_freeze_setup.py includes
# 2. Add missing DLLs to bin_includes
# 3. Rebuild
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "python311.dll was not found"

**Cause:** Python runtime DLL not included in build

**Solution:**
```python
# In cx_freeze_setup.py, ensure:
build_exe_options = {
    "include_msvcr": True,  # Include Microsoft Visual C++ runtime
    "bin_includes": [],     # Add if needed: ["python311.dll"]
}
```

Then rebuild:
```powershell
Remove-Item -Path "build" -Recurse -Force
uv run python cx_freeze_setup.py build
```

#### 2. "Module not found" errors

**Cause:** Missing package in build configuration

**Solution:**
```python
# In cx_freeze_setup.py, add to packages:
build_exe_options = {
    "packages": [
        "tkinter",
        "PIL",
        "your_missing_module",  # Add here
    ],
}
```

#### 3. Large EXE size (>100 MB)

**Cause:** Too many packages included

**Solution:**
```python
# In cx_freeze_setup.py, add to excludes:
build_exe_options = {
    "excludes": [
        "unittest", "email", "http", "xml",
        "pydoc", "doctest", "distutils",
    ],
    "optimize": 2,  # Maximum optimization
}
```

#### 4. tkinter interface issues

**Cause:** Tcl/Tk files not found

**Solution:**
```python
# Ensure include_files has Tcl/Tk:
import os
import sys

# Auto-find Tcl/Tk
tcl_path = os.path.join(sys.prefix, "tcl")
tk_path = os.path.join(sys.prefix, "tk")

build_exe_options = {
    "include_files": [
        (tcl_path, "tcl"),
        (tk_path, "tk"),
    ],
}
```

#### 5. Icon not showing in EXE

**Cause:** Icon path incorrect in setup

**Solution:**
```python
# Verify icon path in cx_freeze_setup.py:
executables = [
    Executable(
        "src/gui_app.py",
        base="Win32GUI",
        target_name="App Change Image To .Ico File",
        icon="assets/icon.ico",  # Verify this path exists
    )
]
```

#### 6. MSI build fails

**Cause:** Missing MSI build tools on Windows

**Solution:**
```powershell
# Install Windows SDK (includes MSI tools)
# Download from: https://developer.microsoft.com/windows/downloads/windows-sdk/

# Or use chocolatey:
choco install windows-sdk-10.1
```

#### 7. Auto-update not working in frozen app

**Cause:** Update URLs hardcoded for development

**Solution:**
```python
# In auto_updater.py, detect frozen state:
import sys

if getattr(sys, 'frozen', False):
    # Running as frozen EXE
    update_url = "https://raw.githubusercontent.com/user/repo/main/version.json"
else:
    # Running as script
    update_url = "http://localhost/version.json"
```

---

## 📝 Best Practices

### 1. Version Numbering

Use semantic versioning: `MAJOR.MINOR.PATCH`

```python
# Example progression:
"1.0.0"  # Initial release
"1.0.1"  # Bug fix
"1.1.0"  # New feature
"2.0.0"  # Breaking change
```

### 2. File Naming

```powershell
# Good naming conventions:
app-name-1.0.0-win64.msi           # MSI installer
app-name-1.0.0-win64-portable.zip  # Portable version
app-name-1.0.0-macos.dmg           # macOS version
```

### 3. Changelog

Create `CHANGELOG.md` for each release:

```markdown
# Changelog

## [1.0.0] - 2025-11-11

### Added
- Initial release
- Image to ICO conversion
- Multi-format support

### Fixed
- None

### Changed
- None
```

### 4. Testing Matrix

Test on multiple systems:

| OS Version | Python | Status |
|-----------|--------|--------|
| Windows 11 | N/A | ✅ |
| Windows 10 | N/A | ✅ |
| Windows Server 2019 | N/A | ⏳ |

### 5. Size Optimization

```python
# Minimize EXE size:
build_exe_options = {
    "optimize": 2,
    "excludes": ["unittest", "email", "http", "xml"],
    "zip_include_packages": ["*"],
    "zip_exclude_packages": [],
}
```

**Results:**
- Before optimization: ~80 MB
- After optimization: ~20 MB

---

## 🚀 Release Workflow

### Complete Release Process

1. **Prepare Code**
   ```powershell
   # Update version
   # Update CHANGELOG.md
   # Commit changes
   git add .
   git commit -m "Release v1.0.0"
   git tag v1.0.0
   git push origin main --tags
   ```

2. **Build Installers**
   ```powershell
   # Clean previous builds
   Remove-Item -Path "build", "dist" -Recurse -Force -ErrorAction SilentlyContinue
   
   # Build MSI
   uv run python src/build_msi_gui.py
   # Or: uv run python cx_freeze_setup.py bdist_msi
   
   # Create portable ZIP
   Compress-Archive -Path "build\exe.win-amd64-3.11\*" -DestinationPath "dist\App-Portable-v1.0.0.zip" -Force
   ```

3. **Test Builds**
   ```powershell
   # Test EXE
   & "build\exe.win-amd64-3.11\App Change Image To .Ico File.exe"
   
   # Test MSI (on clean system)
   msiexec /i dist\your-app-1.0.0-win64.msi /l*v install.log
   ```

4. **Create GitHub Release**
   ```powershell
   # Go to GitHub → Releases → New Release
   # - Tag: v1.0.0
   # - Title: Version 1.0.0
   # - Description: Release notes from CHANGELOG.md
   # - Attach files:
   #   - your-app-1.0.0-win64.msi
   #   - App-Portable-v1.0.0.zip
   # - Publish release
   ```

5. **Update Auto-Update Config**
   ```json
   // version.json
   {
     "version": "1.0.0",
     "download_url": "https://github.com/user/repo/releases/download/v1.0.0/your-app-1.0.0-win64.msi",
     "checksum": "sha256hash",
     "changelog": "- Initial release\n- Feature 1\n- Feature 2"
   }
   ```

6. **Announce Release**
   - Update README.md
   - Post on social media
   - Notify users via email/Discord

---

## 📚 Additional Resources

- **cx_Freeze Documentation:** https://cx-freeze.readthedocs.io/
- **MSI Installer Guide:** https://learn.microsoft.com/en-us/windows/win32/msi/
- **Build Guide:** [BUILD_GUIDE.md](BUILD_GUIDE.md)
- **Auto-Update Guide:** [AUTO_UPDATE_GUIDE.md](AUTO_UPDATE_GUIDE.md)

---

## 💡 Tips & Tricks

### Reduce Build Time

```powershell
# Use incremental builds (don't clean)
uv run python cx_freeze_setup.py build

# Only clean when necessary
# (after changing dependencies)
```

### Debug Build Issues

```powershell
# Run with verbose output
uv run python cx_freeze_setup.py build --verbose

# Check build log
cat build.log
```

### Automate Builds

Create `build.bat`:

```batch
@echo off
echo Building application...
uv run python cx_freeze_setup.py clean
uv run python cx_freeze_setup.py build
uv run python cx_freeze_setup.py bdist_msi
echo Done! Check dist/ folder
pause
```

---

## ❓ FAQ

**Q: Can I build for macOS/Linux on Windows?**  
A: No, you need to build on the target platform. Use CI/CD (GitHub Actions) for multi-platform builds.

**Q: How do I sign my EXE/MSI?**  
A: Use `signtool.exe` from Windows SDK:
```powershell
signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com dist\your-app.msi
```

**Q: Can I reduce the 20 MB size?**  
A: Yes, by excluding unused modules and using UPX compression (advanced).

**Q: Is the built EXE truly standalone?**  
A: Yes, it includes Python runtime and all dependencies. No Python installation needed on target system.

---

<div align="center">

**📦 Happy Building! 📦**

Need help? Check [FAQ](../FAQ.md) or open an [issue](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues).

</div>
