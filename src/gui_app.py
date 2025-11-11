#!/usr/bin/env python3
"""
GUI Application for Image to ICO Converter
Ứng dụng GUI cho chuyển đổi ảnh sang định dạng .ico
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

# Fix import path for frozen application
if getattr(sys, 'frozen', False):
    # Running as compiled executable - modules are in src package
    from src.convert_to_ico import convert_image_to_ico
else:
    # Running as script
    try:
        from src.convert_to_ico import convert_image_to_ico
    except ImportError:
        from convert_to_ico import convert_image_to_ico


class ImageToIcoConverterGUI:
    """GUI class for Image to ICO Converter"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image to ICO Converter - Chuyển đổi ảnh sang .ico")
        self.root.geometry("800x700")
        self.root.resizable(True, True)  # Cho phép kéo dãn cửa sổ
        self.root.minsize(600, 500)  # Kích thước tối thiểu
        
        # Variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.preview_image = None
        self.original_image = None  # Lưu ảnh gốc để zoom
        self.zoom_level = 1.0  # Mức độ zoom
        self.max_preview_size = 400  # Kích thước preview tối đa
        
        # Set up UI
        self.setup_ui()
        
        # Center window
        self.center_window()
        
        # Bind resize event
        self.root.bind('<Configure>', self.on_window_resize)
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_ui(self):
        """Set up the user interface"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="🖼️ Image to ICO Converter",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=15)
        
        # Main content frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input file section
        input_frame = tk.LabelFrame(
            main_frame, 
            text="1. Chọn file ảnh đầu vào / Select Input Image",
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=10
        )
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        input_entry_frame = tk.Frame(input_frame)
        input_entry_frame.pack(fill=tk.X, pady=5)
        
        input_entry = tk.Entry(
            input_entry_frame,
            textvariable=self.input_path,
            font=('Arial', 10),
            state='readonly'
        )
        input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        browse_btn = tk.Button(
            input_entry_frame,
            text="📁 Browse",
            command=self.browse_input,
            bg='#3498db',
            fg='white',
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=5
        )
        browse_btn.pack(side=tk.RIGHT)
        
        # Supported formats info
        formats_label = tk.Label(
            input_frame,
            text="Hỗ trợ / Supported: PNG, JPG, JPEG, BMP, GIF, TIFF, WEBP",
            font=('Arial', 8),
            fg='gray'
        )
        formats_label.pack(anchor=tk.W)
        
        # Preview section
        preview_frame = tk.LabelFrame(
            main_frame,
            text="2. Xem trước / Preview",
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=10
        )
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Canvas cho preview với scrollbar
        preview_canvas_frame = tk.Frame(preview_frame)
        preview_canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.preview_canvas = tk.Canvas(
            preview_canvas_frame,
            bg='#ecf0f1',
            relief=tk.SUNKEN,
            highlightthickness=0
        )
        
        # Scrollbars
        h_scrollbar = tk.Scrollbar(preview_canvas_frame, orient=tk.HORIZONTAL, command=self.preview_canvas.xview)
        v_scrollbar = tk.Scrollbar(preview_canvas_frame, orient=tk.VERTICAL, command=self.preview_canvas.yview)
        
        self.preview_canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        
        # Grid layout
        self.preview_canvas.grid(row=0, column=0, sticky='nsew')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        
        preview_canvas_frame.grid_rowconfigure(0, weight=1)
        preview_canvas_frame.grid_columnconfigure(0, weight=1)
        
        # Label hiển thị ảnh trên canvas
        self.preview_label = tk.Label(
            self.preview_canvas,
            text="Chưa chọn ảnh / No image selected",
            bg='#ecf0f1',
            font=('Arial', 10)
        )
        self.preview_canvas.create_window(0, 0, window=self.preview_label, anchor='nw')
        
        # Zoom controls
        zoom_control_frame = tk.Frame(preview_frame)
        zoom_control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(zoom_control_frame, text="Zoom:", font=('Arial', 9)).pack(side=tk.LEFT, padx=5)
        
        zoom_out_btn = tk.Button(
            zoom_control_frame,
            text="➖",
            command=self.zoom_out,
            bg='#95a5a6',
            fg='white',
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=2
        )
        zoom_out_btn.pack(side=tk.LEFT, padx=2)
        
        self.zoom_label = tk.Label(
            zoom_control_frame,
            text="100%",
            font=('Arial', 9, 'bold'),
            width=8
        )
        self.zoom_label.pack(side=tk.LEFT, padx=5)
        
        zoom_in_btn = tk.Button(
            zoom_control_frame,
            text="➕",
            command=self.zoom_in,
            bg='#95a5a6',
            fg='white',
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=2
        )
        zoom_in_btn.pack(side=tk.LEFT, padx=2)
        
        reset_zoom_btn = tk.Button(
            zoom_control_frame,
            text="↻ Reset",
            command=self.reset_zoom,
            bg='#95a5a6',
            fg='white',
            font=('Arial', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=2
        )
        reset_zoom_btn.pack(side=tk.LEFT, padx=2)
        
        fit_window_btn = tk.Button(
            zoom_control_frame,
            text="⛶ Fit Window",
            command=self.fit_to_window,
            bg='#95a5a6',
            fg='white',
            font=('Arial', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=2
        )
        fit_window_btn.pack(side=tk.LEFT, padx=2)
        
        # Output file section
        output_frame = tk.LabelFrame(
            main_frame,
            text="3. Chọn vị trí lưu file .ico / Select Output Location (Optional)",
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=10
        )
        output_frame.pack(fill=tk.X, pady=(0, 10))
        
        output_entry_frame = tk.Frame(output_frame)
        output_entry_frame.pack(fill=tk.X, pady=5)
        
        output_entry = tk.Entry(
            output_entry_frame,
            textvariable=self.output_path,
            font=('Arial', 10)
        )
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        browse_output_btn = tk.Button(
            output_entry_frame,
            text="📁 Browse",
            command=self.browse_output,
            bg='#3498db',
            fg='white',
            font=('Arial', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=5
        )
        browse_output_btn.pack(side=tk.RIGHT)
        
        info_label = tk.Label(
            output_frame,
            text="Để trống để tự động tạo tên file / Leave empty for automatic naming",
            font=('Arial', 8),
            fg='gray'
        )
        info_label.pack(anchor=tk.W)
        
        # Convert button
        convert_btn = tk.Button(
            main_frame,
            text="🔄 Chuyển đổi / Convert to ICO",
            command=self.convert,
            bg='#27ae60',
            fg='white',
            font=('Arial', 12, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        convert_btn.pack(fill=tk.X, pady=(0, 5))
        
        # Status bar
        self.status_label = tk.Label(
            main_frame,
            text="Sẵn sàng / Ready",
            font=('Arial', 9),
            fg='green',
            anchor=tk.W
        )
        self.status_label.pack(fill=tk.X)
    
    def browse_input(self):
        """Open file dialog to select input image"""
        filename = filedialog.askopenfilename(
            title="Chọn file ảnh / Select Image File",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("BMP files", "*.bmp"),
                ("GIF files", "*.gif"),
                ("TIFF files", "*.tiff"),
                ("WEBP files", "*.webp"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            self.input_path.set(filename)
            self.load_preview(filename)
            self.update_status(f"Đã chọn: {os.path.basename(filename)} / Selected: {os.path.basename(filename)}", 'blue')
            
            # Auto-suggest output path
            if not self.output_path.get():
                base_name = os.path.splitext(filename)[0]
                suggested_output = f"{base_name}.ico"
                self.output_path.set(suggested_output)
    
    def browse_output(self):
        """Open file dialog to select output location"""
        filename = filedialog.asksaveasfilename(
            title="Chọn vị trí lưu file .ico / Select Output Location",
            defaultextension=".ico",
            filetypes=[
                ("ICO files", "*.ico"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            if not filename.lower().endswith('.ico'):
                filename += '.ico'
            self.output_path.set(filename)
    
    def load_preview(self, image_path):
        """Load and display preview of the selected image"""
        try:
            img = Image.open(image_path)
            
            # Convert to RGBA if needed
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Lưu ảnh gốc để zoom
            self.original_image = img.copy()
            self.zoom_level = 1.0
            
            # Hiển thị ảnh với zoom
            self.update_preview()
            
        except Exception as e:
            self.preview_label.config(
                text=f"Không thể xem trước ảnh\nCannot preview image\n{str(e)}",
                image=''
            )
            self.original_image = None
            self.update_status(f"Lỗi xem trước / Preview error: {str(e)}", 'red')
    
    def update_preview(self):
        """Update preview with current zoom level"""
        if self.original_image is None:
            return
        
        try:
            # Tính kích thước mới dựa trên zoom level
            new_width = int(self.original_image.width * self.zoom_level)
            new_height = int(self.original_image.height * self.zoom_level)
            
            # Resize ảnh
            resized_img = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(resized_img)
            
            # Update preview label
            self.preview_label.config(image=photo, text='')
            self.preview_label.image = photo  # Keep a reference
            
            # Update canvas scroll region
            self.preview_canvas.configure(scrollregion=self.preview_canvas.bbox('all'))
            
            # Update zoom label
            self.zoom_label.config(text=f"{int(self.zoom_level * 100)}%")
            
        except Exception as e:
            self.update_status(f"Lỗi cập nhật preview / Preview update error: {str(e)}", 'red')
    
    def zoom_in(self):
        """Zoom in the preview image"""
        if self.original_image is None:
            return
        self.zoom_level = min(self.zoom_level * 1.2, 5.0)  # Max 500%
        self.update_preview()
    
    def zoom_out(self):
        """Zoom out the preview image"""
        if self.original_image is None:
            return
        self.zoom_level = max(self.zoom_level / 1.2, 0.1)  # Min 10%
        self.update_preview()
    
    def reset_zoom(self):
        """Reset zoom to 100%"""
        if self.original_image is None:
            return
        self.zoom_level = 1.0
        self.update_preview()
    
    def fit_to_window(self):
        """Fit image to preview window"""
        if self.original_image is None:
            return
        
        # Lấy kích thước canvas
        canvas_width = self.preview_canvas.winfo_width()
        canvas_height = self.preview_canvas.winfo_height()
        
        if canvas_width <= 1 or canvas_height <= 1:
            return
        
        # Tính zoom level để fit vào window
        width_ratio = (canvas_width - 20) / self.original_image.width
        height_ratio = (canvas_height - 20) / self.original_image.height
        
        self.zoom_level = min(width_ratio, height_ratio, 1.0)  # Không zoom to hơn 100%
        self.update_preview()
    
    def on_window_resize(self, event):
        """Handle window resize event"""
        # Chỉ xử lý resize event của root window
        if event.widget == self.root:
            # Update canvas scroll region
            if hasattr(self, 'preview_canvas'):
                self.preview_canvas.configure(scrollregion=self.preview_canvas.bbox('all'))
    
    def update_status(self, message, color='black'):
        """Update status message"""
        self.status_label.config(text=message, fg=color)
        self.root.update_idletasks()
    
    def convert(self):
        """Convert the selected image to ICO format"""
        input_file = self.input_path.get()
        
        if not input_file:
            messagebox.showwarning(
                "Cảnh báo / Warning",
                "Vui lòng chọn file ảnh đầu vào!\nPlease select an input image!"
            )
            return
        
        if not os.path.exists(input_file):
            messagebox.showerror(
                "Lỗi / Error",
                "File không tồn tại!\nFile does not exist!"
            )
            return
        
        output_file = self.output_path.get() if self.output_path.get() else None
        
        try:
            self.update_status("Đang chuyển đổi... / Converting...", 'orange')
            result = convert_image_to_ico(input_file, output_file)
            
            self.update_status(
                f"✓ Chuyển đổi thành công! / Converted successfully!",
                'green'
            )
            
            messagebox.showinfo(
                "Thành công / Success",
                f"Chuyển đổi thành công!\nConverted successfully!\n\n"
                f"File đã được lưu tại:\nFile saved at:\n{os.path.abspath(result)}"
            )
            
            # Ask if user wants to convert another image
            if messagebox.askyesno(
                "Tiếp tục / Continue",
                "Bạn có muốn chuyển đổi ảnh khác không?\nDo you want to convert another image?"
            ):
                self.reset_form()
            
        except Exception as e:
            self.update_status(f"❌ Lỗi / Error: {str(e)}", 'red')
            messagebox.showerror(
                "Lỗi / Error",
                f"Không thể chuyển đổi file!\nCannot convert file!\n\nLỗi / Error: {str(e)}"
            )
    
    def reset_form(self):
        """Reset the form to initial state"""
        self.input_path.set('')
        self.output_path.set('')
        self.original_image = None
        self.zoom_level = 1.0
        self.preview_label.config(
            image='',
            text="Chưa chọn ảnh / No image selected"
        )
        self.zoom_label.config(text="100%")
        self.update_status("Sẵn sàng / Ready", 'green')


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = ImageToIcoConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
