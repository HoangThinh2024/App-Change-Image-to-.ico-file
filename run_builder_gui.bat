@echo off
REM MSI Builder GUI Launcher
REM Khởi chạy công cụ build MSI với giao diện đồ họa

echo ========================================
echo     MSI Builder GUI Launcher
echo ========================================
echo.

REM Check if uv is installed
uv --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] uv da duoc cai dat
    echo [OK] uv is installed
    echo.
    echo Dang khoi chay voi uv...
    echo Launching with uv...
    echo.
    uv run python build_msi_gui.py
    goto :end
)

echo [INFO] uv khong duoc cai dat, dang thu voi Python...
echo [INFO] uv not installed, trying with Python...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python khong duoc cai dat hoac khong co trong PATH
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo === KHUYẾN NGHỊ / RECOMMENDED ===
    echo.
    echo 1. Cài đặt uv (nhanh hơn, hiện đại hơn):
    echo    Install uv (faster, modern):
    echo    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    echo.
    echo 2. Hoặc cài đặt Python từ:
    echo    Or install Python from:
    echo    https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo [OK] Python da duoc cai dat
echo [OK] Python is installed
echo.

REM Check if required packages are installed
echo Dang kiem tra cac thu vien...
echo Checking required packages...
echo.

python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Tkinter khong duoc cai dat
    echo [WARNING] Tkinter is not installed
)

python -c "import cx_Freeze" >nul 2>&1
if errorlevel 1 (
    echo [WARNING] cx_Freeze chua duoc cai dat
    echo [WARNING] cx_Freeze is not installed
    echo.
    echo Dang cai dat cx_Freeze...
    echo Installing cx_Freeze...
    pip install cx_Freeze
)

echo.
echo Dang khoi chay MSI Builder GUI...
echo Launching MSI Builder GUI...
echo.

REM Launch the GUI
python build_msi_gui.py

:end
if errorlevel 1 (
    echo.
    echo [ERROR] Co loi xay ra khi khoi chay GUI
    echo [ERROR] An error occurred while launching GUI
    echo.
    echo Neu ban chua cai uv, hay thu:
    echo If you haven't installed uv, try:
    echo powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    echo.
    pause
    exit /b 1
)

exit /b 0
