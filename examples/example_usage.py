"""
Ví dụ sử dụng module convert_to_ico
Example of using convert_to_ico module
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from convert_to_ico import convert_image_to_ico

# Ví dụ 1: Chuyển đổi cơ bản / Example 1: Basic conversion
# convert_image_to_ico('input.png')

# Ví dụ 2: Chỉ định tên file đầu ra / Example 2: Specify output filename
# convert_image_to_ico('input.jpg', 'output.ico')

# Ví dụ 3: Chỉ định kích thước tùy chỉnh / Example 3: Custom sizes
# convert_image_to_ico('input.png', 'custom.ico', sizes=[(32, 32), (64, 64)])

print("Xem các ví dụ bên trên để sử dụng module / See examples above for module usage")
print("Uncomment các dòng để chạy thử / Uncomment lines to test")
