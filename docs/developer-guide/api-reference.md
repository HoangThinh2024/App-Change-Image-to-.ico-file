# 📖 API Reference

> **Complete API documentation for developers**

## Overview

This document provides API reference for all modules in the toolkit. For high-level architecture, see [Architecture Guide](architecture.md).

---

## 📦 convert_to_ico Module

### `convert_to_ico(input_path, output_path, sizes=None)`

Convert an image file to ICO format with multiple resolutions.

**Parameters:**
- `input_path` (str): Path to input image (PNG, JPG, BMP, GIF, TIFF, WEBP)
- `output_path` (str): Path for output ICO file
- `sizes` (list[int], optional): Icon sizes in pixels. Default: `[16, 32, 48, 256]`

**Returns:** None

**Raises:**
- `FileNotFoundError`: Input file doesn't exist
- `IOError`: Cannot read input or write output
- `ValueError`: Invalid image format

**Example:**

```python
from convert_to_ico import convert_to_ico

# Basic usage
convert_to_ico("logo.png", "favicon.ico")

# Custom sizes
convert_to_ico("logo.png", "custom.ico", sizes=[16, 32, 64, 128])

# Single size
convert_to_ico("logo.png", "small.ico", sizes=[16])
```

---

## 🎨 gui_app Module

### `class ImageConverterGUI(tk.Tk)`

Main GUI window for Image Converter.

#### Methods:

##### `__init__()`
Initialize the GUI window with all components.

##### `select_image()`
Open file dialog to select input image.

**Supported formats:** PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP

##### `convert_to_ico_action()`
Convert selected image to ICO format.

Opens save dialog for output path.

##### `zoom_in()`
Zoom in the image preview by 20%.

##### `zoom_out()`
Zoom out the image preview by 20%.

##### `fit_to_window()`
Fit image to window size (auto-scale).

##### `reset_zoom()`
Reset zoom to 100%.

**Example:**

```python
from gui_app import ImageConverterGUI

app = ImageConverterGUI()
app.mainloop()
```

---

## 🏗️ build_msi_gui Module

### `class MSIBuilderGUI(tk.Tk)`

Main GUI window for MSI/EXE Builder.

#### Attributes:

- `project_folder` (str): Selected project directory path
- `main_script` (str): Path to main Python script
- `app_name` (str): Application name
- `version` (str): Version number (e.g., "1.0.0")
- `company` (str): Company/developer name
- `icon_path` (str): Path to ICO file
- `enable_auto_update` (bool): Whether to enable auto-update
- `auto_detect_update` (bool): Whether to auto-detect update URL
- `update_url` (str): Update server URL
- `compress_upx` (bool): Whether to compress with UPX
- `build_type` (str): "EXE" or "MSI"

#### Methods:

##### `select_project_folder()`
Open dialog to select project folder. Triggers auto-detection.

##### `detect_main_script()`
Auto-detect main Python script in project folder.

**Detection order:** `main.py`, `app.py`, `gui_app.py`, `__main__.py`

**Returns:** str - Path to detected main script, or None

##### `auto_detect_git_info()`
Auto-detect GitHub repository and generate update URL.

Uses `auto_update_helper` module.

**Returns:** dict - Contains `owner`, `repo`, `update_url`, or None

##### `detect_version()`
Auto-detect version from git tags, pyproject.toml, or __init__.py.

**Returns:** str - Detected version or "1.0.0"

##### `generate_setup_py()`
Generate cx_Freeze setup.py file for building.

**Returns:** str - Path to generated setup.py

##### `run_build()`
Execute the build process (EXE or MSI).

**Returns:** bool - True if successful, False otherwise

##### `compress_with_upx(exe_path)`
Compress EXE file with UPX.

**Parameters:**
- `exe_path` (str): Path to EXE file to compress

**Returns:** bool - True if successful, False otherwise

##### `save_config()`
Save current configuration to JSON file.

##### `load_config()`
Load configuration from JSON file.

**Example:**

```python
from build_msi_gui import MSIBuilderGUI

app = MSIBuilderGUI()
app.mainloop()
```

---

## 🔄 auto_updater Module

### `class AutoUpdater`

Core auto-update functionality.

#### Constructor:

```python
AutoUpdater(current_version, update_url, app_name="MyApp")
```

**Parameters:**
- `current_version` (str): Current app version (e.g., "1.0.0")
- `update_url` (str): URL to version.json file
- `app_name` (str): Application name for display

#### Methods:

##### `check_for_updates()`
Check if a new version is available.

**Returns:** dict or None
```python
{
    "version": "1.0.1",
    "download_url": "https://...",
    "checksum": "sha256hash",
    "changelog": "Bug fixes...",
    "release_date": "2024-01-15"
}
```

##### `download_update(download_url, progress_callback=None)`
Download update ZIP file.

**Parameters:**
- `download_url` (str): URL to download ZIP
- `progress_callback` (callable): Function to call with progress `(downloaded, total)`

**Returns:** str - Path to downloaded file

##### `verify_checksum(file_path, expected_checksum)`
Verify file integrity with SHA256.

