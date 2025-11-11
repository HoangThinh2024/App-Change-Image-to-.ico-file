#!/usr/bin/env python3
"""
Demo: Sử dụng MSI Builder với các dự án khác
Demo: Using MSI Builder with different projects
"""

import os
import sys


def print_separator():
    """Print a separator line"""
    print("\n" + "="*70 + "\n")


def demo_simple_calculator():
    """Demo: Build a simple calculator app"""
    print("📱 Demo 1: Simple Calculator Application")
    print_separator()
    
    print("Tạo file demo: simple_calculator.py")
    print("Creating demo file: simple_calculator.py")
    print()
    
    calculator_code = '''#!/usr/bin/env python3
"""
Simple Calculator with GUI
Máy tính đơn giản với giao diện đồ họa
"""

import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Display
        self.display = tk.Entry(
            root,
            font=('Arial', 24),
            justify='right',
            bd=10
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '←', '', '']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:
                    btn = tk.Button(
                        buttons_frame,
                        text=text,
                        font=('Arial', 18),
                        command=lambda t=text: self.on_button_click(t)
                    )
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
        
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(0, self.expression)
            except:
                messagebox.showerror("Error", "Invalid expression")
                self.expression = ""
                self.display.delete(0, tk.END)
        elif char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '←':
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
'''
    
    # Save demo file
    with open('demo_calculator.py', 'w', encoding='utf-8') as f:
        f.write(calculator_code)
    
    print("✓ Đã tạo file: demo_calculator.py")
    print("✓ Created file: demo_calculator.py")
    print()
    print("Cách build với MSI Builder GUI:")
    print("How to build with MSI Builder GUI:")
    print()
    print("1. Chạy: python build_msi_gui.py")
    print("2. Chọn thư mục dự án hiện tại")
    print("3. Chọn file: demo_calculator.py")
    print("4. Điền thông tin:")
    print("   - Tên: SimpleCalculator")
    print("   - Version: 1.0.0")
    print("   - Mô tả: A simple calculator application")
    print("5. Click 'Build All'")
    print()


def demo_notepad():
    """Demo: Build a simple notepad app"""
    print("📝 Demo 2: Simple Notepad Application")
    print_separator()
    
    print("Tạo file demo: simple_notepad.py")
    print("Creating demo file: simple_notepad.py")
    print()
    
    notepad_code = '''#!/usr/bin/env python3
"""
Simple Notepad with GUI
Notepad đơn giản với giao diện đồ họa
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("800x600")
        
        self.current_file = None
        
        # Menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        # Text area
        self.text_area = scrolledtext.ScrolledText(
            root,
            font=('Consolas', 11),
            wrap=tk.WORD,
            undo=True
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
    
    def new_file(self):
        self.text_area.delete('1.0', tk.END)
        self.current_file = None
        self.root.title("Simple Notepad - New File")
    
    def open_file(self):
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', content)
                self.current_file = filename
                self.root.title(f"Simple Notepad - {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot open file:\\n{e}")
    
    def save_file(self):
        if self.current_file:
            try:
                content = self.text_area.get('1.0', 'end-1c')
                with open(self.current_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file:\\n{e}")
        else:
            self.save_file_as()
    
    def save_file_as(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            try:
                content = self.text_area.get('1.0', 'end-1c')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.current_file = filename
                self.root.title(f"Simple Notepad - {filename}")
                messagebox.showinfo("Success", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Cannot save file:\\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleNotepad(root)
    root.mainloop()
'''
    
    # Save demo file
    with open('demo_notepad.py', 'w', encoding='utf-8') as f:
        f.write(notepad_code)
    
    print("✓ Đã tạo file: demo_notepad.py")
    print("✓ Created file: demo_notepad.py")
    print()
    print("Cách build với MSI Builder GUI:")
    print("How to build with MSI Builder GUI:")
    print()
    print("1. Chạy: python build_msi_gui.py")
    print("2. Chọn file: demo_notepad.py")
    print("3. Điền thông tin app")
    print("4. Build!")
    print()


