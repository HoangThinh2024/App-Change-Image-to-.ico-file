#!/usr/bin/env python3
"""
Demonstration script for Image to ICO Converter
Script demo cho chuyển đổi ảnh sang .ico
"""

import os
import sys
from PIL import Image

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from convert_to_ico import convert_image_to_ico


def create_sample_images():
    """Create sample images for demonstration"""
    print("📝 Creating sample images...")
    print("📝 Đang tạo ảnh mẫu...")
    
    # Create temp directory if it doesn't exist
    temp_dir = "/tmp/ico_converter_demo"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create different colored sample images
    samples = [
        ("red", (255, 0, 0)),
        ("green", (0, 255, 0)),
        ("blue", (0, 0, 255)),
    ]
    
    sample_paths = []
    for name, color in samples:
        img = Image.new('RGBA', (256, 256), color=color)
        path = os.path.join(temp_dir, f"sample_{name}.png")
        img.save(path)
        print(f"   ✓ Created: {path}")
        sample_paths.append(path)
    
    return sample_paths, temp_dir


def demo_basic_conversion(sample_paths):
    """Demonstrate basic conversion"""
    print("\n" + "="*60)
    print("Demo 1: Basic Conversion / Chuyển đổi cơ bản")
    print("="*60)
    
    sample = sample_paths[0]
    print(f"Converting {sample}...")
    result = convert_image_to_ico(sample)
    print(f"✓ Result: {result}")


def demo_custom_output(sample_paths, temp_dir):
    """Demonstrate conversion with custom output name"""
    print("\n" + "="*60)
    print("Demo 2: Custom Output Name / Tên file đầu ra tùy chỉnh")
    print("="*60)
    
    sample = sample_paths[1]
    output = os.path.join(temp_dir, "my_custom_icon.ico")
    print(f"Converting {sample} to {output}...")
    result = convert_image_to_ico(sample, output)
    print(f"✓ Result: {result}")


def demo_custom_sizes(sample_paths, temp_dir):
    """Demonstrate conversion with custom sizes"""
    print("\n" + "="*60)
    print("Demo 3: Custom Icon Sizes / Kích thước icon tùy chỉnh")
    print("="*60)
    
    sample = sample_paths[2]
    output = os.path.join(temp_dir, "custom_sizes.ico")
    custom_sizes = [(16, 16), (32, 32), (64, 64)]
    
    print(f"Converting {sample} with sizes: {custom_sizes}...")
    result = convert_image_to_ico(sample, output, sizes=custom_sizes)
    print(f"✓ Result: {result}")


def show_results(temp_dir):
    """Show all generated .ico files"""
    print("\n" + "="*60)
    print("📁 Generated ICO Files / Các file ICO đã tạo:")
    print("="*60)
    
    for filename in os.listdir(temp_dir):
        if filename.endswith('.ico'):
            path = os.path.join(temp_dir, filename)
            size = os.path.getsize(path)
            print(f"   • {filename} ({size} bytes)")


def main():
    """Main demonstration function"""
    print("="*60)
    print("🎨 Image to ICO Converter - Demonstration")
    print("🎨 Chương trình chuyển đổi ảnh sang .ico - Demo")
    print("="*60)
    
    # Create sample images
    sample_paths, temp_dir = create_sample_images()
    
    # Run demonstrations
    demo_basic_conversion(sample_paths)
    demo_custom_output(sample_paths, temp_dir)
    demo_custom_sizes(sample_paths, temp_dir)
    
    # Show results
    show_results(temp_dir)
    
    print("\n" + "="*60)
    print("✅ Demonstration completed!")
    print("✅ Demo hoàn tất!")
    print(f"\n📁 All demo files are in: {temp_dir}")
    print(f"📁 Tất cả file demo trong: {temp_dir}")
    print("="*60)
    
    # Instructions
    print("\n📖 Next steps / Bước tiếp theo:")
    print("   1. Try the GUI: python gui_app.py")
    print("   2. Try CLI: python convert_to_ico.py <your_image.png>")
    print("   3. Build MSI (Windows): python build_msi.py")


if __name__ == "__main__":
    main()