**Parameters:**
- `file_path` (str): Path to downloaded file
- `expected_checksum` (str): Expected SHA256 hash

**Returns:** bool - True if valid, False otherwise

##### `apply_update(zip_path)`
Extract and apply update.

Creates backup before applying. Auto-rollback on failure.

**Returns:** bool - True if successful, False otherwise

##### `rollback()`
Restore from backup if update failed.

**Returns:** bool - True if successful, False otherwise

**Example:**

```python
from auto_updater import AutoUpdater

updater = AutoUpdater(
    current_version="1.0.0",
    update_url="https://raw.githubusercontent.com/user/repo/main/version.json",
    app_name="MyApp"
)

# Check for updates
update_info = updater.check_for_updates()
if update_info:
    print(f"New version available: {update_info['version']}")
    
    # Download
    zip_path = updater.download_update(
        update_info['download_url'],
        progress_callback=lambda d, t: print(f"{d}/{t} bytes")
    )
    
    # Verify
    if updater.verify_checksum(zip_path, update_info['checksum']):
        # Apply
        if updater.apply_update(zip_path):
            print("Update successful!")
        else:
            print("Update failed, rolled back")
```

### `check_and_prompt_update(root, current_version, update_url, app_name)`

Convenient one-line integration function.

**Parameters:**
- `root` (tk.Tk): Tkinter root window
- `current_version` (str): Current version
- `update_url` (str): URL to version.json
- `app_name` (str): Application name

**Example:**

```python
import tkinter as tk
from auto_updater import check_and_prompt_update

root = tk.Tk()

# Check for updates on startup
check_and_prompt_update(
    root,
    current_version="1.0.0",
    update_url="https://raw.githubusercontent.com/user/repo/main/version.json",
    app_name="MyApp"
)

root.mainloop()
```

---

## 🤖 auto_update_helper Module

### `find_git_repo(start_path)`

Find Git repository root from given path.

**Parameters:**
- `start_path` (str): Directory to start searching from

**Returns:** str or None - Path to .git directory

### `get_git_remote_url(git_dir)`

Read Git remote URL from .git/config.

**Parameters:**
- `git_dir` (str): Path to .git directory

**Returns:** str or None - Git remote URL (SSH or HTTPS)

### `parse_github_url(url)`

Parse GitHub URL into owner and repo.

**Parameters:**
- `url` (str): Git remote URL (SSH or HTTPS format)

**Returns:** tuple or None - `(owner, repo)` or None

**Supported formats:**
- SSH: `git@github.com:user/repo.git`
- HTTPS: `https://github.com/user/repo.git`

### `detect_project_info(project_path)`

Auto-detect Git repository info from project path.

**Parameters:**
- `project_path` (str): Path to project folder

**Returns:** dict or None
```python
{
    "owner": "user",
    "repo": "myproject",
    "update_url": "https://raw.githubusercontent.com/user/myproject/main/version.json"
}
```

### `auto_detect_version(project_path)`

Auto-detect version from multiple sources.

**Detection order:**
1. Git tags (`git describe --tags`)
2. pyproject.toml (`version = "1.0.0"`)
3. __init__.py (`__version__ = "1.0.0"`)

**Parameters:**
- `project_path` (str): Path to project folder

**Returns:** str or None - Detected version

### `create_update_config(project_path, owner, repo, version, app_name)`

Generate update_config.py file.

**Parameters:**
- `project_path` (str): Path to project folder
- `owner` (str): GitHub owner
- `repo` (str): GitHub repository name
- `version` (str): Current version
- `app_name` (str): Application name

**Returns:** str - Path to generated update_config.py

**Example:**

```python
from auto_update_helper import detect_project_info, auto_detect_version, create_update_config

# Auto-detect everything
project_path = "C:/my_project"

# Get Git info
info = detect_project_info(project_path)
if info:
    print(f"Detected: {info['owner']}/{info['repo']}")
    print(f"Update URL: {info['update_url']}")
    
    # Get version
    version = auto_detect_version(project_path)
    print(f"Version: {version}")
    
    # Generate config
    config_path = create_update_config(
        project_path,
        info['owner'],
        info['repo'],
        version,
        "MyApp"
    )
    print(f"Config created: {config_path}")
```

---

## 🛠️ publish_update Module (tools/)

### `create_update_package(files, output_path, version)`

Create update ZIP package from files.

**Parameters:**
- `files` (list[str]): List of file paths to include
- `output_path` (str): Path for output ZIP
- `version` (str): Version number for naming

**Returns:** str - Path to created ZIP file

### `calculate_checksum(file_path)`

Calculate SHA256 checksum of file.

**Parameters:**
- `file_path` (str): Path to file

**Returns:** str - Hex-encoded SHA256 hash

### `generate_version_json(version, download_url, checksum, changelog, release_date)`

Create version.json file.

**Parameters:**
- `version` (str): Version number (e.g., "1.0.1")
- `download_url` (str): URL to download ZIP
- `checksum` (str): SHA256 hash of ZIP
- `changelog` (str): Release notes
- `release_date` (str): Release date (YYYY-MM-DD)