def demo_todo_list():
    """Demo: Build a todo list app"""
    print("✅ Demo 3: Todo List Application")
    print_separator()
    
    print("Tạo file demo: todo_list.py")
    print("Creating demo file: todo_list.py")
    print()
    
    todo_code = '''#!/usr/bin/env python3
"""
Simple Todo List with GUI
Ứng dụng Todo List đơn giản
"""

import tkinter as tk
from tkinter import messagebox
import json
import os


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("500x600")
        
        self.todos = []
        self.data_file = "todos.json"
        
        # Title
        title = tk.Label(
            root,
            text="📝 My Todo List",
            font=('Arial', 20, 'bold'),
            bg='#3498db',
            fg='white',
            pady=10
        )
        title.pack(fill=tk.X)
        
        # Input frame
        input_frame = tk.Frame(root, pady=10)
        input_frame.pack(fill=tk.X, padx=10)
        
        self.task_entry = tk.Entry(
            input_frame,
            font=('Arial', 12)
        )
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        add_btn = tk.Button(
            input_frame,
            text="Add",
            command=self.add_task,
            bg='#27ae60',
            fg='white',
            font=('Arial', 11, 'bold'),
            cursor='hand2',
            padx=20
        )
        add_btn.pack(side=tk.RIGHT)
        
        # Todo list frame
        list_frame = tk.Frame(root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.todo_listbox = tk.Listbox(
            list_frame,
            font=('Arial', 11),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE
        )
        self.todo_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.todo_listbox.yview)
        
        # Buttons frame
        buttons_frame = tk.Frame(root, pady=10)
        buttons_frame.pack(fill=tk.X, padx=10)
        
        tk.Button(
            buttons_frame,
            text="Delete",
            command=self.delete_task,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10),
            cursor='hand2',
            padx=15
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            buttons_frame,
            text="Clear All",
            command=self.clear_all,
            bg='#95a5a6',
            fg='white',
            font=('Arial', 10),
            cursor='hand2',
            padx=15
        ).pack(side=tk.LEFT, padx=2)
        
        # Load saved todos
        self.load_todos()
    
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.todos.append(task)
            self.todo_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_todos()
    
    def delete_task(self):
        try:
            index = self.todo_listbox.curselection()[0]
            self.todo_listbox.delete(index)
            del self.todos[index]
            self.save_todos()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete")
    
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.todo_listbox.delete(0, tk.END)
            self.todos = []
            self.save_todos()
    
    def save_todos(self):
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving: {e}")
    
    def load_todos(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
                for task in self.todos:
                    self.todo_listbox.insert(tk.END, task)
            except Exception as e:
                print(f"Error loading: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
'''
    
    # Save demo file
    with open('demo_todo_list.py', 'w', encoding='utf-8') as f:
        f.write(todo_code)
    
    print("✓ Đã tạo file: demo_todo_list.py")
    print("✓ Created file: demo_todo_list.py")
    print()
    print("Build với MSI Builder và tùy chỉnh:")
    print("Build with MSI Builder and customize:")
    print()
    print("1. Chạy GUI builder")
    print("2. Chọn file: demo_todo_list.py")
    print("3. Thêm icon (tùy chọn)")
    print("4. Tùy chọn build: Bật 'Create shortcut on Desktop'")
    print("5. Build MSI")
    print()


