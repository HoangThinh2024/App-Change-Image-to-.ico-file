"""
Setup script for building MSI installer using cx_Freeze
Script thiết lập để build file MSI installer sử dụng cx_Freeze
"""

import sys
from cx_Freeze import setup, Executable

# Application metadata
APP_NAME = "ImageToIcoConverter"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Convert images to ICO format - Chuyển đổi ảnh sang định dạng .ico"
APP_AUTHOR = "HoangThinh2024"

# Dependencies to include
build_exe_options = {
    "packages": ["tkinter", "PIL", "os", "sys"],
    "include_files": [
        ("README.md", "README.md"),
        ("LICENSE", "LICENSE"),
    ],
    "excludes": ["unittest", "email", "html", "http", "urllib", "xml"],
    "optimize": 2,
}

# MSI build options
bdist_msi_options = {
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\ImageToIcoConverter",
    "install_icon": None,  # You can add an icon file here if you have one
}

# Base for Windows GUI application (no console window)
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Executables to build
executables = [
    Executable(
        "gui_app.py",
        base=base,
        target_name="ImageToIcoConverter.exe",
        icon=None,  # You can add an icon file here if you have one
        shortcut_name="Image to ICO Converter",
        shortcut_dir="DesktopFolder",
    ),
    Executable(
        "convert_to_ico.py",
        base=None,  # Console application
        target_name="convert_to_ico.exe",
    ),
]

# Setup configuration
setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    author=APP_AUTHOR,
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)
