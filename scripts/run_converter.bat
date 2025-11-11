@echo off
REM Image Converter GUI Launcher
REM Double-click to run Image Converter

echo ========================================
echo   Image Converter - Loading...
echo ========================================
echo.

REM Check if UV is available
where uv >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Using UV to run...
    uv run python src/gui_app.py
) else (
    echo UV not found, using Python directly...
    python src/gui_app.py
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start Image Converter
    echo.
    echo Make sure Python is installed and dependencies are installed:
    echo   pip install -r requirements.txt
    echo.
    pause
)
