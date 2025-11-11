#!/bin/bash
# Image Converter GUI Launcher (Linux/macOS)
# Run: chmod +x run_converter.sh && ./run_converter.sh

echo "========================================"
echo "  Image Converter - Loading..."
echo "========================================"
echo ""

# Check if UV is available
if command -v uv &> /dev/null; then
    echo "Using UV to run..."
    uv run python src/gui_app.py
else
    echo "UV not found, using Python directly..."
    python3 src/gui_app.py
fi

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to start Image Converter"
    echo ""
    echo "Make sure Python is installed and dependencies are installed:"
    echo "  pip3 install -r requirements.txt"
    echo ""
    read -p "Press Enter to exit..."
fi
