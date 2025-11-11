#!/usr/bin/env python3
"""
GUI Application for Building MSI Installer
Ứng dụng GUI để build file MSI installer với nhiều tính năng nâng cao
"""

import os
import sys
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
from pathlib import Path
import json


class BuilderGUI:
    """GUI class for MSI Builder with advanced features"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("MSI Builder - Công cụ Build Ứng dụng")
        self.root.geometry("1100x750")
        self.root.resizable(True, True)
        self.root.minsize(900, 600)
        
        # Configure style
        self.root.configure(bg='#f5f5f5')
        
        # Variables
        self.project_path = tk.StringVar()
        self.main_script = tk.StringVar()
        self.icon_path = tk.StringVar()
        self.app_name = tk.StringVar(value="MyApplication")
        self.app_version = tk.StringVar(value="1.0.0")
        self.app_author = tk.StringVar(value="")
        self.app_description = tk.StringVar(value="")
        self.is_building = False
        
        # Config file path
        self.config_file = "build_config.json"
        
        # Setup UI
        self.setup_ui()
        self.center_window()
        
        # Load saved config
        self.load_config()
        
        # Initial log message
        self.log("="*60)
        self.log("🏗️  MSI Builder - Professional Build Tool")
        self.log("="*60)
        self.log("Sẵn sàng để build ứng dụng. Hãy chọn dự án của bạn.")
        self.log("")
    
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
        # Title bar
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=70)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="🏗️ MSI Builder",
            font=('Segoe UI', 24, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=15)
        
        subtitle_label = tk.Label(
            title_frame,
            text="Công cụ Build Ứng dụng chuyên nghiệp",
            font=('Segoe UI', 10),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        subtitle_label.pack(side=tk.LEFT, padx=(0, 20))
        
        # Main container with 2 columns
        main_container = tk.Frame(self.root, bg='#f5f5f5')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create PanedWindow for resizable split
        paned = tk.PanedWindow(
            main_container,
            orient=tk.HORIZONTAL,
            sashwidth=5,
            sashrelief=tk.RAISED,
            bg='#e0e0e0'
        )
        paned.pack(fill=tk.BOTH, expand=True)
        
        # LEFT PANEL - Settings
        left_panel = tk.Frame(paned, bg='#f5f5f5')
        paned.add(left_panel, minsize=450)
        
        # Add scrollbar for left panel
        left_canvas = tk.Canvas(left_panel, bg='#f5f5f5', highlightthickness=0)
        left_scrollbar = tk.Scrollbar(left_panel, orient="vertical", command=left_canvas.yview)
        left_scrollable = tk.Frame(left_canvas, bg='#f5f5f5')
        
        left_scrollable.bind(
            "<Configure>",
            lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        )
        
        left_canvas.create_window((0, 0), window=left_scrollable, anchor="nw")
        left_canvas.configure(yscrollcommand=left_scrollbar.set)
        
        left_canvas.pack(side="left", fill="both", expand=True)
        left_scrollbar.pack(side="right", fill="y")
        
        # Content in left panel
        content_frame = tk.Frame(left_scrollable, bg='#f5f5f5', padx=15, pady=15)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Project Settings Section
        self.create_project_section(content_frame)
        
        # Application Info Section
        self.create_app_info_section(content_frame)
        
        # Icon Section
        self.create_icon_section(content_frame)
        
        # Build Options Section
        self.create_build_options_section(content_frame)
        
        # Actions Section
        self.create_actions_section(content_frame)
        
        # RIGHT PANEL - Log
        right_panel = tk.Frame(paned, bg='#ffffff')
        paned.add(right_panel, minsize=400)
        
        # Output Log Section in right panel
        self.create_log_section(right_panel)
        
        # Set initial sash position (60% left, 40% right)
        self.root.update_idletasks()
        paned.sash_place(0, int(self.root.winfo_width() * 0.55), 0)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#34495e', height=32)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="🟢 Sẵn sàng / Ready",
            font=('Segoe UI', 9),
            fg='#ecf0f1',
            bg='#34495e',
            anchor=tk.W,
            padx=15
        )
        self.status_label.pack(fill=tk.X)
    
    def create_project_section(self, parent):
        """Create project settings section"""
        section = tk.LabelFrame(
            parent,
            text="📁 Cài đặt dự án",
            font=('Segoe UI', 10, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10,
            relief=tk.FLAT,
            borderwidth=2
        )
        section.pack(fill=tk.X, pady=(0, 10))
        
        # Project path
        path_frame = tk.Frame(section, bg='#ffffff')
        path_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            path_frame,
            text="Thư mục dự án:",
            width=14,
            anchor='w',
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).pack(side=tk.LEFT)
        
        path_entry = tk.Entry(
            path_frame,
            textvariable=self.project_path,
            state='readonly',
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1
        )
        path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        tk.Button(
            path_frame,
            text="📁",
            command=self.browse_project,
            bg='#3498db',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=12,
            pady=2,
            activebackground='#2980b9',
            activeforeground='white'
        ).pack(side=tk.RIGHT)
        
        # Main script
        script_frame = tk.Frame(section, bg='#ffffff')
        script_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            script_frame,
            text="File Python chính:",
            width=14,
            anchor='w',
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).pack(side=tk.LEFT)
        
        script_entry = tk.Entry(
            script_frame,
            textvariable=self.main_script,
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1
        )
        script_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        tk.Button(
            script_frame,
            text="📄",
            command=self.browse_main_script,
            bg='#3498db',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=12,
            pady=2,
            activebackground='#2980b9',
            activeforeground='white'
        ).pack(side=tk.RIGHT)
    
    def create_app_info_section(self, parent):
        """Create application info section"""
        section = tk.LabelFrame(
            parent,
            text="ℹ️ Thông tin ứng dụng",
            font=('Segoe UI', 10, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10,
            relief=tk.FLAT,
            borderwidth=2
        )
        section.pack(fill=tk.X, pady=(0, 10))
        
        # Grid layout for compact design
        section.grid_columnconfigure(1, weight=1)
        
        # App name
        tk.Label(
            section,
            text="Tên ứng dụng:",
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).grid(row=0, column=0, sticky='w', pady=5, padx=(0, 10))
        
        tk.Entry(
            section,
            textvariable=self.app_name,
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1
        ).grid(row=0, column=1, sticky='ew', pady=5)
        
        # Version
        tk.Label(
            section,
            text="Phiên bản:",
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).grid(row=1, column=0, sticky='w', pady=5, padx=(0, 10))
        
        tk.Entry(
            section,
            textvariable=self.app_version,
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1
        ).grid(row=1, column=1, sticky='ew', pady=5)
        
        # Author
        tk.Label(
            section,
            text="Tác giả:",
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).grid(row=2, column=0, sticky='w', pady=5, padx=(0, 10))
        
        tk.Entry(
            section,
            textvariable=self.app_author,
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1
        ).grid(row=2, column=1, sticky='ew', pady=5)
        
        # Description
        tk.Label(
            section,
            text="Mô tả:",
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).grid(row=3, column=0, sticky='nw', pady=5, padx=(0, 10))
        
        desc_text = tk.Text(
            section,
            height=3,
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1,
            wrap=tk.WORD
        )
        desc_text.grid(row=3, column=1, sticky='ew', pady=5)
        desc_text.bind('<KeyRelease>', lambda e: self.app_description.set(desc_text.get('1.0', 'end-1c')))
        self.desc_text = desc_text
    
    def create_icon_section(self, parent):
        """Create icon section"""
        section = tk.LabelFrame(
            parent,
            text="🎨 Icon ứng dụng",
            font=('Segoe UI', 10, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10,
            relief=tk.FLAT,
            borderwidth=2
        )
        section.pack(fill=tk.X, pady=(0, 10))
        
        icon_frame = tk.Frame(section, bg='#ffffff')
        icon_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(
            icon_frame,
            text="Icon (.ico):",
            width=14,
            anchor='w',
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50'
        ).pack(side=tk.LEFT)
        
        icon_entry = tk.Entry(
            icon_frame,
            textvariable=self.icon_path,
            state='readonly',
            font=('Segoe UI', 9),
            relief=tk.SOLID,
            borderwidth=1
        )
        icon_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        btn_frame = tk.Frame(icon_frame, bg='#ffffff')
        btn_frame.pack(side=tk.RIGHT)
        
        tk.Button(
            btn_frame,
            text="🖼️",
            command=self.browse_icon,
            bg='#9b59b6',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=12,
            pady=2,
            activebackground='#8e44ad',
            activeforeground='white'
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            btn_frame,
            text="❌",
            command=lambda: self.icon_path.set(''),
            bg='#95a5a6',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=12,
            pady=2,
            activebackground='#7f8c8d',
            activeforeground='white'
        ).pack(side=tk.LEFT)
        
        # Info label
        tk.Label(
            section,
            text="💡 Sử dụng Image to ICO Converter để tạo icon",
            font=('Segoe UI', 8),
            fg='#7f8c8d',
            bg='#ffffff'
        ).pack(anchor=tk.W, pady=(5, 0))
    
    def create_build_options_section(self, parent):
        """Create build options section"""
        section = tk.LabelFrame(
            parent,
            text="⚙️ Tùy chọn build",
            font=('Segoe UI', 10, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10,
            relief=tk.FLAT,
            borderwidth=2
        )
        section.pack(fill=tk.X, pady=(0, 10))
        
        self.auto_clean_var = tk.BooleanVar(value=True)
        self.create_shortcut_var = tk.BooleanVar(value=True)
        self.optimize_var = tk.BooleanVar(value=True)
        self.compress_var = tk.BooleanVar(value=True)
        self.include_updater_var = tk.BooleanVar(value=True)
        self.update_url = tk.StringVar()
        
        tk.Checkbutton(
            section,
            text="🧹 Tự động dọn dẹp file build cũ",
            variable=self.auto_clean_var,
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50',
            activebackground='#ffffff',
            activeforeground='#2c3e50',
            selectcolor='#ffffff',
            cursor='hand2'
        ).pack(anchor=tk.W, pady=3)
        
        tk.Checkbutton(
            section,
            text="🔗 Tạo shortcut trên Desktop",
            variable=self.create_shortcut_var,
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50',
            activebackground='#ffffff',
            activeforeground='#2c3e50',
            selectcolor='#ffffff',
            cursor='hand2'
        ).pack(anchor=tk.W, pady=3)
        
        tk.Checkbutton(
            section,
            text="⚡ Optimize code (giảm kích thước)",
            variable=self.optimize_var,
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50',
            activebackground='#ffffff',
            activeforeground='#2c3e50',
            selectcolor='#ffffff',
            cursor='hand2'
        ).pack(anchor=tk.W, pady=3)
        
        tk.Checkbutton(
            section,
            text="🗜️ Compress EXE với UPX (giảm 50-70%)",
            variable=self.compress_var,
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50',
            activebackground='#ffffff',
            activeforeground='#2c3e50',
            selectcolor='#ffffff',
            cursor='hand2'
        ).pack(anchor=tk.W, pady=3)
        
        # Auto-update section
        update_frame = tk.Frame(section, bg='#ffffff')
        update_frame.pack(fill=tk.X, pady=(8, 0))
        
        tk.Checkbutton(
            update_frame,
            text="🔄 Tích hợp Auto-Update",
            variable=self.include_updater_var,
            font=('Segoe UI', 9),
            bg='#ffffff',
            fg='#2c3e50',
            activebackground='#ffffff',
            activeforeground='#2c3e50',
            selectcolor='#ffffff',
            cursor='hand2'
        ).pack(anchor=tk.W, pady=3)
        
        # Update URL input
        url_frame = tk.Frame(section, bg='#ffffff')
        url_frame.pack(fill=tk.X, pady=(0, 5), padx=(20, 0))
        
        tk.Label(
            url_frame,
            text="Update URL:",
            font=('Segoe UI', 8),
            bg='#ffffff',
            fg='#7f8c8d',
            width=10,
            anchor='w'
        ).pack(side=tk.LEFT)
        
        tk.Entry(
            url_frame,
            textvariable=self.update_url,
            font=('Segoe UI', 8),
            relief=tk.SOLID,
            borderwidth=1,
            fg='#7f8c8d'
        ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(
            section,
            text="💡 URL đến file version.json (VD: https://example.com/version.json)",
            font=('Segoe UI', 7),
            fg='#95a5a6',
            bg='#ffffff'
        ).pack(anchor=tk.W, padx=(20, 0))
    
    def create_actions_section(self, parent):
        """Create actions section"""
        section = tk.LabelFrame(
            parent,
            text="🚀 Hành động",
            font=('Segoe UI', 10, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            padx=15,
            pady=10,
            relief=tk.FLAT,
            borderwidth=2
        )
        section.pack(fill=tk.X, pady=(0, 10))
        
        # Build buttons in a grid
        build_frame = tk.Frame(section, bg='#ffffff')
        build_frame.pack(fill=tk.X, pady=(5, 10))
        
        build_frame.grid_columnconfigure(0, weight=1)
        build_frame.grid_columnconfigure(1, weight=1)
        build_frame.grid_columnconfigure(2, weight=1)
        
        self.build_exe_btn = tk.Button(
            build_frame,
            text="🔨 Build EXE",
            command=self.build_executable,
            bg='#27ae60',
            fg='white',
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=10,
            activebackground='#229954',
            activeforeground='white'
        )
        self.build_exe_btn.grid(row=0, column=0, sticky='ew', padx=2)
        
        self.build_msi_btn = tk.Button(
            build_frame,
            text="📦 Build MSI",
            command=self.build_msi,
            bg='#2980b9',
            fg='white',
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=10,
            activebackground='#1f618d',
            activeforeground='white'
        )
        self.build_msi_btn.grid(row=0, column=1, sticky='ew', padx=2)
        
        self.build_all_btn = tk.Button(
            build_frame,
            text="🚀 Build All",
            command=self.build_all,
            bg='#8e44ad',
            fg='white',
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=15,
            pady=10,
            activebackground='#6c3483',
            activeforeground='white'
        )
        self.build_all_btn.grid(row=0, column=2, sticky='ew', padx=2)
        
        # Utility buttons
        util_frame = tk.Frame(section, bg='#ffffff')
        util_frame.pack(fill=tk.X)
        
        util_frame.grid_columnconfigure(0, weight=1)
        util_frame.grid_columnconfigure(1, weight=1)
        util_frame.grid_columnconfigure(2, weight=1)
        
        tk.Button(
            util_frame,
            text="🧹 Clean",
            command=self.clean_build,
            bg='#e67e22',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=6,
            activebackground='#ca6f1e',
            activeforeground='white'
        ).grid(row=0, column=0, sticky='ew', padx=2)
        
        tk.Button(
            util_frame,
            text="📂 Open Folder",
            command=self.open_build_folder,
            bg='#16a085',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=6,
            activebackground='#138d75',
            activeforeground='white'
        ).grid(row=0, column=1, sticky='ew', padx=2)
        
        tk.Button(
            util_frame,
            text="💾 Save Config",
            command=self.save_config,
            bg='#34495e',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=10,
            pady=6,
            activebackground='#2c3e50',
            activeforeground='white'
        ).grid(row=0, column=2, sticky='ew', padx=2)
    
    def create_log_section(self, parent):
        """Create log output section"""
        # Header
        header_frame = tk.Frame(parent, bg='#34495e')
        header_frame.pack(fill=tk.X)
        
        tk.Label(
            header_frame,
            text="📋 Build Log",
            font=('Segoe UI', 11, 'bold'),
            bg='#34495e',
            fg='white',
            anchor=tk.W,
            padx=15,
            pady=10
        ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Button(
            header_frame,
            text="🗑️ Clear",
            command=self.clear_log,
            bg='#7f8c8d',
            fg='white',
            font=('Segoe UI', 9, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=12,
            pady=4,
            activebackground='#95a5a6',
            activeforeground='white'
        ).pack(side=tk.RIGHT, padx=10)
        
        # Log text area with frame
        log_container = tk.Frame(parent, bg='#1e1e1e', padx=2, pady=2)
        log_container.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(
            log_container,
            font=('Consolas', 9),
            bg='#1e1e1e',
            fg='#d4d4d4',
            insertbackground='white',
            wrap=tk.WORD,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure tag colors for different log types
        self.log_text.tag_config('success', foreground='#4ec9b0')
        self.log_text.tag_config('error', foreground='#f48771')
        self.log_text.tag_config('warning', foreground='#dcdcaa')
        self.log_text.tag_config('info', foreground='#569cd6')
    
    def log(self, message, color='white'):
        """Add message to log with color"""
        # Determine tag based on message content or color
        tag = None
        if '✓' in message or 'thành công' in message.lower() or 'success' in message.lower():
            tag = 'success'
        elif '❌' in message or 'lỗi' in message.lower() or 'error' in message.lower() or 'failed' in message.lower():
            tag = 'error'
        elif '⚠' in message or 'warning' in message.lower() or 'cảnh báo' in message.lower():
            tag = 'warning'
        elif 'ℹ' in message or 'info' in message.lower():
            tag = 'info'
        
        self.log_text.insert(tk.END, message + '\n', tag)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def clear_log(self):
        """Clear log text"""
        self.log_text.delete('1.0', tk.END)
    
    def update_status(self, message, color='#ecf0f1'):
        """Update status message"""
        # Map color names to hex
        color_map = {
            'black': '#ecf0f1',
            'green': '#2ecc71',
            'red': '#e74c3c',
            'orange': '#f39c12',
            'blue': '#3498db'
        }
        
        if color in color_map:
            color = color_map[color]
        
        # Add emoji based on color
        if color == color_map['green']:
            icon = '🟢'
        elif color == color_map['red']:
            icon = '🔴'
        elif color == color_map['orange']:
            icon = '🟡'
        elif color == color_map['blue']:
            icon = '🔵'
        else:
            icon = '⚪'
        
        self.status_label.config(text=f"{icon} {message}", fg=color)
        self.root.update_idletasks()
    
    def browse_project(self):
        """Browse for project directory"""
        directory = filedialog.askdirectory(title="Chọn thư mục dự án")
        if directory:
            self.project_path.set(directory)
            self.log(f"✓ Đã chọn thư mục: {directory}")
            
            # Auto-detect main script
            for filename in ['gui_app.py', 'main.py', 'app.py', '__main__.py']:
                full_path = os.path.join(directory, filename)
                if os.path.exists(full_path):
                    self.main_script.set(full_path)
                    self.log(f"✓ Tự động phát hiện file chính: {filename}")
                    break
    
    def browse_main_script(self):
        """Browse for main Python script"""
        filename = filedialog.askopenfilename(
            title="Chọn file Python chính",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        if filename:
            self.main_script.set(filename)
            self.log(f"✓ Đã chọn file chính: {os.path.basename(filename)}")
    
    def browse_icon(self):
        """Browse for icon file"""
        filename = filedialog.askopenfilename(
            title="Chọn file icon",
            filetypes=[("Icon files", "*.ico"), ("All files", "*.*")]
        )
        if filename:
            self.icon_path.set(filename)
            self.log(f"✓ Đã chọn icon: {os.path.basename(filename)}")
    
    def save_config(self):
        """Save current configuration"""
        config = {
            'project_path': self.project_path.get(),
            'main_script': self.main_script.get(),
            'icon_path': self.icon_path.get(),
            'app_name': self.app_name.get(),
            'app_version': self.app_version.get(),
            'app_author': self.app_author.get(),
            'app_description': self.app_description.get(),
            'auto_clean': self.auto_clean_var.get(),
            'create_shortcut': self.create_shortcut_var.get(),
            'optimize': self.optimize_var.get(),
            'compress': self.compress_var.get(),
            'include_updater': self.include_updater_var.get(),
            'update_url': self.update_url.get()
        }
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            self.log("✓ Đã lưu cấu hình")
            messagebox.showinfo("Thành công", "Đã lưu cấu hình thành công!")
        except Exception as e:
            self.log(f"❌ Lỗi khi lưu cấu hình: {e}")
            messagebox.showerror("Lỗi", f"Không thể lưu cấu hình:\n{e}")
    
    def load_config(self):
        """Load saved configuration"""
        if not os.path.exists(self.config_file):
            return
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            self.project_path.set(config.get('project_path', ''))
            self.main_script.set(config.get('main_script', ''))
            self.icon_path.set(config.get('icon_path', ''))
            self.app_name.set(config.get('app_name', 'MyApplication'))
            self.app_version.set(config.get('app_version', '1.0.0'))
            self.app_author.set(config.get('app_author', ''))
            self.app_description.set(config.get('app_description', ''))
            self.desc_text.insert('1.0', config.get('app_description', ''))
            self.auto_clean_var.set(config.get('auto_clean', True))
            self.create_shortcut_var.set(config.get('create_shortcut', True))
            self.optimize_var.set(config.get('optimize', True))
            self.compress_var.set(config.get('compress', True))
            self.include_updater_var.set(config.get('include_updater', True))
            self.update_url.set(config.get('update_url', ''))
            
            self.log("✓ Đã tải cấu hình đã lưu")
        except Exception as e:
            self.log(f"⚠ Không thể tải cấu hình: {e}")
    
    def validate_inputs(self):
        """Validate user inputs"""
        if not self.project_path.get():
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn thư mục dự án!")
            return False
        
        if not self.main_script.get():
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn file Python chính!")
            return False
        
        if not os.path.exists(self.main_script.get()):
            messagebox.showerror("Lỗi", "File Python không tồn tại!")
            return False
        
        if not self.app_name.get():
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập tên ứng dụng!")
            return False
        
        return True
    
    def clean_build(self):
        """Clean build directories"""
        if not self.project_path.get():
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn thư mục dự án trước!")
            return
        
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa các file build?"):
            return
        
        self.log("\n" + "="*60)
        self.log("🧹 Đang dọn dẹp file build...")
        
        project_dir = self.project_path.get()
        dirs_to_clean = ["build", "dist", "__pycache__", "*.egg-info"]
        
        for dir_pattern in dirs_to_clean:
            if '*' in dir_pattern:
                # Handle wildcard patterns
                import glob
                for path in glob.glob(os.path.join(project_dir, dir_pattern)):
                    if os.path.isdir(path):
                        try:
                            shutil.rmtree(path)
                            self.log(f"   ✓ Đã xóa: {os.path.basename(path)}")
                        except Exception as e:
                            self.log(f"   ⚠ Không thể xóa {os.path.basename(path)}: {e}")
            else:
                full_path = os.path.join(project_dir, dir_pattern)
                if os.path.exists(full_path):
                    try:
                        shutil.rmtree(full_path)
                        self.log(f"   ✓ Đã xóa: {dir_pattern}")
                    except Exception as e:
                        self.log(f"   ⚠ Không thể xóa {dir_pattern}: {e}")
        
        self.log("✓ Hoàn tất dọn dẹp!")
        self.update_status("Đã dọn dẹp file build", "green")
    
    def open_build_folder(self):
        """Open build folder in file explorer"""
        if not self.project_path.get():
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn thư mục dự án trước!")
            return
        
        build_dir = os.path.join(self.project_path.get(), "build")
        if not os.path.exists(build_dir):
            build_dir = self.project_path.get()
        
        try:
            if sys.platform == "win32":
                os.startfile(build_dir)
            elif sys.platform == "darwin":
                subprocess.run(["open", build_dir])
            else:
                subprocess.run(["xdg-open", build_dir])
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mở thư mục:\n{e}")
    
    def generate_setup_py(self):
        """Generate setup.py file for the project"""
        
        # Check if auto_updater should be included
        include_updater = self.include_updater_var.get()
        include_files = []
        packages_to_include = ["tkinter", "PIL", "os", "sys"]
        
        if include_updater:
            # Copy auto_updater.py to project directory
            updater_source = os.path.join(os.path.dirname(__file__), "auto_updater.py")
            if os.path.exists(updater_source):
                updater_dest = os.path.join(self.project_path.get(), "auto_updater.py")
                try:
                    shutil.copy2(updater_source, updater_dest)
                    self.log("✓ Đã copy auto_updater.py vào dự án")
                    packages_to_include.extend(["requests", "packaging", "hashlib", "zipfile"])
                except Exception as e:
                    self.log(f"⚠ Không thể copy auto_updater.py: {e}")
            
            # Create update_config.py
            if self.update_url.get():
                update_config_content = f'''"""
