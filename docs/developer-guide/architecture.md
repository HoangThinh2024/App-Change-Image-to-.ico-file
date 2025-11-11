# 🏛️ System Architecture

> **Technical overview of the toolkit's architecture and design**

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture Diagram](#architecture-diagram)
3. [Component Design](#component-design)
4. [Module Structure](#module-structure)
5. [Data Flow](#data-flow)
6. [Design Patterns](#design-patterns)
7. [Dependencies](#dependencies)
8. [Performance Considerations](#performance-considerations)

---

## Overview

This toolkit follows a **modular architecture** with clear separation of concerns:

- **Presentation Layer**: GUI components (Tkinter-based)
- **Business Logic Layer**: Core conversion, building, and update logic
- **Integration Layer**: GitHub API, file system, external tools
- **Data Layer**: Configuration files, version data, metadata

### Design Principles

1. **Modularity**: Each component can be used independently
2. **Extensibility**: Easy to add new features without breaking existing code
3. **User-Friendly**: GUI abstracts complexity for end-users
4. **Developer-Friendly**: CLI and Python API for automation
5. **Cross-Platform**: Core logic works on Windows, macOS, Linux (GUI: Windows-focused)

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                     │
├─────────────────────┬─────────────────────┬─────────────────────┤
│   gui_app.py        │  build_msi_gui.py   │  CLI Scripts        │
│   (Image GUI)       │  (Builder GUI)      │  (Automation)       │
└─────────┬───────────┴──────────┬──────────┴──────────┬──────────┘
          │                      │                      │
┌─────────▼──────────────────────▼──────────────────────▼──────────┐
│                      BUSINESS LOGIC LAYER                         │
├────────────────┬───────────────────┬──────────────────────────────┤
│ convert_to_ico │  setup.py         │  auto_updater.py             │
│ (Converter)    │  (cx_Freeze)      │  (Update System)             │
└────────┬───────┴────────┬──────────┴───────────┬──────────────────┘
         │                │                       │
┌────────▼────────────────▼───────────────────────▼──────────────────┐
│                      INTEGRATION LAYER                              │
├────────────────┬──────────────────┬─────────────────────────────────┤
│ Pillow         │  cx_Freeze       │  auto_update_helper.py          │
│ (Image Proc)   │  (EXE Builder)   │  (Git Detection)                │
├────────────────┼──────────────────┼─────────────────────────────────┤
│ UPX            │  GitHub API      │  File System                    │
│ (Compression)  │  (Releases)      │  (Config, Logs)                 │
└────────────────┴──────────────────┴─────────────────────────────────┘
         │                │                       │
┌────────▼────────────────▼───────────────────────▼──────────────────┐
│                          DATA LAYER                                 │
├─────────────────────────────────────────────────────────────────────┤
│  • Images (PNG, JPG, ICO)                                           │
│  • Config Files (update_config.py, pyproject.toml)                  │
│  • Version Data (version.json)                                      │
│  • Build Artifacts (setup.py, build/, dist/)                        │
│  • Logs (build.log, update.log)                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Component Design

### 1. Image Converter (`gui_app.py` + `convert_to_ico.py`)

**Purpose**: Convert images to ICO format

**Architecture**:
```
gui_app.py (GUI)
    ├── ImageConverterGUI (tkinter.Tk)
    │   ├── UI Components (buttons, labels, canvas)
    │   ├── Event Handlers (select_image, convert_to_ico)
    │   └── Zoom Controls (zoom_in, zoom_out, fit_window)
    └── convert_to_ico.py (Core Logic)
        └── convert_to_ico(input, output, sizes)
            ├── Open image with Pillow
            ├── Resize to multiple sizes
            └── Save as ICO
```

**Key Classes**:
- `ImageConverterGUI`: Main GUI window
- No classes in `convert_to_ico.py` (functional approach)

**Patterns**:
- **MVC**: GUI (View) separates from logic (Model/Controller)
- **Event-Driven**: Tkinter event loop handles user interactions

### 2. MSI Builder (`build_msi_gui.py`)

**Purpose**: Build EXE/MSI installers with auto-update

**Architecture**:
```
build_msi_gui.py
    ├── MSIBuilderGUI (tkinter.Tk)
    │   ├── Configuration UI
    │   │   ├── Project folder selection
    │   │   ├── Auto-detect controls
    │   │   └── Build options
    │   ├── Auto-Detection Logic
    │   │   ├── detect_main_script()
    │   │   ├── auto_detect_git_info() → auto_update_helper
    │   │   └── detect_version()
    │   ├── Build Process
    │   │   ├── generate_setup_py()
    │   │   ├── run_build() → cx_Freeze
    │   │   └── compress_with_upx() → UPX
    │   └── Config Management
    │       ├── save_config()
    │       └── load_config()
    └── External Dependencies
        ├── cx_Freeze (EXE building)
        ├── UPX (compression)
        └── auto_update_helper (Git detection)
```

**Key Classes**:
- `MSIBuilderGUI`: Main builder window
- `SetupGenerator`: Generates cx_Freeze setup.py
- `BuildOrchestrator`: Coordinates build process

**Patterns**:
- **Builder Pattern**: Step-by-step EXE/MSI construction
- **Template Method**: Extensible build process
- **Strategy**: Different build strategies (EXE vs MSI)

### 3. Auto-Updater (`auto_updater.py`)

**Purpose**: Automatic update system for applications

**Architecture**:
```
auto_updater.py
    ├── AutoUpdater (Core Logic)
    │   ├── check_for_updates()
    │   │   ├── Fetch version.json
    │   │   └── Compare versions
    │   ├── download_update()
    │   │   ├── Download ZIP
    │   │   └── Show progress
    │   ├── verify_checksum()
    │   │   └── SHA256 validation
    │   ├── apply_update()
    │   │   ├── Backup current version
    │   │   ├── Extract new files
    │   │   └── Restart app
    │   └── rollback()
    │       └── Restore from backup
    ├── UpdaterGUI (User Interface)
    │   ├── Update notification
    │   ├── Progress bar
    │   └── Changelog display
    └── Helper Functions
        └── check_and_prompt_update()
            └── One-line integration for apps
```

**Key Classes**:
- `AutoUpdater`: Core update logic
- `UpdaterGUI`: User interface for updates
- `VersionInfo`: Data class for version metadata

**Patterns**:
- **State Machine**: Update states (checking, downloading, applying, complete)
- **Observer**: Progress callbacks for GUI updates
- **Command**: Rollback command for failure recovery

### 4. Auto-Setup Helper (`auto_update_helper.py`)

**Purpose**: Auto-detect Git repositories and generate configs

**Architecture**:
```
auto_update_helper.py
    ├── Git Detection
    │   ├── find_git_repo(directory)
    │   │   └── Search for .git/config
    │   ├── get_git_remote_url()
    │   │   └── Parse .git/config
    │   └── parse_github_url(url)
    │       ├── Handle SSH format (git@github.com:...)
    │       └── Handle HTTPS format (https://github.com/...)
    ├── Version Detection
    │   ├── detect_version_from_git()
    │   │   └── git describe --tags
    │   ├── detect_version_from_pyproject()
    │   │   └── Parse pyproject.toml
    │   └── detect_version_from_init()
    │       └── Parse __version__ in __init__.py
    ├── Config Generation
    │   ├── generate_update_url(owner, repo)
    │   │   └── Format GitHub raw URL
    │   └── create_update_config(project_path)
    │       └── Write update_config.py
    └── CLI Interface
        └── main()
            └── Interactive detection and config
```

**Key Functions**:
- `detect_project_info()`: One-stop detection
- `auto_detect_version()`: Multi-source version detection
- `create_update_config()`: Config file generation

**Patterns**:
- **Chain of Responsibility**: Try multiple version detection methods
- **Factory**: Generate appropriate config based on detection
- **Facade**: Simple interface hiding complex detection logic

### 5. Publish Tool (`tools/publish_update.py`)

**Purpose**: Automate update publishing to GitHub

**Architecture**:
```
publish_update.py
    ├── Package Creation
    │   ├── select_files()
    │   │   └── Interactive file selection
    │   ├── create_update_package()
    │   │   └── ZIP creation
    │   └── calculate_checksum()
    │       └── SHA256 hash
    ├── Version Management
    │   ├── generate_version_json()
    │   │   └── Create version.json
    │   └── validate_version()
    │       └── Semantic versioning check
    ├── GitHub Integration
    │   ├── create_github_release()
    │   │   └── Use `gh` CLI
    │   ├── upload_assets()
    │   │   └── Attach ZIP and version.json
    │   └── update_version_json_in_repo()
    │       └── Commit to main branch
    └── CLI Workflow
        └── main()
            ├── Gather info
            ├── Create package
            ├── Generate version.json
            └── Publish to GitHub
```

**Key Functions**:
- `create_update_package()`: Package builder
- `generate_version_json()`: Metadata creator
- `create_github_release()`: GitHub API wrapper

**Patterns**:
- **Workflow**: Sequential steps for publishing
- **Adapter**: Wraps `gh` CLI for GitHub operations
- **Template Method**: Extensible publishing process

---

## Module Structure

### Directory Organization

```
src/
├── gui_app.py                  # Image Converter GUI (300 lines)
├── convert_to_ico.py           # Converter core logic (100 lines)
├── build_msi_gui.py            # MSI Builder GUI (1400 lines)
├── auto_updater.py             # Auto-Update system (600 lines)
└── auto_update_helper.py       # Git detection (370 lines)

tools/
└── publish_update.py           # Publishing automation (280 lines)

docs/
├── user-guide/                 # End-user documentation
│   ├── quick-start.md
│   ├── image-converter.md
│   └── msi-builder.md
├── developer-guide/            # Developer documentation
│   ├── architecture.md         # This file
│   ├── api-reference.md
│   ├── extending.md
│   └── contributing.md
└── *.md                        # Technical guides

examples/
├── example_usage.py            # Basic examples
├── advanced_integration.py     # Advanced patterns
└── custom_updater.py           # Custom update logic

scripts/
├── run_converter.bat           # Launch Image Converter
└── run_builder.bat             # Launch MSI Builder

tests/
├── test_converter.py           # Unit tests
├── test_builder.py
└── test_updater.py
```

### Module Dependencies

```
convert_to_ico.py
    └── Pillow

gui_app.py
    ├── tkinter
    ├── Pillow
    └── convert_to_ico

build_msi_gui.py
    ├── tkinter
    ├── cx_Freeze
    └── auto_update_helper

auto_updater.py
    ├── requests
    ├── packaging
    └── tkinter (optional, for GUI)

auto_update_helper.py
    └── (no external deps, uses stdlib only)

publish_update.py
    └── (uses subprocess for `gh` CLI)
```

---

## Data Flow

### 1. Image Conversion Flow

```
User selects image (PNG)
    ↓
gui_app.py: select_image()
    ↓
Display preview with zoom controls
    ↓
User clicks "Convert to ICO"
    ↓
gui_app.py: convert_to_ico_action()
    ↓
convert_to_ico.convert_to_ico(input, output, sizes)
    ↓
Pillow: Open image → Resize to [16,32,48,256] → Save as ICO
    ↓
Success message → Output .ico file
```

### 2. EXE Build Flow

```
User selects project folder
    ↓
build_msi_gui.py: select_project_folder()
    ↓
Auto-detect:
    ├── detect_main_script() → main.py found
    ├── auto_detect_git_info() → GitHub URL detected
    └── detect_version() → version from git tag
    ↓
User configures options (name, version, icon, etc.)
    ↓
User clicks "Build EXE"
    ↓
generate_setup_py()
    ├── Create cx_Freeze setup.py
    ├── Embed auto_updater.py
    └── Generate update_config.py
    ↓
run_build() → subprocess: python setup.py build
    ↓
cx_Freeze: Collect dependencies → Build EXE
    ↓
compress_with_upx() → subprocess: upx --best --lzma app.exe
    ↓
cleanup() → Remove temp files
    ↓
Success! → dist/MyApp.exe
```

### 3. Auto-Update Flow

```
App Startup
    ↓
check_and_prompt_update(root, version, url, name)
    ↓
AutoUpdater.check_for_updates()
    ↓
requests.get(version.json URL)
    ↓
Parse JSON → Compare versions
    ↓
if new_version > current_version:
    ↓
    Show UpdaterGUI notification
    ↓
    User clicks "Update Now"
    ↓
    download_update()
        ├── requests.get(download_url, stream=True)
        └── Update progress bar
    ↓
    verify_checksum()
        └── SHA256 hash verification
    ↓
    apply_update()
        ├── Backup current version
        ├── Extract ZIP to app directory
        └── Cleanup temp files
    ↓
    Restart app → New version!
```

### 4. Publish Update Flow

```
Developer runs: python tools/publish_update.py
    ↓
Enter version number (e.g., 1.0.1)
    ↓
Select files to include
    ↓
create_update_package()
    └── ZIP selected files → MyApp-1.0.1.zip
    ↓
calculate_checksum()
    └── SHA256 hash of ZIP
    ↓
Enter changelog text
    ↓
generate_version_json()
    └── Create version.json with metadata
    ↓
create_github_release()
    ├── subprocess: gh release create v1.0.1
    ├── Upload MyApp-1.0.1.zip
    └── Upload version.json
    ↓
update_version_json_in_repo()
    ├── git add version.json
    ├── git commit -m "Update to 1.0.1"
    └── git push
    ↓
Success! Update published to GitHub
```

---

## Design Patterns

### 1. Model-View-Controller (MVC)

**Usage**: GUI applications

```python
# Model: Data and business logic
class ImageConverter:
    def convert(self, input_path, output_path, sizes):
        # Core conversion logic
        pass

# View: Tkinter UI
class ImageConverterGUI(tk.Tk):
    def __init__(self):
        # Build UI
        pass

# Controller: Event handlers
    def on_convert_clicked(self):
        input_path = self.get_input_path()
        output_path = self.get_output_path()
        self.model.convert(input_path, output_path, [16,32,48,256])
```

### 2. Builder Pattern

**Usage**: EXE/MSI construction

```python
class SetupBuilder:
    def __init__(self):
        self.config = {}
    
    def set_app_name(self, name):
        self.config['name'] = name
        return self
    
    def set_version(self, version):
        self.config['version'] = version
        return self
    
    def set_icon(self, icon_path):
        self.config['icon'] = icon_path
        return self
    
    def build(self):
        return generate_setup_py(self.config)

# Usage:
setup = (SetupBuilder()
    .set_app_name("MyApp")
    .set_version("1.0.0")
    .set_icon("icon.ico")
    .build())
```

### 3. Strategy Pattern

**Usage**: Different build strategies

```python
class BuildStrategy(ABC):
    @abstractmethod
    def build(self, config):
        pass

class EXEBuildStrategy(BuildStrategy):
    def build(self, config):
        # Build standalone EXE
        subprocess.run(["python", "setup.py", "build"])

class MSIBuildStrategy(BuildStrategy):
    def build(self, config):
        # Build MSI installer
        subprocess.run(["python", "setup.py", "bdist_msi"])

# Usage:
strategy = EXEBuildStrategy() if build_type == "EXE" else MSIBuildStrategy()
strategy.build(config)
```

### 4. Observer Pattern

**Usage**: Progress updates

```python
class DownloadObserver(ABC):
    @abstractmethod
    def on_progress(self, downloaded, total):
        pass

class ProgressBarObserver(DownloadObserver):
    def __init__(self, progress_bar):
        self.progress_bar = progress_bar
    
    def on_progress(self, downloaded, total):
        percent = (downloaded / total) * 100
        self.progress_bar.set(percent)

# Usage in downloader:
def download_update(self, url, observers):
    for chunk in response.iter_content():
        downloaded += len(chunk)
        for observer in observers:
            observer.on_progress(downloaded, total)
```

### 5. Chain of Responsibility

**Usage**: Version detection

```python
class VersionDetector(ABC):
    def __init__(self, next_detector=None):
        self.next = next_detector
    
    def detect(self, project_path):
        version = self._try_detect(project_path)
        if version:
            return version
        elif self.next:
            return self.next.detect(project_path)
        return None
    
    @abstractmethod
    def _try_detect(self, project_path):
        pass

class GitTagDetector(VersionDetector):
    def _try_detect(self, project_path):
        # Try git describe --tags
        pass

class PyProjectDetector(VersionDetector):
    def _try_detect(self, project_path):
        # Try pyproject.toml
        pass

# Usage:
detector = GitTagDetector(
    next_detector=PyProjectDetector(
        next_detector=InitFileDetector()
    )
)
version = detector.detect("/path/to/project")
```

---

## Dependencies

### Core Dependencies

```toml
# pyproject.toml
[project]
requires-python = ">=3.8"
dependencies = [
    "Pillow>=10.0.0",        # Image processing
    "cx-Freeze>=6.15.0",     # EXE building
    "requests>=2.31.0",      # HTTP requests
    "packaging>=23.0",       # Version comparison
]
```

### Optional Dependencies

- **UPX**: External tool for EXE compression
- **gh CLI**: GitHub CLI for automated releases

### Dependency Graph

```
Application
    ├── Pillow (Image Converter)
    │   └── Required for: PNG/JPG → ICO conversion
    ├── cx_Freeze (MSI Builder)
    │   └── Required for: Python → EXE compilation
    ├── requests (Auto-Updater)
    │   └── Required for: HTTP downloads, version checking
    ├── packaging (Auto-Updater)
    │   └── Required for: Version comparison (1.0.1 > 1.0.0)
    └── tkinter (All GUIs)
        └── Built-in with Python

External Tools
    ├── UPX (Optional)
    │   └── Required for: EXE compression
    └── gh CLI (Optional)
        └── Required for: Automated GitHub releases
```

---

## Performance Considerations

### 1. Image Conversion

**Performance**:
- **Time**: ~0.1-0.5 seconds per image
- **Memory**: ~50-100 MB for typical images
- **Optimization**: Use PNG for best quality/speed trade-off

**Bottlenecks**:
- Large images (>4096x4096): Slow to resize
- Animated GIFs: Only first frame processed

**Improvements**:
- Batch processing: Process multiple images in parallel
- Caching: Cache resized images if converting multiple times

### 2. EXE Building

**Performance**:
- **Time**: 30-60 seconds (EXE), 2-5 minutes (MSI)
- **Disk I/O**: Heavy read/write during collection
- **CPU**: UPX compression is CPU-intensive

**Bottlenecks**:
- Dependency collection: cx_Freeze scans all packages
- UPX compression: Trade-off between size and time

**Improvements**:
- Exclude unnecessary packages: Faster collection
- Skip UPX: Faster builds, larger files
- Use SSD: Faster I/O

### 3. Auto-Update

**Performance**:
- **Version check**: <1 second (small JSON)
- **Download**: Depends on file size and connection speed
- **Apply update**: 2-5 seconds (extract + restart)

**Bottlenecks**:
- Network speed: Slow downloads on poor connections
- Disk I/O: Extraction can be slow on HDD

**Improvements**:
- Resume downloads: Handle interrupted connections
- Delta updates: Only download changed files
- Background downloads: Don't block UI

---

## Extensibility Points

### 1. Adding New Image Formats

```python
# In convert_to_ico.py
SUPPORTED_FORMATS = {
    'PNG': Image.open,
    'JPG': Image.open,
    'JPEG': Image.open,
    # Add new format:
    'SVG': lambda path: cairosvg.svg2png(path),
}
```

### 2. Custom Build Steps

```python
# In build_msi_gui.py
class BuildOrchestrator:
    def build(self, config):
        self.pre_build_hook(config)   # Extensibility point
        self.run_cx_freeze(config)
        self.compress_with_upx(config)
        self.post_build_hook(config)  # Extensibility point
    
    def post_build_hook(self, config):
        # Override in subclass for custom steps
        pass
```

### 3. Custom Update Sources

```python
# In auto_updater.py
class UpdateSource(ABC):
    @abstractmethod
    def get_latest_version(self):
        pass

class GitHubSource(UpdateSource):
    def get_latest_version(self):
        # Fetch from GitHub
        pass

class CustomServerSource(UpdateSource):
    def get_latest_version(self):
        # Fetch from custom server
        pass
```

---

## Next Steps

For more details on specific aspects:

- **[API Reference](api-reference.md)** - Detailed API documentation
- **[Extending Guide](extending.md)** - How to extend and customize
- **[Contributing](contributing.md)** - How to contribute to the project

---

<div align="center">

**[⬅️ Back to Developer Guide](../README.md)** • **[➡️ Next: API Reference](api-reference.md)**

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

</div>
