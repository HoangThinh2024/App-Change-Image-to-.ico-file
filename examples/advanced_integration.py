#!/usr/bin/env python3
"""
Advanced Integration Example

This example shows advanced use cases combining multiple modules.
"""

import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from convert_to_ico import convert_image_to_ico as convert_to_ico
from auto_updater import check_and_prompt_update


class AdvancedApp(tk.Tk):
    """
    Advanced application combining:
    - Image conversion
    - Auto-update
    - Modern UI
    - Background processing
    """
    
    def __init__(self):
        super().__init__()
        
        # App config
        self.title("Advanced Image Converter")
        self.geometry("600x500")
        self.version = "1.0.0"
        self.update_url = "https://raw.githubusercontent.com/user/repo/main/version.json"
        
        # State
        self.selected_files = []
        self.conversion_results = []
        
        # Build UI
        self.create_ui()
        
        # Check for updates on startup
        check_and_prompt_update(
            self,
            current_version=self.version,
            update_url=self.update_url,
            app_name="Advanced Converter"
        )
    
    def create_ui(self):
        """Create modern UI"""
        # Header
        header = tk.Frame(self, bg="#2196F3", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="🎨 Advanced Image Converter",
            font=("Arial", 18, "bold"),
            bg="#2196F3",
            fg="white"
        ).pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            header,
            text=f"v{self.version}",
            font=("Arial", 10),
            bg="#2196F3",
            fg="white"
        ).pack(side=tk.RIGHT, padx=20)
        
        # Main content
        content = tk.Frame(self, padx=20, pady=20)
        content.pack(fill=tk.BOTH, expand=True)
        
        # File selection
        select_frame = tk.Frame(content)
        select_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Button(
            select_frame,
            text="📁 Select Files",
            command=self.select_files,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            select_frame,
            text="🔄 Convert All",
            command=self.convert_all,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            width=15
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            select_frame,
            text="🗑️ Clear",
            command=self.clear_files,
            width=10
        ).pack(side=tk.LEFT, padx=5)
        
        # File list
        tk.Label(content, text="Selected Files:", font=("Arial", 10, "bold")).pack(anchor=tk.W, pady=(0, 5))
        
        list_frame = tk.Frame(content)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.file_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=("Courier", 9)
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            self,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#f0f0f0",
            padx=10,
            pady=5
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def select_files(self):
        """Select files to convert"""
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp"),
                ("All files", "*.*")
            ]
        )
        
        if files:
            self.selected_files.extend(files)
            self.update_file_list()
            self.status_var.set(f"{len(self.selected_files)} file(s) selected")
    
    def update_file_list(self):
        """Update file listbox"""
        self.file_listbox.delete(0, tk.END)
        for file in self.selected_files:
            filename = os.path.basename(file)
            self.file_listbox.insert(tk.END, f"  {filename}")
    
    def clear_files(self):
        """Clear selected files"""
        self.selected_files.clear()
        self.conversion_results.clear()
        self.file_listbox.delete(0, tk.END)
        self.status_var.set("Cleared")
    
    def convert_all(self):
        """Convert all selected files"""
        if not self.selected_files:
            messagebox.showwarning("No Files", "Please select files first")
            return
        
        # Ask for output directory
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return
        
        # Convert in background thread
        self.status_var.set("Converting...")
        
        thread = threading.Thread(
            target=self.conversion_worker,
            args=(output_dir,),
            daemon=True
        )
        thread.start()
    
    def conversion_worker(self, output_dir):
        """Background conversion worker"""
        self.conversion_results.clear()
        total = len(self.selected_files)
        
        for i, input_file in enumerate(self.selected_files, 1):
            # Update status in main thread
            self.after(0, self.status_var.set, f"Converting {i}/{total}...")
            
            # Generate output path
            filename = os.path.splitext(os.path.basename(input_file))[0]
            output_file = os.path.join(output_dir, f"{filename}.ico")
            
            try:
                convert_to_ico(input_file, output_file)
                self.conversion_results.append((input_file, "✅ Success"))
            except Exception as e:
                self.conversion_results.append((input_file, f"❌ Error: {e}"))
        
        # Show results in main thread
        self.after(0, self.show_results)
    
    def show_results(self):
        """Show conversion results"""
        self.status_var.set("Conversion complete!")
        
        success_count = sum(1 for _, result in self.conversion_results if "Success" in result)
        total = len(self.conversion_results)
        
        message = f"Converted {success_count}/{total} files\n\n"
        
        for file, result in self.conversion_results:
            filename = os.path.basename(file)
            message += f"{filename}: {result}\n"
        
        messagebox.showinfo("Conversion Results", message)
        self.clear_files()


class MinimalConverterApp(tk.Tk):
    """
    Minimal converter app - just the essentials
    """
    
    def __init__(self):
        super().__init__()
        
        self.title("Quick Converter")
        self.geometry("400x200")
        
        # UI
        tk.Label(self, text="Quick Image to ICO Converter", font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Button(
            self,
            text="Select & Convert",
            command=self.quick_convert,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=20,
            height=2
        ).pack(pady=20)
        
        self.status = tk.Label(self, text="Ready", fg="gray")
        self.status.pack()
    
    def quick_convert(self):
        """Quick one-click conversion"""
        # Select input
        input_file = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Images", "*.png *.jpg *.jpeg"), ("All", "*.*")]
        )
        
        if not input_file:
            return
        
        # Select output
        output_file = filedialog.asksaveasfilename(
            title="Save ICO As",
            defaultextension=".ico",
            filetypes=[("Icon", "*.ico")]
        )
        
        if not output_file:
            return
        
        # Convert
        try:
            self.status.config(text="Converting...", fg="blue")
            self.update()
            
            convert_to_ico(input_file, output_file)
            
            self.status.config(text="✅ Success!", fg="green")
            messagebox.showinfo("Success", f"Created: {os.path.basename(output_file)}")
        
        except Exception as e:
            self.status.config(text="❌ Failed", fg="red")
            messagebox.showerror("Error", str(e))


def example_advanced_app():
    """Run advanced app with all features"""
    print("Example: Advanced App (Image Converter + Auto-Update)")
    print("-" * 50)
    app = AdvancedApp()
    app.mainloop()
    print("✅ App closed\n")


def example_minimal_app():
    """Run minimal app"""
    print("Example: Minimal Converter (Quick & Simple)")
    print("-" * 50)
    app = MinimalConverterApp()
    app.mainloop()
    print("✅ App closed\n")


if __name__ == "__main__":
    print("=" * 50)
    print("Advanced Integration Examples")
    print("=" * 50)
    print()
    print("Choose an app to run:")
    print("1. Advanced App (Full-featured)")
    print("2. Minimal App (Quick & Simple)")
    print()
    
    choice = input("Enter number (1-2): ").strip()
    
    if choice == '1':
        example_advanced_app()
    elif choice == '2':
        example_minimal_app()
    else:
        print("Invalid choice. Running advanced app...")
        example_advanced_app()
    
    print("=" * 50)
    print("Example complete!")
    print("=" * 50)
