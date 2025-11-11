# 🤝 Contributing Guide

> **How to contribute to this project**

Thank you for considering contributing! This guide will help you get started.

---

## 📋 Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Setup](#development-setup)
4. [Coding Standards](#coding-standards)
5. [Pull Request Process](#pull-request-process)
6. [Reporting Bugs](#reporting-bugs)
7. [Suggesting Features](#suggesting-features)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, background, or identity.

### Expected Behavior

- ✅ Be respectful and considerate
- ✅ Welcome newcomers and help them learn
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what's best for the community

### Unacceptable Behavior

- ❌ Harassment or discrimination
- ❌ Trolling or insulting comments
- ❌ Publishing others' private information
- ❌ Other unprofessional conduct

---

## How Can I Contribute?

### 1. Reporting Bugs

Found a bug? Help us fix it!

**Before submitting:**
- Check [existing issues](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)
- Try the latest version
- Gather relevant information

**Bug Report Template:**

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 11]
- Python version: [e.g., 3.8.10]
- Package version: [e.g., 1.0.0]

**Additional context**
Any other relevant information.
```

### 2. Suggesting Features

Have an idea? We'd love to hear it!

**Feature Request Template:**

```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other approaches you've thought about.

**Use cases**
How would this feature be used?

**Additional context**
Mockups, examples, or references.
```

### 3. Improving Documentation

Documentation is always welcome!

**What to improve:**
- Fix typos or grammar
- Add examples
- Clarify confusing sections
- Translate to other languages
- Add diagrams or screenshots

**How to contribute docs:**
1. Find the file in `docs/`
2. Edit and submit a Pull Request
3. No code changes needed!

### 4. Writing Code

Ready to code? Great!

**Good first issues:**
- Look for issues labeled `good first issue`
- Issues labeled `help wanted`
- Small bug fixes
- Adding tests

**Before you start:**
- Comment on the issue to claim it
- Discuss your approach
- Fork the repository

---

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- UV (recommended) or pip

### Setup Steps

```powershell
# 1. Fork the repository on GitHub
# Click "Fork" button on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/App-Change-Image-to-.ico-file.git
cd App-Change-Image-to-.ico-file

# 3. Add upstream remote
git remote add upstream https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file.git

# 4. Create virtual environment
uv venv
# OR
python -m venv venv
.\venv\Scripts\activate

# 5. Install dependencies
uv sync
# OR
pip install -r requirements.txt

# 6. Install development dependencies
pip install pytest pytest-cov black flake8 mypy

# 7. Run tests to verify setup
pytest tests/
```

### Running the Tools

```powershell
# Image Converter
uv run python src/gui_app.py

# MSI Builder
uv run python src/build_msi_gui.py

# Auto-Update Helper
uv run --no-project python src/auto_update_helper.py
```

---

## Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

**Line Length:**
- Maximum 100 characters (not 79)

**Imports:**
```python
# Standard library
import os
import sys

# Third-party
import tkinter as tk
from PIL import Image

# Local
from convert_to_ico import convert_to_ico
```

**Naming Conventions:**
```python
# Classes: PascalCase
class ImageConverter:
    pass

# Functions/methods: snake_case
def convert_to_ico(input_path):
    pass

# Constants: UPPER_SNAKE_CASE
MAX_IMAGE_SIZE = 4096

# Private: _leading_underscore
def _internal_helper():
    pass
```

### Code Formatting

Use **Black** for automatic formatting:

```powershell
# Format a file
black src/gui_app.py

# Format all files
black src/ tests/

# Check without modifying
black --check src/
```

### Linting

Use **flake8** for linting:

```powershell
# Lint a file
flake8 src/gui_app.py

# Lint all files
flake8 src/ tests/

# With specific rules
flake8 --max-line-length=100 --ignore=E203,W503 src/
```

### Type Hints

Use **mypy** for type checking:

```python
# Add type hints
def convert_to_ico(input_path: str, output_path: str, sizes: list[int] = None) -> None:
    if sizes is None:
        sizes = [16, 32, 48, 256]
    # ...
```

```powershell
# Run type checker
mypy src/
```

### Documentation

**Docstrings** (Google style):

```python
def convert_to_ico(input_path: str, output_path: str, sizes: list[int] = None) -> None:
    """Convert an image to ICO format.
    
    Args:
        input_path: Path to input image file.
        output_path: Path for output ICO file.
        sizes: List of icon sizes in pixels. Default: [16, 32, 48, 256].
    
    Raises:
        FileNotFoundError: If input file doesn't exist.
        IOError: If cannot read/write files.
        ValueError: If image format is invalid.
    
    Example:
        >>> convert_to_ico("logo.png", "favicon.ico")
        >>> convert_to_ico("logo.png", "custom.ico", sizes=[16, 32, 64])
    """
    # Implementation...
```

### Comments

```python
# Good: Explain WHY, not WHAT
# Use cache to avoid re-downloading version.json on every check
if not self._cache_expired():
    return self._cached_version

# Bad: Obvious comment
# Set x to 10
x = 10
```

---

## Testing

### Writing Tests

Use **pytest** for testing:

```python
# tests/test_converter.py

import pytest
from convert_to_ico import convert_to_ico

def test_convert_png_to_ico(tmp_path):
    """Test PNG to ICO conversion"""
    input_file = "test_data/logo.png"
    output_file = tmp_path / "output.ico"
    
    convert_to_ico(str(input_file), str(output_file))
    
    assert output_file.exists()
    assert output_file.stat().st_size > 0

def test_custom_sizes(tmp_path):
    """Test custom icon sizes"""
    input_file = "test_data/logo.png"
    output_file = tmp_path / "custom.ico"
    
    convert_to_ico(str(input_file), str(output_file), sizes=[16, 32])
    
    # Verify sizes in ICO
    # ...

def test_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(FileNotFoundError):
        convert_to_ico("nonexistent.png", "output.ico")
```

### Running Tests

```powershell
# Run all tests
pytest

# Run specific test file
pytest tests/test_converter.py

# Run specific test
pytest tests/test_converter.py::test_convert_png_to_ico

# With coverage
pytest --cov=src --cov-report=html

# View coverage report
# Open htmlcov/index.html in browser
```

### Test Coverage

Aim for **80%+ coverage** for new code:

```powershell
# Check coverage
pytest --cov=src --cov-report=term-missing

# Fail if below 80%
pytest --cov=src --cov-fail-under=80
```

---

## Pull Request Process

### Before Submitting

**Checklist:**
- ✅ Code follows style guide
- ✅ All tests pass
- ✅ Added tests for new features
- ✅ Updated documentation
- ✅ No breaking changes (or clearly documented)
- ✅ Commit messages are clear

### Creating a Pull Request

**Step 1: Create a branch**

```powershell
# Update main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/amazing-feature

# Or for bug fixes
git checkout -b fix/issue-123
```

**Step 2: Make changes**

```powershell
# Make your changes
# Edit files, add features, fix bugs

# Stage changes
git add .

# Commit with clear message
git commit -m "Add amazing feature

- Implemented feature X
- Added tests for feature X
- Updated documentation

Fixes #123"
```

**Step 3: Push and create PR**

```powershell
# Push to your fork
git push origin feature/amazing-feature

# Go to GitHub and click "Create Pull Request"
```

### Pull Request Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issue
Fixes #123

## Changes Made
- Added feature X
- Fixed bug Y
- Updated docs for Z

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Manual testing performed

## Screenshots (if applicable)
Add screenshots here.

## Checklist
- [ ] Code follows style guide
- [ ] Self-reviewed code
- [ ] Commented complex sections
- [ ] Updated documentation
- [ ] No new warnings
```

### Review Process

1. **Automated Checks:**
   - CI/CD runs tests
   - Linters check code style
   - Coverage report generated

2. **Code Review:**
   - Maintainer reviews code
   - May request changes
   - Discussion via comments

3. **Approval:**
   - Once approved, PR is merged
   - Your changes are now in `main`!

### After Merge

```powershell
# Update your fork
git checkout main
git pull upstream main
git push origin main

# Delete feature branch
git branch -d feature/amazing-feature
git push origin --delete feature/amazing-feature
```

---

## Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

### Examples

**Good commits:**

```
feat(converter): Add SVG support

- Added SVG to PNG conversion
- Used cairosvg library
- Updated docs with SVG examples

Closes #45
```

```
fix(updater): Handle network timeout

- Added timeout parameter to requests
- Retry on connection errors
- Better error messages

Fixes #67
```

```
docs(readme): Update installation instructions

- Added UV installation steps
- Clarified Python version requirement
- Fixed typos
```

**Bad commits:**

```
update files
```

```
fix bug
```

```
WIP
```

---

## Release Process

For maintainers:

### Version Numbering

Use **Semantic Versioning** (semver):

- `MAJOR.MINOR.PATCH`
- `1.0.0` → `1.0.1` (patch: bug fixes)
- `1.0.1` → `1.1.0` (minor: new features)
- `1.1.0` → `2.0.0` (major: breaking changes)

### Release Checklist

```powershell
# 1. Update version
# Edit: pyproject.toml, src/__init__.py, version.json

# 2. Update CHANGELOG.md
# Add release notes

# 3. Commit
git commit -m "chore: Bump version to 1.1.0"

# 4. Create tag
git tag -a v1.1.0 -m "Release 1.1.0"

# 5. Push
git push origin main
git push origin v1.1.0

# 6. Create GitHub Release
# Go to GitHub → Releases → Create new release
# Upload built assets (EXE, MSI)

# 7. Announce
# Update README, social media, etc.
```

---

## Community

### Getting Help

- **GitHub Issues**: Technical questions
- **GitHub Discussions**: General questions, ideas
- **README**: Quick reference

### Recognition

Contributors are recognized in:
- **CONTRIBUTORS.md**: All contributors listed
- **Release Notes**: Major contributions highlighted
- **GitHub Insights**: Automatic contribution stats

---

## Resources

- **[Code of Conduct](CODE_OF_CONDUCT.md)**
- **[Architecture](architecture.md)** - System design
- **[API Reference](api-reference.md)** - Detailed API
- **[Extending](extending.md)** - Customization guide

---

## Thank You!

Every contribution, no matter how small, is valuable and appreciated. Thank you for making this project better! 🙏

---

<div align="center">

**[⬅️ Extending Guide](extending.md)** • **[🏠 Back to README](../../README.md)**

**Questions?** Open an [issue](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues) or [discussion](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/discussions)

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

⭐ **Star the repo** if you find it helpful!

</div>
