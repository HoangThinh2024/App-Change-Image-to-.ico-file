# 🎨 Image Converter - Complete User Guide

> **Convert any image to ICO format with professional quality**

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [GUI Mode](#gui-mode)
5. [CLI Mode](#cli-mode)
6. [Advanced Usage](#advanced-usage)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)
9. [FAQ](#faq)

---

## Overview

Image Converter là công cụ chuyên nghiệp để convert images sang format .ico (icon), hỗ trợ nhiều size và format đầu vào.

### What is ICO Format?

- **ICO** = Icon file format used by Windows
- **Multi-resolution**: Chứa nhiều kích thước trong 1 file (16x16, 32x32, 48x48, 256x256)
- **Transparency**: Hỗ trợ alpha channel (nền trong suốt)
- **Use cases**: Icons for apps, favicons for websites, desktop shortcuts

---

## Features

### ✅ Supported Input Formats

- **PNG** - Recommended (supports transparency)
- **JPG/JPEG** - Popular format
- **BMP** - Bitmap images
- **GIF** - Animated images (first frame)
- **TIFF** - High-quality format
- **WEBP** - Modern web format

### ✅ GUI Features

- **Preview with zoom**: Zoom in/out, fit window, pan image
- **Drag to resize window**: Flexible window sizing
- **Multi-size ICO**: Auto-generate 16x16, 32x32, 48x48, 256x256
- **Progress indication**: Clear status messages
- **Recent files**: Quick access to recent conversions

### ✅ CLI Features

- **Batch processing**: Convert multiple files at once
- **Custom sizes**: Specify exact icon sizes
- **Automation**: Integrate into scripts/workflows
- **Silent mode**: No GUI interaction

---

## Getting Started

### Prerequisites

```powershell
# Ensure Python 3.8+ is installed
python --version

# Install dependencies
uv sync
# OR
pip install -r requirements.txt
```

### Launch GUI

```powershell
# Method 1: Using UV (recommended)
uv run python src/gui_app.py

# Method 2: Using Python directly
python src/gui_app.py

# Method 3: Using batch script
scripts\run_converter.bat
```

---

## GUI Mode

### Interface Overview

```
╔════════════════════════════════════════╗
║  Image to ICO Converter                ║
╠════════════════════════════════════════╣
║  [Image Preview Area]                  ║
║                                        ║
║                                        ║
╠════════════════════════════════════════╣
║  [Select Image]  [Convert to ICO]     ║
║  Zoom: [-] [100%] [+] [Fit]           ║
╚════════════════════════════════════════╝
```

### Step-by-Step Guide

#### 1. Select Input Image

1. Click **"Select Image"** button
2. Browse to your image file
3. Select file (PNG, JPG, etc.)
4. Image will display in preview area

**Tip:** Drag the window corner to resize!

#### 2. Preview & Adjust

- **Zoom In**: Click `+` button or `Ctrl + +`
- **Zoom Out**: Click `-` button or `Ctrl + -`
- **Fit to Window**: Click `Fit` button or `Ctrl + 0`
- **Reset**: Click `100%` button

#### 3. Convert to ICO

1. Click **"Convert to ICO"** button
2. Choose save location
3. Enter filename (e.g., `myicon.ico`)
4. Click `Save`
5. Success message appears

**Result:** Multi-size ICO file created with 16x16, 32x32, 48x48, 256x256 px

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + O` | Open image |
| `Ctrl + S` | Convert to ICO |
| `Ctrl + +` | Zoom in |
| `Ctrl + -` | Zoom out |
| `Ctrl + 0` | Fit to window |
| `Ctrl + Q` | Quit app |

---

## CLI Mode

### Basic Usage

```powershell
# Convert single image
uv run python src/convert_to_ico.py input.png output.ico

# With Python directly
python src/convert_to_ico.py logo.jpg favicon.ico
```

### Batch Conversion

```powershell
# Convert all PNGs in folder
Get-ChildItem *.png | ForEach-Object {
    $name = $_.BaseName
    uv run python src/convert_to_ico.py $_.FullName "$name.ico"
}

# Convert specific files
uv run python src/convert_to_ico.py logo.png logo.ico
uv run python src/convert_to_ico.py favicon.jpg favicon.ico
uv run python src/convert_to_ico.py app_icon.webp app_icon.ico
```

### Custom Sizes

```python
# In Python script
from convert_to_ico import convert_to_ico

# Standard sizes (default)
convert_to_ico("input.png", "output.ico")

# Custom sizes
convert_to_ico("input.png", "output.ico", sizes=[16, 24, 32, 64, 128])

# Single size
convert_to_ico("input.png", "small.ico", sizes=[16])
```

---

## Advanced Usage

### Automation Example

```powershell
# automated_convert.ps1
param(
    [string]$InputFolder = ".\images",
    [string]$OutputFolder = ".\icons"
)

# Create output folder
New-Item -ItemType Directory -Force -Path $OutputFolder

# Convert all images
Get-ChildItem "$InputFolder\*.png", "$InputFolder\*.jpg" | ForEach-Object {
    $outputFile = Join-Path $OutputFolder ($_.BaseName + ".ico")
    Write-Host "Converting $($_.Name)..."
    uv run python src/convert_to_ico.py $_.FullName $outputFile
}

Write-Host "Done! Icons saved to $OutputFolder"
```

**Usage:**

```powershell
.\automated_convert.ps1 -InputFolder "C:\MyImages" -OutputFolder "C:\MyIcons"
```

### Integration in Python App

```python
from convert_to_ico import convert_to_ico
import tkinter as tk
from tkinter import filedialog

def convert_selected_image():
    """Convert user-selected image to ICO"""
    input_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp"),
            ("All files", "*.*")
        ]
    )
    
    if input_path:
        output_path = input_path.rsplit('.', 1)[0] + '.ico'
        
        try:
            convert_to_ico(input_path, output_path)
            print(f"✅ Successfully converted: {output_path}")
            return output_path
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None

# Usage in your app
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide root window
    
    icon_path = convert_selected_image()
    if icon_path:
        print(f"Icon ready: {icon_path}")
```

---

## Best Practices

### Input Image Quality

✅ **DO:**
- Use **PNG with transparency** for best results
- Start with **high resolution** (256x256 or larger)
- Use **square images** for icons
- Keep **simple designs** for small sizes

❌ **DON'T:**
- Use very small images (<100x100 px)
- Use complex photos for small icons
- Forget to test visibility at 16x16 px
- Ignore background color (if not transparent)

### Design Tips

1. **Test at 16x16**: Smallest size, must be readable
2. **Use contrast**: Clear distinction between elements
3. **Simplify for small sizes**: Less detail = better clarity
4. **Transparency**: Use PNG with alpha channel
5. **Consistent style**: Match your app's design

### Recommended Workflows

#### Workflow 1: Logo to Favicon

```
Logo (PNG, 512x512) 
   → Image Converter 
   → favicon.ico (16, 32, 48, 256)
   → Upload to website
```

#### Workflow 2: App Icon

```
Design (PNG, 1024x1024)
   → Image Converter
   → app_icon.ico (16, 32, 48, 256)
   → Use in MSI Builder
```

#### Workflow 3: Batch Icons

```
Multiple PNGs
   → CLI batch script
   → Multiple ICOs
   → Use in project
```

---

## Troubleshooting

### Problem: "Error opening image"

**Cause:** File format not supported or corrupted

**Solutions:**
- Verify file is a valid image (open in viewer)
- Check file extension matches actual format
- Try converting to PNG first
- Ensure file is not locked by another app

### Problem: "Output ICO looks blurry"

**Cause:** Input image too small or low quality

**Solutions:**
- Use higher resolution input (256x256 minimum)
- Start with vector graphics (SVG → PNG → ICO)
- Avoid JPEG compression artifacts
- Use PNG with transparency

### Problem: "Icon not showing in app/website"

**Cause:** Cache or format issue

**Solutions:**
- Clear browser cache (for favicons)
- Restart Windows Explorer (for app icons)
- Verify ICO file is valid (open in image viewer)
- Check file permissions

### Problem: "GUI window too small/large"

**Cause:** Display scaling or DPI settings

**Solutions:**
- Drag window corner to resize
- Use `Fit` button to auto-fit image
- Adjust Windows display settings
- Use zoom controls (+ / -)

---

## FAQ

### Q: What sizes are included in the ICO?

**A:** By default: **16x16, 32x32, 48x48, 256x256** pixels. You can customize in CLI mode.

### Q: Can I convert animated GIFs?

**A:** Only the **first frame** is converted. ICO format doesn't support animation.

### Q: Why use PNG instead of JPG?

**A:** PNG supports **transparency** (alpha channel), essential for icons. JPG always has opaque background.

### Q: How to make transparent background?

**A:** Use image editor (Photoshop, GIMP, Paint.NET) to remove background → Save as PNG → Convert to ICO.

### Q: Can I batch convert in GUI?

**A:** No, GUI is for single files. Use **CLI mode** for batch processing.

### Q: What's the maximum size?

**A:** ICO format supports up to **256x256 px** for Windows. For larger sizes, use PNG directly.

### Q: How to use for favicon?

```html
<!-- In your HTML <head> -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
```

### Q: File size too large?

**Solutions:**
- Reduce input image resolution
- Remove unnecessary large sizes
- Use fewer colors
- Compress PNG before conversion

---

## Examples Gallery

### Example 1: Company Logo

```powershell
# Input: company_logo.png (512x512)
# Process:
uv run python src/gui_app.py
# Select company_logo.png
# Convert → company_logo.ico

# Result: Multi-size ICO for website favicon
```

### Example 2: Application Icon

```powershell
# Input: app_design.png (1024x1024)
# Process:
uv run python src/convert_to_ico.py app_design.png app_icon.ico

# Use in MSI Builder:
# Icon Path: C:\path\to\app_icon.ico
```

### Example 3: Batch Social Icons

```powershell
# Input: facebook.png, twitter.png, instagram.png
# Process:
Get-ChildItem *.png | ForEach-Object {
    python src/convert_to_ico.py $_.FullName "$($_.BaseName).ico"
}

# Result: facebook.ico, twitter.ico, instagram.ico
```

---

## Performance Notes

- **Conversion speed**: ~0.1-0.5 seconds per image
- **Memory usage**: ~50-100 MB for typical images
- **Supported size**: Up to 4096x4096 input (but 256x256 output max)
- **Batch limit**: No hard limit, tested with 1000+ files

---

## Next Steps

After mastering Image Converter:

1. **📚 [MSI Builder Guide](msi-builder.md)** - Build installers with your ICO
2. **🔧 [Advanced Examples](../../examples/)** - Code samples
3. **❓ [FAQ](../FAQ.md)** - More questions & answers
4. **🐛 [Report Issues](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)**

---

## Related Tools

- **MSI Builder** - Use your ICO in app installers
- **Auto-Updater** - Add update system to your apps
- **Examples** - Sample code and workflows

---

**💡 Pro Tip:** Always keep original high-res PNG files. You can regenerate ICOs anytime with different sizes!

**❓ Need Help?** Check [FAQ](../FAQ.md) or open an [issue](https://github.com/HoangThinh2024/App-Change-Image-to-.ico-file/issues)

---

<div align="center">

**[⬅️ Back to Quick Start](quick-start.md)** • **[➡️ Next: MSI Builder](msi-builder.md)**

Made with ❤️ by [HoangThinh2024](https://github.com/HoangThinh2024)

</div>
