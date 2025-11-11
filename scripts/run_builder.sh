#!/bin/bash
# MSI Builder GUI Launcher (Linux/macOS)
# Run: chmod +x run_builder.sh && ./run_builder.sh

echo "========================================"
echo "  MSI Builder - Loading..."
echo "========================================"
echo ""

# Check if UV is available
if command -v uv &> /dev/null; then
    echo "Using UV to run..."
    uv run python src/build_msi_gui.py
else
    echo "UV not found, using Python directly..."
    python3 src/build_msi_gui.py
fi

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to start MSI Builder"
    echo ""
    echo "Make sure Python is installed and dependencies are installed:"
    echo "  pip3 install -r requirements.txt"
    echo ""
    read -p "Press Enter to exit..."
fi
