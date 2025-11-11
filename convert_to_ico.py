#!/usr/bin/env python3
"""
Chương trình chuyển đổi file ảnh thành file .ico
Image to ICO Converter - Convert image files to .ico format
"""

import os
import sys
from PIL import Image


def convert_image_to_ico(input_path, output_path=None, sizes=None):
    """
    Chuyển đổi file ảnh sang định dạng .ico
    Convert image file to .ico format
    
    Args:
        input_path (str): Đường dẫn đến file ảnh đầu vào / Path to input image file
        output_path (str): Đường dẫn đến file .ico đầu ra / Path to output .ico file (optional)
        sizes (list): Danh sách kích thước cho icon / List of sizes for icon (optional)
    
    Returns:
        str: Đường dẫn đến file .ico đã tạo / Path to created .ico file
    """
    # Kiểm tra file đầu vào có tồn tại không / Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Không tìm thấy file: {input_path} / File not found: {input_path}")
    
    # Mở ảnh đầu vào / Open input image
    try:
        img = Image.open(input_path)
    except Exception as e:
        raise ValueError(f"Không thể mở file ảnh: {e} / Cannot open image file: {e}")
    
    # Chuyển đổi sang RGBA nếu cần / Convert to RGBA if needed
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Tạo tên file đầu ra nếu không được cung cấp / Create output filename if not provided
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.ico"
    
    # Đảm bảo output có đuôi .ico / Ensure output has .ico extension
    if not output_path.lower().endswith('.ico'):
        output_path += '.ico'
    
    # Kích thước mặc định cho icon / Default icon sizes
    if sizes is None:
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    # Lưu ảnh dưới dạng .ico với nhiều kích thước / Save image as .ico with multiple sizes
    try:
        img.save(output_path, format='ICO', sizes=sizes)
        print(f"✓ Chuyển đổi thành công / Converted successfully: {output_path}")
        return output_path
    except Exception as e:
        raise RuntimeError(f"Lỗi khi lưu file .ico: {e} / Error saving .ico file: {e}")


def main():
    """
    Hàm chính để chạy chương trình từ dòng lệnh
    Main function to run the program from command line
    """
    if len(sys.argv) < 2:
        print("Cách sử dụng / Usage:")
        print(f"  python {sys.argv[0]} <input_image> [output_ico]")
        print()
        print("Ví dụ / Examples:")
        print(f"  python {sys.argv[0]} image.png")
        print(f"  python {sys.argv[0]} image.jpg output.ico")
        print()
        print("Định dạng ảnh được hỗ trợ / Supported image formats:")
        print("  PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = convert_image_to_ico(input_path, output_path)
        print(f"\n📁 File đã được lưu tại / File saved at: {os.path.abspath(result)}")
    except Exception as e:
        print(f"❌ Lỗi / Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
