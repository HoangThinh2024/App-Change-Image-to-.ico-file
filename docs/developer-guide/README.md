# 👨‍💻 Developer Guide

> **Technical documentation for developers who want to understand, extend, or contribute to this project**

## 📖 What's in This Guide

This guide is for developers who want to:
- **Understand** the system architecture
- **Use** the APIs in their own projects
- **Extend** functionality with custom features
- **Contribute** code to this project

---

## 📚 Documentation Index

### 1. [Architecture](architecture.md)
**System design and structure**

Learn about:
- Component architecture (700+ lines)
- Module organization
- Data flow diagrams
- Design patterns used
- Performance considerations
- Extensibility points

**Read this first** to understand how everything fits together.

---

### 2. [API Reference](api-reference.md)
**Complete API documentation**

Detailed reference for:
- `convert_to_ico` module
- `gui_app` module (Image Converter GUI)
- `build_msi_gui` module (MSI Builder)
- `auto_updater` module (Auto-Update System)
- `auto_update_helper` module (Git Detection)
- `publish_update` module (Publishing Tool)

Includes:
- Function signatures
- Parameters and return values
- Usage examples
- Error handling

**Use this** for integrating modules into your projects.

---

### 3. [Extending Guide](extending.md)
**Customize and add features**

Learn how to:
- Add new image formats
- Create custom build strategies
- Extend auto-updater
- Build plugins
- Integrate with CI/CD
- Write tests for extensions

**Use this** to add custom functionality.

---

### 4. [Contributing Guide](contributing.md)
**Contribute to the project**

Everything you need to know:
- Code of Conduct
- Development setup
- Coding standards
- Testing guidelines
- Pull Request process
- Release workflow

**Read this** before submitting PRs.

---

## 🚀 Quick Start for Developers

### Understand the Project (30 minutes)

```
1. Read README.md (5 min)
   ↓
2. Review STRUCTURE.md (5 min)
   ↓
3. Read Architecture.md (20 min)
```

### Use the APIs (1 hour)

```
1. Read API Reference (30 min)
   ↓
2. Try examples in docs (15 min)
   ↓
3. Build something with APIs (15 min)
```

### Extend Features (2-3 hours)

```
1. Read Extending Guide (45 min)
   ↓
2. Choose extension point (15 min)
   ↓
3. Implement and test (1-2 hours)
```

### Contribute Code (ongoing)

```
1. Read Contributing Guide (30 min)
   ↓
2. Find issue or feature (15 min)
   ↓
3. Setup dev environment (30 min)
   ↓
4. Code, test, submit PR (varies)
```

---

## 💡 Common Use Cases

### Use Case 1: Integrate Auto-Update in Your App

**Goal:** Add auto-update to your Python app

