# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Complete project restructuring with professional organization
- Comprehensive documentation suite (8000+ lines)
  - User guides: Quick Start, Image Converter, MSI Builder, FAQ
  - Developer guides: Architecture, API Reference, Extending, Contributing
- Code examples demonstrating integration patterns
  - Basic converter integration
  - Auto-update integration
  - Advanced full-featured applications
- Launcher scripts for easy application startup
  - Windows batch scripts (.bat)
  - Linux/macOS shell scripts (.sh)
- STRUCTURE.md explaining new project organization
- README files for docs/, examples/, and developer-guide/

### Changed
- Reorganized project structure
  - Source code moved to `src/`
  - Documentation in `docs/`
  - Examples in `examples/`
  - Tools in `tools/`
  - Scripts in `scripts/`
- Updated README.md with modern layout, badges, and bilingual support
- All documentation now includes extensive examples and use cases

---

## [Previous Versions]

### Auto-Update & Compression Features

#### Added
- **Auto-Update System** (`auto_updater.py`)
  - Automatic version checking
  - Download with progress tracking
  - SHA256 checksum verification
  - Backup and rollback functionality
  - Tkinter GUI for update notifications
  
- **Auto-Setup Helper** (`auto_update_helper.py`)
  - Automatic Git repository detection
  - GitHub URL parsing (SSH and HTTPS)
  - Version detection from multiple sources (git tags, pyproject.toml, __init__.py)
  - Automatic `update_config.py` generation
  
- **UPX Compression**
  - 50-70% EXE size reduction
  - Integrated into MSI Builder GUI
  - Optional compression toggle
  
- **Publishing Tool** (`publish_update.py`)
  - Automated update package creation
  - GitHub Release integration
  - Checksum calculation
  - version.json generation
  
- **Documentation**
  - AUTO_UPDATE_GUIDE.md (500+ lines)
  - AUTO_SETUP_GUIDE.md (300+ lines)
  - BUILD_GUIDE.md
  - NEW_FEATURES.md
  - UV_QUICKSTART.md

#### Changed
- **MSI Builder GUI** enhanced with:
  - Auto-detect update checkbox (default: enabled)
  - Auto-detect Git info functionality
  - UPX compression option
  - Readonly update URL field (auto-populated)
  - Auto-generation of `update_config.py`
  
- **Python Version Requirement**
  - Updated from Python >=3.7 to Python >=3.8
  - Required for Pillow >=10.0.0 compatibility

#### Fixed
- Resolved Pillow compatibility issues with Python 3.7
- Fixed import paths in examples
- Improved error handling in build process

---

## Future Roadmap

### Planned Features
- [ ] Automated testing suite
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Code signing support
- [ ] Delta updates for smaller download sizes
- [ ] Multi-language support in GUI
- [ ] Plugin system for extensibility
- [ ] Web-based update dashboard

### Under Consideration
- [ ] macOS app bundling with py2app
- [ ] Linux AppImage/Flatpak support
- [ ] Electron-based cross-platform GUI
- [ ] Cloud storage integration for updates
- [ ] Telemetry and analytics (opt-in)

---

## Contributing

See [CONTRIBUTING.md](docs/developer-guide/contributing.md) for guidelines on how to contribute to this project.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** Version numbers will be assigned when formal releases are created. Current development is in pre-release state.
