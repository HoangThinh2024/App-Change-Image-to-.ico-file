@echo off
REM MSI Builder GUI Launcher
REM Double-click to run MSI Builder

echo ========================================
echo   MSI Builder - Loading...
echo ========================================
echo.

REM Check if UV is available
where uv >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo Using UV to run...
    uv run python src/build_msi_gui.py
) else (
    echo UV not found, using Python directly...
    python src/build_msi_gui.py
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to start MSI Builder
    echo.
    echo Make sure Python is installed and dependencies are installed:
    echo   pip install -r requirements.txt
    echo.
    pause
)
