# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Complete Distribution System**
  - MSI Installer builder for professional Windows deployment
  - Portable ZIP packaging for USB/no-install usage
  - Standalone EXE with all dependencies included
  - cx_Freeze integration with optimized build configuration
  - Auto-detection of Python environment and dependencies
  
- **End-User Distribution Files**
  - `image-to-ico-converter-1.0.0-win64.msi` - Professional MSI installer (~20 MB)
  - `App-Change-Image-to-Ico-Portable.zip` - Portable version (~20 MB)
  - No Python required for end-users
  - Start Menu integration (MSI only)
  - Clean uninstallation support (MSI only)
  
- **Build System Enhancements**
  - `cx_freeze_setup.py` - Dedicated freeze configuration
  - Separated from package build system (pyproject.toml)
  - Auto-includes for tkinter, PIL, and all dependencies
  - DLL management and runtime inclusion
  - Optimized package excludes for smaller size
  
- **Documentation Updates**
  - Distribution Guide (`docs/guides/DISTRIBUTION_GUIDE.md`) - 800+ lines
  - Updated Quick Start with MSI/EXE instructions
  - Updated README with end-user installation options
  - Build troubleshooting and testing guides
  
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
- **Build Configuration**
  - Renamed `setup.py` to `cx_freeze_setup.py` to avoid conflicts
  - Updated `build_msi_gui.py` to generate proper freeze setup
  - Added `bin_includes` and `bin_excludes` for DLL management
  - Fixed executable paths to use `src/` package structure
  
- **Import System**
  - Updated `src/gui_app.py` to handle frozen vs. script execution
  - Fixed module imports for cx_Freeze frozen applications
  - Added proper `src` package inclusion in build
  
- Reorganized project structure
  - Source code moved to `src/`
  - Documentation in `docs/`
  - Examples in `examples/`
  - Tools in `tools/`
  - Scripts in `scripts/`
- Updated README.md with modern layout, badges, and bilingual support
- All documentation now includes extensive examples and use cases

### Fixed
- **Build System Issues**
  - Fixed "python311.dll was not found" error with proper DLL inclusion
  - Fixed "ModuleNotFoundError: No module named 'convert_to_ico'" in frozen apps
  - Fixed executable path from `gui_app.py` to `src/gui_app.py`
  - Fixed package detection to include `src` module
  
- **Runtime Issues**
  - Resolved import errors in frozen application
  - Fixed module path resolution for packaged apps
  - Ensured all dependencies are properly bundled

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