def print_usage_guide():
    """Print general usage guide"""
    print_separator()
    print("📖 HƯỚNG DẪN SỬ DỤNG MSI BUILDER VỚI BẤT KỲ DỰ ÁN NÀO")
    print("📖 HOW TO USE MSI BUILDER WITH ANY PROJECT")
    print_separator()
    
    print("""
🎯 CÁC BƯỚC CƠ BẢN / BASIC STEPS:

1. CÀI ĐẶT / INSTALLATION:
   
   Với uv (Khuyến nghị - Nhanh hơn 10-100x):
   # Windows:
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   uv sync
   
   Hoặc với pip (Truyền thống):
   pip install cx_Freeze
   pip install Pillow  # (optional, for image handling)

2. KHỞI CHẠY GUI / LAUNCH GUI:
   python build_msi_gui.py
   hoặc / or
   python build_msi.py --gui

3. CẤU HÌNH / CONFIGURATION:
   a. Chọn thư mục dự án / Select project folder
   b. Chọn file Python chính / Select main Python file
   c. Điền thông tin app / Fill app information
   d. (Tùy chọn) Thêm icon / (Optional) Add icon
   e. Chọn tùy chọn build / Select build options

4. BUILD:
   - Build EXE: Để test nhanh / For quick testing
   - Build MSI: Để phân phối / For distribution
   - Build All: Build cả hai / Build both

5. KẾT QUẢ / RESULTS:
   - File EXE: build/exe.win-amd64-3.x/YourApp.exe
   - File MSI: dist/YourApp-1.0.0-amd64.msi

💡 TIPS:

✓ Luôn test EXE file trước khi build MSI
✓ Sử dụng virtual environment để giảm kích thước file
✓ Lưu config để build nhanh hơn lần sau
✓ Clean build files trước khi build phiên bản mới
✓ Thêm icon để app trông chuyên nghiệp hơn

🎨 TẠO ICON:

- Sử dụng Image to ICO Converter (trong project này)
- Hoặc dùng online tools: icoconvert.com, convertio.co
- Kích thước khuyến nghị: 256x256 hoặc lớn hơn

🔧 TƯƠNG THÍCH / COMPATIBILITY:

MSI Builder GUI tương thích với:
✓ Tkinter applications
✓ PyQt/PySide applications
✓ Kivy applications
✓ Pygame games
✓ Flask/Django apps (với cấu hình đặc biệt)
✓ Command-line tools
✓ Data processing scripts
✓ Automation tools

❌ TROUBLESHOOTING:

Lỗi "Missing dependencies":
→ pip install cx_Freeze

Build thất bại:
→ Kiểm tra log trong GUI
→ Đảm bảo tất cả dependencies đã được cài đặt
→ Thử clean build files và build lại

File quá lớn:
→ Bật tùy chọn "Optimize code"
→ Sử dụng virtual environment
→ Loại bỏ dependencies không cần thiết

📚 TÀI LIỆU THAM KHẢO / REFERENCES:

- cx_Freeze docs: https://cx-freeze.readthedocs.io/
- BUILD_GUIDE.md: Hướng dẫn chi tiết
- Python Packaging: https://packaging.python.org/
""")


def main():
    """Main demo function"""
    print("\n" + "="*70)
    print("  MSI BUILDER - DEMO VÀ HƯỚNG DẪN SỬ DỤNG")
    print("  MSI BUILDER - DEMO AND USAGE GUIDE")
    print("="*70 + "\n")
    
    print("Chương trình này sẽ tạo các file demo để bạn có thể test")
    print("MSI Builder với nhiều loại ứng dụng khác nhau.")
    print()
    print("This program will create demo files so you can test")
    print("MSI Builder with different types of applications.")
    print()
    
    input("Nhấn Enter để tiếp tục / Press Enter to continue...")
    
    # Create demos
    demo_simple_calculator()
    input("\nNhấn Enter để tiếp tục / Press Enter to continue...")
    
    demo_notepad()
    input("\nNhấn Enter để tiếp tục / Press Enter to continue...")
    
    demo_todo_list()
    input("\nNhấn Enter để xem hướng dẫn / Press Enter for guide...")
    
    # Print usage guide
    print_usage_guide()
    
    print_separator()
    print("✅ Hoàn tất! Các file demo đã được tạo:")
    print("✅ Done! Demo files have been created:")
    print()
    print("   1. demo_calculator.py")
    print("   2. demo_notepad.py")
    print("   3. demo_todo_list.py")
    print()
    print("Bạn có thể chạy và build bất kỳ file nào ở trên.")
    print("You can run and build any of the files above.")
    print()
    print("Để bắt đầu build, chạy:")
    print("To start building, run:")
    print()
    print("   python build_msi_gui.py")
    print()
    print_separator()


if __name__ == "__main__":
    main()