**Steps:**
1. Read [API Reference - auto_updater](api-reference.md#auto_updater-module)
2. Copy this code:

```python
import tkinter as tk
from auto_updater import check_and_prompt_update

root = tk.Tk()
root.title("My App")

# Check for updates on startup
check_and_prompt_update(
    root,
    current_version="1.0.0",
    update_url="https://raw.githubusercontent.com/user/repo/main/version.json",
    app_name="MyApp"
)

root.mainloop()
```

3. Publish updates with `tools/publish_update.py`

**Time:** ~15 minutes

---

### Use Case 2: Build Custom Image Converter

**Goal:** Add SVG support to converter

**Steps:**
1. Read [Extending Guide - Add New Formats](extending.md#add-new-input-formats)
2. Install dependencies: `pip install cairosvg`
3. Add conversion function:

```python
def convert_svg_to_ico(input_path, output_path, sizes=None):
    import cairosvg
    from PIL import Image
    from io import BytesIO
    
    png_data = cairosvg.svg2png(url=input_path)
    image = Image.open(BytesIO(png_data))
    
    if sizes is None:
        sizes = [16, 32, 48, 256]
    
    image.save(output_path, format='ICO', sizes=[(s, s) for s in sizes])
```

4. Test: `convert_svg_to_ico("logo.svg", "favicon.ico")`

**Time:** ~30 minutes

---

### Use Case 3: Create Build Plugin

**Goal:** Auto-sign EXEs after build

**Steps:**
1. Read [Extending Guide - Add Build Plugins](extending.md#add-build-plugins)
2. Create plugin:

```python
class CodeSignPlugin:
    def on_post_build(self, exe_path):
        import subprocess
        subprocess.run([
            "signtool", "sign",
            "/f", "certificate.pfx",
            "/p", "password",
            "/t", "http://timestamp.digicert.com",
            exe_path
        ])
```

3. Integrate in `build_msi_gui.py`

**Time:** ~1 hour

---

### Use Case 4: Contribute Feature

**Goal:** Add new feature to project

**Steps:**
1. Read [Contributing Guide](contributing.md)
2. Find issue or create Feature Request
3. Fork repository
4. Setup dev environment:

```powershell
git clone https://github.com/YOUR_USERNAME/App-Change-Image-to-.ico-file.git
cd App-Change-Image-to-.ico-file
uv sync
pytest tests/
```

5. Create branch: `git checkout -b feature/amazing-feature`
6. Code, test, commit
7. Push and create Pull Request

**Time:** Varies (hours to days)

---

## 🧪 Testing Your Changes

### Run Tests

```powershell
# All tests
pytest

# Specific module
pytest tests/test_converter.py

# With coverage
pytest --cov=src --cov-report=html
```

### Manual Testing

```powershell
# Test Image Converter
uv run python src/gui_app.py

# Test MSI Builder
uv run python src/build_msi_gui.py

# Test Auto-Update Helper
uv run --no-project python src/auto_update_helper.py
```

---

## 📊 Code Statistics

- **Total Lines**: 5000+
- **Documentation**: 3000+ lines
- **Modules**: 6 core modules
- **Test Coverage**: Target 80%+
- **Supported Formats**: 7 image formats
- **Supported Platforms**: Windows, macOS, Linux

---

## 🛠️ Development Tools

### Recommended IDE Setup

**VS Code Extensions:**
- Python
- Pylance
- Black Formatter
- Python Test Explorer
- GitLens

**Settings:**
```json
{
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true
}
```

### Useful Commands

```powershell
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/

# Run tests with coverage
pytest --cov=src --cov-report=term-missing

# Build documentation
# (If using Sphinx or similar)
cd docs && make html
```

---

## 📖 Learning Path

### Beginner Developer

**Goal:** Understand and use the tools

1. ✅ Read [README](../../README.md)
2. ✅ Read [Architecture](architecture.md) - overview sections
3. ✅ Read [API Reference](api-reference.md) - try examples
4. ✅ Run examples in `examples/` folder
5. ✅ Integrate one module in your project

**Time:** 2-3 hours

---

### Intermediate Developer

**Goal:** Extend and customize

1. ✅ Complete Beginner path
2. ✅ Read [Architecture](architecture.md) - design patterns
3. ✅ Read [Extending Guide](extending.md)
4. ✅ Create custom extension
5. ✅ Write tests for extension
6. ✅ Share extension with community

**Time:** 1-2 days

---

### Advanced Developer / Contributor

**Goal:** Contribute to core project

1. ✅ Complete Intermediate path
2. ✅ Read [Contributing Guide](contributing.md)
3. ✅ Setup development environment
4. ✅ Find issue to work on
5. ✅ Implement, test, document
6. ✅ Submit Pull Request
7. ✅ Collaborate on review

**Time:** Ongoing

---

## 🤝 Getting Help

### Documentation

- Start with [Architecture](architecture.md) for big picture
- Use [API Reference](api-reference.md) for specific APIs
- Check [Extending Guide](extending.md) for customization
- Read [Contributing Guide](contributing.md) for contributing

### Community

- **GitHub Issues**: Ask technical questions
- **GitHub Discussions**: Share ideas, get feedback
- **Pull Requests**: Code review and collaboration

### Examples

- Look at `examples/` folder for code samples
- Check existing code in `src/` for patterns
- Read test files in `tests/` for usage examples

---

## 🎯 Goals for Developers

After reading this guide, you should be able to:

✅ Understand the system architecture  
✅ Use APIs in your own projects  
✅ Extend functionality with plugins  
✅ Write tests for your changes  
✅ Follow coding standards  
✅ Contribute to the project  
✅ Help others in the community

---

## 📚 Additional Resources

### External Documentation

- **Python**: https://docs.python.org/3/
- **Pillow**: https://pillow.readthedocs.io/
- **cx_Freeze**: https://cx-freeze.readthedocs.io/
- **Tkinter**: https://docs.python.org/3/library/tkinter.html
- **pytest**: https://docs.pytest.org/

### Related Projects

- **PyInstaller**: Alternative to cx_Freeze
- **py2app**: macOS app bundler
- **auto-py-to-exe**: GUI for PyInstaller
- **UPX**: Executable compressor

---

## 🚀 Next Steps

Choose your path:

- **Understand**: Read [Architecture](architecture.md)
- **Use**: Read [API Reference](api-reference.md)
- **Extend**: Read [Extending Guide](extending.md)
- **Contribute**: Read [Contributing Guide](contributing.md)

---

<div align="center">

**[⬅️ Back to Main Docs](../README.md)** • **[🏠 Home](../../README.md)**

**Questions?** Open an [issue](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues) or [discussion](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/discussions)

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

**⭐ Star the repo if you find it useful!**

</div>