**Returns:** dict - version.json content

### `create_github_release(owner, repo, version, zip_path, version_json_path, changelog)`

Create GitHub Release and upload assets.

**Parameters:**
- `owner` (str): GitHub owner
- `repo` (str): Repository name
- `version` (str): Version tag (e.g., "v1.0.1")
- `zip_path` (str): Path to update ZIP
- `version_json_path` (str): Path to version.json
- `changelog` (str): Release notes

**Returns:** bool - True if successful

**Requires:** `gh` CLI installed and authenticated

**Example:**

```python
from publish_update import (
    create_update_package,
    calculate_checksum,
    generate_version_json,
    create_github_release
)

# Create update package
files = ["myapp.exe", "README.txt"]
zip_path = create_update_package(files, "update.zip", "1.0.1")

# Calculate checksum
checksum = calculate_checksum(zip_path)

# Generate version.json
version_info = generate_version_json(
    version="1.0.1",
    download_url="https://github.com/user/repo/releases/download/v1.0.1/update.zip",
    checksum=checksum,
    changelog="Bug fixes and improvements",
    release_date="2024-01-15"
)

# Write version.json
import json
with open("version.json", "w") as f:
    json.dump(version_info, f, indent=2)

# Create GitHub Release
create_github_release(
    owner="user",
    repo="myrepo",
    version="v1.0.1",
    zip_path=zip_path,
    version_json_path="version.json",
    changelog="Bug fixes and improvements"
)
```

---

## 📊 Data Structures

### version.json Format

```json
{
  "version": "1.0.1",
  "download_url": "https://github.com/user/repo/releases/download/v1.0.1/MyApp.zip",
  "checksum": "sha256_hash_here",
  "changelog": "Bug fixes and new features",
  "release_date": "2024-01-15",
  "min_version": "1.0.0",
  "critical": false
}
```

**Fields:**
- `version` (required): New version number
- `download_url` (required): URL to download update ZIP
- `checksum` (required): SHA256 hash for verification
- `changelog` (optional): Release notes
- `release_date` (optional): Release date (YYYY-MM-DD)
- `min_version` (optional): Minimum version that can update
- `critical` (optional): Force update if true

### update_config.py Format

```python
# Auto-generated by auto_update_helper

UPDATE_URL = "https://raw.githubusercontent.com/user/repo/main/version.json"
CURRENT_VERSION = "1.0.0"
APP_NAME = "MyApp"
```

### Build Config JSON Format

```json
{
  "project_folder": "C:/my_project",
  "main_script": "main.py",
  "app_name": "MyApp",
  "version": "1.0.0",
  "company": "MyCompany",
  "icon_path": "icon.ico",
  "enable_auto_update": true,
  "auto_detect_update": true,
  "update_url": "https://...",
  "compress_upx": true,
  "build_type": "EXE"
}
```

---

## 🔧 Error Handling

### Common Exceptions

```python
# Image conversion errors
try:
    convert_to_ico("input.png", "output.ico")
except FileNotFoundError:
    print("Input file not found")
except IOError as e:
    print(f"I/O error: {e}")
except ValueError as e:
    print(f"Invalid image: {e}")

# Auto-update errors
try:
    updater = AutoUpdater("1.0.0", "https://...", "MyApp")
    update_info = updater.check_for_updates()
except requests.RequestException as e:
    print(f"Network error: {e}")
except json.JSONDecodeError:
    print("Invalid version.json format")
except Exception as e:
    print(f"Update failed: {e}")

# Build errors
try:
    builder.run_build()
except subprocess.CalledProcessError as e:
    print(f"Build failed: {e}")
except FileNotFoundError:
    print("cx_Freeze or UPX not found")
```

---

## 🧪 Testing

### Unit Test Examples

```python
import unittest
from convert_to_ico import convert_to_ico

class TestConverter(unittest.TestCase):
    def test_png_to_ico(self):
        convert_to_ico("test.png", "output.ico")
        self.assertTrue(os.path.exists("output.ico"))
    
    def test_custom_sizes(self):
        convert_to_ico("test.png", "custom.ico", sizes=[16, 32])
        # Verify ICO contains correct sizes

class TestAutoUpdater(unittest.TestCase):
    def test_version_check(self):
        updater = AutoUpdater("1.0.0", "http://localhost/version.json")
        update_info = updater.check_for_updates()
        self.assertIsNotNone(update_info)
    
    def test_checksum_verify(self):
        updater = AutoUpdater("1.0.0", "http://...")
        result = updater.verify_checksum("file.zip", "expected_hash")
        self.assertTrue(result)
```

---

## 📚 Next Steps

- **[Extending Guide](extending.md)** - Customize and extend functionality
- **[Contributing](contributing.md)** - Contribute to the project
- **[Architecture](architecture.md)** - High-level system design

---

<div align="center">

**[⬅️ Architecture](architecture.md)** • **[➡️ Extending](extending.md)**

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

</div>
