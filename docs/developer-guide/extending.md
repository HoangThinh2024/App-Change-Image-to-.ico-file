# 🔧 Extending the Toolkit

> **Guide to customizing and extending functionality**

## Overview

This toolkit is designed to be modular and extensible. This guide shows you how to add new features, customize existing ones, and integrate with your own systems.

---

## 🎨 Extending Image Converter

### Add New Input Formats

To support additional image formats (e.g., SVG, PDF):

```python
# In convert_to_ico.py

def convert_svg_to_ico(input_path, output_path, sizes=None):
    """Convert SVG to ICO using cairosvg"""
    import cairosvg
    from PIL import Image
    from io import BytesIO
    
    # Convert SVG to PNG in memory
    png_data = cairosvg.svg2png(url=input_path)
    image = Image.open(BytesIO(png_data))
    
    # Use existing ICO conversion
    return convert_to_ico_from_image(image, output_path, sizes)

def convert_to_ico_from_image(image, output_path, sizes=None):
    """Convert PIL Image object to ICO"""
    if sizes is None:
        sizes = [16, 32, 48, 256]
    
    image.save(output_path, format='ICO', sizes=[(s, s) for s in sizes])
```

### Custom Size Presets

```python
# Add size presets
SIZE_PRESETS = {
    'favicon': [16, 32, 48],
    'app': [16, 32, 48, 64, 128, 256],
    'macos': [16, 32, 64, 128, 256, 512, 1024],
    'windows': [16, 20, 24, 32, 40, 48, 64, 96, 128, 256],
}

def convert_with_preset(input_path, output_path, preset='favicon'):
    sizes = SIZE_PRESETS.get(preset, [16, 32, 48, 256])
    convert_to_ico(input_path, output_path, sizes)
```

### Add Image Processing

```python
# Add pre-processing options
def convert_to_ico_with_processing(input_path, output_path, 
                                   sizes=None, 
                                   enhance=False,
                                   background_color=None):
    from PIL import Image, ImageEnhance
    
    image = Image.open(input_path)
    
    # Add background if transparent
    if background_color and image.mode == 'RGBA':
        background = Image.new('RGB', image.size, background_color)
        background.paste(image, mask=image.split()[3])
        image = background
    
    # Enhance sharpness
    if enhance:
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(1.5)
    
    if sizes is None:
        sizes = [16, 32, 48, 256]
    
    image.save(output_path, format='ICO', sizes=[(s, s) for s in sizes])
```

---

## 🏗️ Extending MSI Builder

### Custom Build Strategies

```python
# In build_msi_gui.py or separate module

class CustomBuildStrategy:
    def __init__(self, config):
        self.config = config
    
    def pre_build(self):
        """Run before build"""
        print("Running custom pre-build steps...")
        # Your custom logic here
    
    def build(self):
        """Custom build process"""
        self.pre_build()
        # Standard build
        subprocess.run(["python", "setup.py", "build"])
        self.post_build()
    
    def post_build(self):
        """Run after build"""
        print("Running custom post-build steps...")
        # Sign EXE, create installer, etc.

# Usage in MSIBuilderGUI
def run_custom_build(self):
    config = self.get_config()
    strategy = CustomBuildStrategy(config)
    strategy.build()
```

### Add Build Plugins

```python
# Plugin system for extensibility

class BuildPlugin:
    def on_pre_build(self, config):
        pass
    
    def on_post_build(self, exe_path):
        pass

class CodeSignPlugin(BuildPlugin):
    def on_post_build(self, exe_path):
        """Sign EXE with certificate"""
        subprocess.run([
            "signtool", "sign",
            "/f", "certificate.pfx",
            "/p", "password",
            "/t", "http://timestamp.digicert.com",
            exe_path
        ])

class VirusTotalPlugin(BuildPlugin):
    def on_post_build(self, exe_path):
        """Upload to VirusTotal for scanning"""
        # Use VirusTotal API
        pass

# Register plugins
plugins = [CodeSignPlugin(), VirusTotalPlugin()]

def run_build_with_plugins(config, plugins):
    for plugin in plugins:
        plugin.on_pre_build(config)
    
    # Build EXE
    exe_path = build_exe(config)
    
    for plugin in plugins:
        plugin.on_post_build(exe_path)
```

### Custom Setup.py Templates

```python
# Create custom templates for different app types

TEMPLATES = {
    'gui_app': """
from cx_Freeze import setup, Executable

build_options = {
    "packages": ["tkinter"],
    "excludes": ["test"],
    "optimize": 2,
}

executables = [Executable(
    script="{main_script}",
    base="Win32GUI",  # No console
    icon="{icon_path}",
    target_name="{app_name}.exe"
)]

setup(
    name="{app_name}",
    version="{version}",
    options={"build_exe": build_options},
    executables=executables
)
""",
    
    'console_app': """
from cx_Freeze import setup, Executable

build_options = {
    "packages": [],
    "optimize": 2,
}

executables = [Executable(
    script="{main_script}",
    base="Console",  # With console
    target_name="{app_name}.exe"
)]

setup(
    name="{app_name}",
    version="{version}",
    options={"build_exe": build_options},
    executables=executables
)
""",
}

def generate_setup_from_template(template_name, config):
    template = TEMPLATES[template_name]
    return template.format(**config)
```

