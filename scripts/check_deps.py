"""Check that required dependencies are installed in the active environment.

Run this on the same machine/venv where you plan to build the MSI (Windows).
"""
import importlib
import sys

REQUIRED = [
    ("PIL", "Pillow"),
    ("cx_Freeze", "cx_Freeze"),
    ("requests", "requests"),
    ("packaging", "packaging"),
]

missing = []
for module, pkg in REQUIRED:
    try:
        importlib.import_module(module)
    except Exception:
        missing.append(pkg)

if not missing:
    print("All required packages are installed.")
    sys.exit(0)

print("Missing packages detected:")
for pkg in missing:
    print(f" - {pkg}")

print("\nInstall with:")
print("    pip install " + " ".join(missing))
print("or:\n    pip install -r requirements.txt")
sys.exit(1)
