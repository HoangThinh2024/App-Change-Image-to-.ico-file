# 📚 Examples Directory

> **Practical code examples showing how to use this toolkit**

## Overview

This directory contains ready-to-run examples demonstrating common use cases and integration patterns.

---

## 📋 Available Examples

### 1. **basic_converter_integration.py**
**Basic image conversion examples**

Learn how to:
- Convert single images
- Use custom icon sizes
- Batch convert multiple files
- Handle errors properly
- Support multiple formats

**Run:**
```powershell
cd examples
python basic_converter_integration.py
```

**Examples included:**
- Example 1: Basic PNG to ICO conversion
- Example 2: Custom favicon sizes
- Example 3: Batch conversion
- Example 4: Production-ready error handling
- Example 5: Multi-format support

---

### 2. **auto_update_integration.py**
**Auto-update system integration**

Learn how to:
- Add one-line auto-update
- Create manual update button
- Check updates in background
- Use auto-generated configs
- Build custom update UI

**Run:**
```powershell
cd examples
python auto_update_integration.py
```

**Examples included:**
- Example 1: Simple one-line integration
- Example 2: Manual update check button
- Example 3: Background update check
- Example 4: Using auto-generated config
- Example 5: Custom update notification UI

---

### 3. **advanced_integration.py**
**Advanced full-featured applications**

Learn how to:
- Combine multiple modules
- Build modern UIs
- Process in background threads
- Show progress indicators
- Create production apps

**Run:**
```powershell
cd examples
python advanced_integration.py
```

**Apps included:**
- Advanced App: Full-featured converter with auto-update
- Minimal App: Quick & simple converter

---

### 4. **example_usage.py** *(if exists)*
**Original demo script**

Basic demonstration of converter functionality.

---

### 5. **demo.py** *(if exists)*
**Quick demo**

Simple demo showing basic features.

---

## 🚀 Quick Start

### Run All Examples

```powershell
# Navigate to examples
cd examples

# Run basic examples
python basic_converter_integration.py

# Run auto-update examples
python auto_update_integration.py

# Run advanced apps
python advanced_integration.py
```

### Import in Your Code

```python
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Now you can import
from convert_to_ico import convert_to_ico
from auto_updater import check_and_prompt_update
```

---

## 📖 Example Structure

Each example file contains:
- **Multiple examples** demonstrating different use cases
- **Complete working code** ready to run
- **Detailed comments** explaining each step
- **Error handling** showing best practices
- **Tips and notes** for real-world usage

---

## 💡 Usage Patterns

### Pattern 1: Simple Conversion

```python
from convert_to_ico import convert_to_ico

# Convert with defaults (16, 32, 48, 256)
convert_to_ico("logo.png", "favicon.ico")
```

### Pattern 2: Custom Sizes

```python
# Favicon sizes
convert_to_ico("logo.png", "favicon.ico", sizes=[16, 32, 48])

# App icon sizes
convert_to_ico("logo.png", "app.ico", sizes=[16, 32, 48, 64, 128, 256])
```

### Pattern 3: Error Handling

```python
try:
    convert_to_ico("input.png", "output.ico")
    print("✅ Success!")
except FileNotFoundError:
    print("❌ Input file not found")
except Exception as e:
    print(f"❌ Error: {e}")
```

### Pattern 4: One-Line Auto-Update

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

### Pattern 5: Manual Update Check

```python
from auto_updater import AutoUpdater

updater = AutoUpdater("1.0.0", "https://...", "MyApp")
update_info = updater.check_for_updates()

if update_info:
    print(f"New version available: {update_info['version']}")
```

---

## 🎯 Learning Path

### Beginner (15 minutes)

1. Read `basic_converter_integration.py`
2. Run examples 1-3
3. Try converting your own images

### Intermediate (30 minutes)

1. Read `auto_update_integration.py`
2. Run examples 1-2
3. Integrate auto-update in a test app

### Advanced (1 hour)

1. Read `advanced_integration.py`
2. Run both apps
3. Build your own custom app combining features

---

## 🔧 Customization

### Modify Examples

All examples are well-commented and easy to modify:

```python
# Change version
self.version = "1.0.0"  # ← Edit this

# Change update URL
self.update_url = "https://..."  # ← Edit this

# Change sizes
sizes = [16, 32, 48, 256]  # ← Edit this
```

### Create Your Own

Use examples as templates:

1. Copy an example file
2. Modify for your needs
3. Add your custom logic
4. Test and iterate

---

## 🐛 Troubleshooting

### Import Errors

If you see import errors:

```python
# Add this at the top of your script
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
```

### File Not Found

Make sure you're in the correct directory:

```powershell
# Should be in project root
cd C:\App-Change-Image-to-.ico-file

# Then navigate to examples
cd examples
```

### Module Not Installed

Install dependencies:

```powershell
pip install -r requirements.txt
# OR
uv sync
```

---

## 📚 Additional Resources

- **[User Guide](../docs/user-guide/)** - End-user documentation
- **[Developer Guide](../docs/developer-guide/)** - Technical documentation
- **[API Reference](../docs/developer-guide/api-reference.md)** - Complete API docs
- **[FAQ](../docs/FAQ.md)** - Common questions

---

## 🤝 Contributing

Found a bug in examples? Have a better example to share?

1. Open an [issue](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)
2. Submit a [pull request](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/pulls)
3. Share in [discussions](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/discussions)

---

## 💡 Tips

- **Start simple**: Try basic examples first
- **Read comments**: Examples are heavily commented
- **Experiment**: Modify examples to learn
- **Ask questions**: Open an issue if stuck
- **Share**: Show us what you built!

---

<div align="center">

**[⬅️ Back to Main README](../README.md)** • **[📚 Documentation](../docs/)**

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

⭐ **Star the repo** if these examples helped you!

</div>