---

## 🔄 Extending Auto-Updater

### Custom Update Sources

```python
# Support different update servers

class UpdateSource(ABC):
    @abstractmethod
    def get_latest_version(self):
        """Return update info dict"""
        pass

class GitHubSource(UpdateSource):
    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo
    
    def get_latest_version(self):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
        response = requests.get(url)
        data = response.json()
        return {
            "version": data["tag_name"].lstrip("v"),
            "download_url": data["assets"][0]["browser_download_url"],
            "changelog": data["body"],
        }

class CustomServerSource(UpdateSource):
    def __init__(self, api_url):
        self.api_url = api_url
    
    def get_latest_version(self):
        response = requests.get(self.api_url)
        return response.json()

# Usage
source = GitHubSource("user", "repo")
update_info = source.get_latest_version()
```

### Delta Updates

```python
# Only download changed files instead of full package

class DeltaUpdater(AutoUpdater):
    def download_delta_update(self, current_version, target_version):
        """Download only changed files"""
        delta_url = f"{self.update_url}/delta/{current_version}-{target_version}.zip"
        return self.download_update(delta_url)
    
    def apply_delta_update(self, delta_path):
        """Apply patch to existing files"""
        with zipfile.ZipFile(delta_path, 'r') as zip_ref:
            for file in zip_ref.namelist():
                zip_ref.extract(file, self.app_dir)
```

### Background Updates

```python
# Download updates in background without blocking UI

import threading

class BackgroundUpdater(AutoUpdater):
    def check_and_download_background(self, callback=None):
        """Check and download in background thread"""
        thread = threading.Thread(
            target=self._background_worker,
            args=(callback,),
            daemon=True
        )
        thread.start()
    
    def _background_worker(self, callback):
        update_info = self.check_for_updates()
        if update_info:
            zip_path = self.download_update(update_info['download_url'])
            if self.verify_checksum(zip_path, update_info['checksum']):
                if callback:
                    callback(update_info, zip_path)
```

### Custom Update UI

```python
# Create custom update notification

class CustomUpdaterGUI:
    def __init__(self, parent, update_info):
        self.window = tk.Toplevel(parent)
        self.window.title("Update Available")
        
        # Custom design
        tk.Label(self.window, 
                 text=f"Version {update_info['version']} is available!",
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        # Changelog with rich text
        changelog_text = scrolledtext.ScrolledText(
            self.window, width=50, height=10, wrap=tk.WORD
        )
        changelog_text.insert('1.0', update_info['changelog'])
        changelog_text.config(state='disabled')
        changelog_text.pack(padx=10, pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.window)
        tk.Button(button_frame, text="Update Now", 
                 command=self.update_now).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Remind Later", 
                 command=self.remind_later).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Skip This Version", 
                 command=self.skip_version).pack(side=tk.LEFT, padx=5)
        button_frame.pack(pady=10)
```

---

## 🤖 Extending Auto-Setup Helper

### Custom Detection Methods

```python
# Add custom version detection sources

def detect_version_from_custom_file(project_path):
    """Detect version from custom VERSION file"""
    version_file = os.path.join(project_path, "VERSION")
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            return f.read().strip()
    return None

def detect_version_from_package_json(project_path):
    """Detect version from package.json (for Electron apps)"""
    package_json = os.path.join(project_path, "package.json")
    if os.path.exists(package_json):
        import json
        with open(package_json, 'r') as f:
            data = json.load(f)
            return data.get("version")
    return None

# Extend detection chain
def auto_detect_version_extended(project_path):
    # Try all methods
    version = (
        detect_version_from_git(project_path) or
        detect_version_from_pyproject(project_path) or
        detect_version_from_init(project_path) or
        detect_version_from_custom_file(project_path) or
        detect_version_from_package_json(project_path) or
        "1.0.0"
    )
    return version
```

### Support Other VCS

```python
# Support GitLab, Bitbucket, etc.

def parse_gitlab_url(url):
    """Parse GitLab URL"""
    # https://gitlab.com/user/repo.git
    # git@gitlab.com:user/repo.git
    if 'gitlab.com' in url:
        if url.startswith('git@'):
            url = url.replace('git@gitlab.com:', '')
        else:
            url = url.replace('https://gitlab.com/', '')
        url = url.rstrip('.git')
        parts = url.split('/')
        return parts[0], parts[1], 'gitlab'
    return None

def generate_update_url_for_vcs(owner, repo, vcs_type):
    """Generate update URL for different VCS"""
    if vcs_type == 'github':
        return f"https://raw.githubusercontent.com/{owner}/{repo}/main/version.json"
    elif vcs_type == 'gitlab':
        return f"https://gitlab.com/{owner}/{repo}/-/raw/main/version.json"
    elif vcs_type == 'bitbucket':
        return f"https://bitbucket.org/{owner}/{repo}/raw/main/version.json"
```