Auto-generated update configuration
"""

UPDATE_URL = "{self.update_url.get()}"
APP_VERSION = "{self.app_version.get()}"
APP_NAME = "{self.app_name.get()}"
'''
                config_path = os.path.join(self.project_path.get(), "update_config.py")
                try:
                    with open(config_path, 'w', encoding='utf-8') as f:
                        f.write(update_config_content)
                    self.log("✓ Đã tạo update_config.py")
                except Exception as e:
                    self.log(f"⚠ Không thể tạo update_config.py: {e}")
        
        packages_str = ', '.join([f'"{p}"' for p in packages_to_include])
        
        setup_content = f'''"""
Setup script for building installer
Auto-generated by MSI Builder GUI
"""

import sys
from cx_Freeze import setup, Executable

# Application metadata
APP_NAME = "{self.app_name.get()}"
APP_VERSION = "{self.app_version.get()}"
APP_DESCRIPTION = """{self.app_description.get()}"""
APP_AUTHOR = "{self.app_author.get()}"

# Dependencies to include
build_exe_options = {{
    "packages": [{packages_str}],
    "include_files": {include_files},
    "excludes": ["unittest", "email", "html", "http", "urllib", "xml", "test"],
    "optimize": {2 if self.optimize_var.get() else 0},
    "include_msvcr": True,
}}

# MSI build options
bdist_msi_options = {{
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\\{self.app_name.get()}",
    "install_icon": {f'"{self.icon_path.get()}"' if self.icon_path.get() else 'None'},
}}

# Base for Windows GUI application
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Executables to build
executables = [
    Executable(
        "{os.path.basename(self.main_script.get())}",
        base=base,
        target_name="{self.app_name.get()}.exe",
        icon={f'"{self.icon_path.get()}"' if self.icon_path.get() else 'None'},
        shortcut_name="{self.app_name.get()}",
        shortcut_dir={"'DesktopFolder'" if self.create_shortcut_var.get() else 'None'},
    ),
]

# Setup configuration
setup(
    name=APP_NAME,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    author=APP_AUTHOR,
    options={{
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    }},
    executables=executables,
)
'''
        
        setup_path = os.path.join(self.project_path.get(), "setup.py")
        try:
            with open(setup_path, 'w', encoding='utf-8') as f:
                f.write(setup_content)
            self.log(f"✓ Đã tạo file setup.py")
            return True
        except Exception as e:
            self.log(f"❌ Lỗi khi tạo setup.py: {e}")
            return False
    
    def run_build_command(self, command, description):
        """Run build command in separate thread"""
        if not self.validate_inputs():
            return
        
        if self.is_building:
            messagebox.showwarning("Cảnh báo", "Đang có quá trình build khác đang chạy!")
            return
        
        # Clean if needed
        if self.auto_clean_var.get():
            self.clean_build()
        
        # Generate setup.py
        if not self.generate_setup_py():
            messagebox.showerror("Lỗi", "Không thể tạo file setup.py!")
            return
        
        self.log("\n" + "="*60)
        self.log(f"🚀 {description}")
        self.log("="*60)
        
        self.is_building = True
        self.disable_buttons()
        self.update_status(f"Đang build... / {description}", "orange")
        
        def build_thread():
            try:
                project_dir = self.project_path.get()
                
                # Detect if uv is available
                uv_available = False
                try:
                    subprocess.run(
                        ["uv", "--version"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=True
                    )
                    uv_available = True
                    self.root.after(0, self.log, "✓ Phát hiện uv - Sử dụng uv run")
                except (subprocess.CalledProcessError, FileNotFoundError):
                    self.root.after(0, self.log, "ℹ Sử dụng python trực tiếp")
                
                # Build command based on availability
                if uv_available:
                    cmd = ["uv", "run", "python", "setup.py"] + command
                else:
                    cmd = [sys.executable, "setup.py"] + command
                
                # Run build command
                process = subprocess.Popen(
                    cmd,
                    cwd=project_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                
                # Read output line by line
                for line in process.stdout:
                    self.root.after(0, self.log, line.strip())
                
                process.wait()
                
                if process.returncode == 0:
                    # Apply UPX compression if enabled
                    if self.compress_var.get():
                        self.root.after(0, self.log, "\n🗜️ Đang nén EXE với UPX...")
                        self.root.after(0, self.compress_with_upx, project_dir)
                    
                    self.root.after(0, self.log, f"\n✓ {description} thành công!")
                    self.root.after(0, self.update_status, f"✓ {description} thành công!", "green")
                    self.root.after(0, self.show_build_results)
                else:
                    self.root.after(0, self.log, f"\n❌ {description} thất bại!")
                    self.root.after(0, self.update_status, f"❌ {description} thất bại!", "red")
                
            except Exception as e:
                self.root.after(0, self.log, f"\n❌ Lỗi: {e}")
                self.root.after(0, self.update_status, f"❌ Lỗi: {e}", "red")
            finally:
                self.is_building = False
                self.root.after(0, self.enable_buttons)
        
        threading.Thread(target=build_thread, daemon=True).start()
    
    def compress_with_upx(self, project_dir):
        """Compress EXE files with UPX"""
        try:
            # Check if UPX is available
            upx_available = False
            try:
                subprocess.run(
                    ["upx", "--version"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=True
                )
                upx_available = True
            except (subprocess.CalledProcessError, FileNotFoundError):
                self.log("⚠ UPX không được cài đặt. Bỏ qua nén.")
                self.log("💡 Tải UPX tại: https://upx.github.io/")
                return
            
            # Find all EXE files in build directory
            build_dir = os.path.join(project_dir, "build")
            if not os.path.exists(build_dir):
                return
            
            exe_files = []
            for root, dirs, files in os.walk(build_dir):
                for file in files:
                    if file.endswith(".exe"):
                        exe_files.append(os.path.join(root, file))
            
            if not exe_files:
                self.log("⚠ Không tìm thấy file EXE để nén")
                return
            
            # Compress each EXE file
            for exe_path in exe_files:
                try:
                    # Get original size
                    original_size = os.path.getsize(exe_path)
                    
                    self.log(f"   Đang nén: {os.path.basename(exe_path)}...")
                    
                    # Run UPX compression (best compression)
                    result = subprocess.run(
                        ["upx", "--best", "--lzma", exe_path],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    
                    # Get compressed size
                    compressed_size = os.path.getsize(exe_path)
                    reduction = ((original_size - compressed_size) / original_size) * 100
                    
                    if result.returncode == 0:
                        self.log(f"   ✓ Đã nén: {os.path.basename(exe_path)}")
                        self.log(f"     {original_size:,} bytes → {compressed_size:,} bytes (giảm {reduction:.1f}%)")
                    else:
                        self.log(f"   ⚠ Không thể nén {os.path.basename(exe_path)}")
                        
                except Exception as e:
                    self.log(f"   ⚠ Lỗi khi nén {os.path.basename(exe_path)}: {e}")
            
            self.log("✓ Hoàn thành nén EXE")
            
        except Exception as e:
            self.log(f"⚠ Lỗi trong quá trình nén: {e}")
    
    def build_executable(self):
        """Build executable only"""
        self.run_build_command(["build"], "Build EXE")
    
    def build_msi(self):
        """Build MSI installer"""
        if sys.platform != "win32":
            messagebox.showwarning(
                "Cảnh báo",
                "MSI installer chỉ có thể build trên Windows!"
            )
            return
        self.run_build_command(["bdist_msi"], "Build MSI")
    
    def build_all(self):
        """Build both executable and MSI"""
        if sys.platform != "win32":
            self.build_executable()
        else:
            self.run_build_command(["build", "bdist_msi"], "Build All (EXE + MSI)")
    
    def show_build_results(self):
        """Show build results"""
        self.log("\n" + "="*60)
        self.log("📁 Kết quả build / Build Results:")
        self.log("="*60)
        
        project_dir = self.project_path.get()
        
        # Check build directory
        build_dir = os.path.join(project_dir, "build")
        if os.path.exists(build_dir):
            self.log("\n✓ File EXE trong thư mục 'build':")
            for root, dirs, files in os.walk(build_dir):
                for file in files:
                    if file.endswith(".exe"):
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, project_dir)
                        self.log(f"   • {rel_path}")
        
        # Check dist directory
        dist_dir = os.path.join(project_dir, "dist")
        if os.path.exists(dist_dir):
            self.log("\n✓ File MSI trong thư mục 'dist':")
            for file in os.listdir(dist_dir):
                if file.endswith(".msi"):
                    full_path = os.path.join(dist_dir, file)
                    rel_path = os.path.relpath(full_path, project_dir)
                    self.log(f"   • {rel_path}")
        
        self.log("\n" + "="*60)
    
    def disable_buttons(self):
        """Disable build buttons"""
        self.build_exe_btn.config(state='disabled')
        self.build_msi_btn.config(state='disabled')
        self.build_all_btn.config(state='disabled')
    
    def enable_buttons(self):
        """Enable build buttons"""
        self.build_exe_btn.config(state='normal')
        self.build_msi_btn.config(state='normal')
        self.build_all_btn.config(state='normal')


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = BuilderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