---

## 🛠️ Creating Plugins

### Plugin Architecture

```python
# plugin_system.py

class Plugin:
    name = "Base Plugin"
    version = "1.0.0"
    
    def on_load(self):
        """Called when plugin is loaded"""
        pass
    
    def on_unload(self):
        """Called when plugin is unloaded"""
        pass

class PluginManager:
    def __init__(self):
        self.plugins = []
    
    def load_plugin(self, plugin_class):
        plugin = plugin_class()
        plugin.on_load()
        self.plugins.append(plugin)
        print(f"Loaded plugin: {plugin.name} v{plugin.version}")
    
    def unload_all(self):
        for plugin in self.plugins:
            plugin.on_unload()
        self.plugins.clear()
    
    def execute_hook(self, hook_name, *args, **kwargs):
        """Execute hook on all plugins"""
        for plugin in self.plugins:
            if hasattr(plugin, hook_name):
                getattr(plugin, hook_name)(*args, **kwargs)
```

### Example Plugin: Auto-Backup

```python
# plugins/auto_backup.py

class AutoBackupPlugin(Plugin):
    name = "Auto Backup"
    version = "1.0.0"
    
    def on_pre_build(self, config):
        """Backup project before build"""
        import shutil
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"backups/{config['app_name']}_{timestamp}"
        
        shutil.copytree(config['project_folder'], backup_path)
        print(f"Backup created: {backup_path}")
```

### Example Plugin: Telemetry

```python
# plugins/telemetry.py

class TelemetryPlugin(Plugin):
    name = "Telemetry"
    version = "1.0.0"
    
    def on_app_start(self):
        """Track app launch"""
        self.send_event("app_start")
    
    def on_app_close(self):
        """Track app close"""
        self.send_event("app_close")
    
    def send_event(self, event_name):
        """Send telemetry data"""
        import requests
        requests.post("https://analytics.example.com/track", json={
            "event": event_name,
            "app": "MyApp",
            "version": "1.0.0",
        })
```

---

## 📦 Integrating with CI/CD

### GitHub Actions

```yaml
# .github/workflows/build.yml

name: Build and Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: windows-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Build EXE
        run: |
          python src/build_msi_gui.py --cli --config build_config.json
      
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            dist/*.exe
            dist/*.msi
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Automated Version Bumping

```python
# scripts/bump_version.py

import sys
import re

def bump_version(version, bump_type='patch'):
    """Bump semantic version"""
    major, minor, patch = map(int, version.split('.'))
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    
    return f"{major}.{minor}.{patch}"

def update_version_in_files(new_version):
    """Update version in all relevant files"""
    files = ['pyproject.toml', 'src/__init__.py', 'version.json']
    
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace version string
        content = re.sub(r'version = "[^"]+"', f'version = "{new_version}"', content)
        content = re.sub(r'__version__ = "[^"]+"', f'__version__ = "{new_version}"', content)
        
        with open(file, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    current = "1.0.0"
    bump_type = sys.argv[1] if len(sys.argv) > 1 else 'patch'
    new = bump_version(current, bump_type)
    update_version_in_files(new)
    print(f"Version bumped: {current} → {new}")
```

---

## 🧪 Testing Extensions

### Unit Tests for Custom Features

```python
# tests/test_extensions.py

import unittest
from my_extensions import CustomBuildStrategy

class TestCustomBuild(unittest.TestCase):
    def test_pre_build_hook(self):
        config = {"app_name": "TestApp"}
        strategy = CustomBuildStrategy(config)
        
        # Verify pre-build runs
        strategy.pre_build()
        self.assertTrue(os.path.exists("pre_build_flag.txt"))
    
    def test_post_build_hook(self):
        strategy = CustomBuildStrategy({})
        strategy.post_build()
        # Verify post-build actions
```

### Integration Tests

```python
# tests/test_integration.py

def test_full_build_pipeline():
    """Test entire build process with extensions"""
    # Setup
    config = create_test_config()
    
    # Build with plugins
    plugins = [AutoBackupPlugin(), CodeSignPlugin()]
    result = run_build_with_plugins(config, plugins)
    
    # Verify
    assert result.success
    assert os.path.exists(result.exe_path)
    assert is_signed(result.exe_path)
```

---

## 📚 Resources

- **[Architecture](architecture.md)** - Understand system design
- **[API Reference](api-reference.md)** - Detailed API docs
- **[Contributing](contributing.md)** - How to contribute your extensions

---

<div align="center">

**[⬅️ API Reference](api-reference.md)** • **[➡️ Contributing](contributing.md)**

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

</div>
