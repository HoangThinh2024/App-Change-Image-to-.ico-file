#!/usr/bin/env python3
"""
Example: How to integrate Auto-Update into your application
Ví dụ: Cách tích hợp Auto-Update vào ứng dụng của bạn
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Example 1: Basic Integration
# Tích hợp cơ bản

def example_basic_app():
    """Example of basic auto-update integration"""
    
    root = tk.Tk()
    root.title("My App with Auto-Update")
    root.geometry("600x400")
    
    # Your app configuration
    APP_VERSION = "1.0.0"
    APP_NAME = "MyApp"
    UPDATE_URL = "https://example.com/myapp/version.json"
    
    # Your main UI
    label = tk.Label(
        root,
        text=f"Welcome to {APP_NAME} v{APP_VERSION}",
        font=('Arial', 16, 'bold')
    )
    label.pack(pady=50)
    
    # Add update check on startup
    def check_for_updates():
        """Check for updates when app starts"""
        try:
            from auto_updater import check_and_prompt_update
            
            # This will automatically show dialog if update is available
            check_and_prompt_update(
                parent_window=root,
                current_version=APP_VERSION,
                update_url=UPDATE_URL,
                app_name=APP_NAME
            )
        except ImportError:
            print("⚠ Auto-updater not available")
        except Exception as e:
            print(f"⚠ Error checking updates: {e}")
    
    # Check after 1 second (let UI load first)
    root.after(1000, check_for_updates)
    
    root.mainloop()


# Example 2: Manual Update Check
# Kiểm tra update thủ công

def example_manual_check():
    """Example with manual update check button"""
    
    root = tk.Tk()
    root.title("App with Manual Update Check")
    root.geometry("600x400")
    
    APP_VERSION = "1.0.0"
    UPDATE_URL = "https://example.com/myapp/version.json"
    APP_NAME = "MyApp"
    
    # Status label
    status_label = tk.Label(root, text="Ready", fg='green')
    status_label.pack(pady=20)
    
    def manual_update_check():
        """Manually check for updates"""
        status_label.config(text="Checking for updates...", fg='orange')
        root.update()
        
        try:
            from auto_updater import AutoUpdater
            
            updater = AutoUpdater(APP_VERSION, UPDATE_URL, APP_NAME)
            update_info = updater.check_for_updates(silent=False)
            
            if update_info:
                status_label.config(
                    text=f"Update available: v{update_info['version']}",
                    fg='blue'
                )
                
                # Show update GUI
                from auto_updater import UpdaterGUI
                UpdaterGUI(root, updater, update_info)
            else:
                status_label.config(
                    text="You're up to date!",
                    fg='green'
                )
                messagebox.showinfo(
                    "No Updates",
                    f"You are using the latest version ({APP_VERSION})"
                )
                
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg='red')
            messagebox.showerror("Error", f"Failed to check for updates:\n{e}")
    
    # Manual check button
    check_btn = tk.Button(
        root,
        text="🔄 Check for Updates",
        command=manual_update_check,
        font=('Arial', 12, 'bold'),
        bg='#3498db',
        fg='white',
        padx=20,
        pady=10,
        cursor='hand2'
    )
    check_btn.pack(pady=50)
    
    root.mainloop()


# Example 3: Silent Background Check
# Kiểm tra im lặng ở background

def example_background_check():
    """Example with periodic background update check"""
    
    import threading
    import time
    
    root = tk.Tk()
    root.title("App with Background Update Check")
    root.geometry("600x400")
    
    APP_VERSION = "1.0.0"
    UPDATE_URL = "https://example.com/myapp/version.json"
    APP_NAME = "MyApp"
    
    # Notification badge
    notification_label = tk.Label(
        root,
        text="",
        font=('Arial', 10),
        fg='red'
    )
    notification_label.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)
    
    def background_update_check():
        """Check for updates in background"""
        while True:
            try:
                from auto_updater import AutoUpdater
                
                updater = AutoUpdater(APP_VERSION, UPDATE_URL, APP_NAME)
                update_info = updater.check_for_updates(silent=True)
                
                if update_info:
                    # Update UI from background thread
                    root.after(0, lambda: notification_label.config(
                        text=f"🔴 Update available: v{update_info['version']}"
                    ))
                else:
                    root.after(0, lambda: notification_label.config(text=""))
                    
            except Exception as e:
                print(f"Background check error: {e}")
            
            # Check every hour
            time.sleep(3600)
    
    # Start background thread
    update_thread = threading.Thread(target=background_update_check, daemon=True)
    update_thread.start()
    
    # Initial check after 2 seconds
    def initial_check():
        try:
            from auto_updater import check_and_prompt_update
            check_and_prompt_update(root, APP_VERSION, UPDATE_URL, APP_NAME)
        except:
            pass
    
    root.after(2000, initial_check)
    
    # Main content
    tk.Label(
        root,
        text=f"App running v{APP_VERSION}\nBackground update check enabled",
        font=('Arial', 14)
    ).pack(expand=True)
    
    root.mainloop()


# Example 4: Integration with Existing App
# Tích hợp vào app có sẵn

class ExistingApp:
    """Example of existing app with auto-update added"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Existing App + Auto-Update")
        self.root.geometry("800x600")
        
        # App config
        self.APP_VERSION = "1.0.0"
        self.APP_NAME = "ExistingApp"
        self.UPDATE_URL = "https://example.com/app/version.json"
        
        # Setup UI
        self.setup_menu()
        self.setup_ui()
        
        # Check for updates on startup
        self.root.after(1500, self.auto_check_update)
    
    def setup_menu(self):
        """Setup menu bar with update option"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        help_menu.add_command(
            label="Check for Updates",
            command=self.check_update_manual
        )
        help_menu.add_separator()
        help_menu.add_command(
            label="About",
            command=self.show_about
        )
    
    def setup_ui(self):
        """Setup main UI"""
        # Title
        title = tk.Label(
            self.root,
            text=f"{self.APP_NAME} v{self.APP_VERSION}",
            font=('Arial', 20, 'bold')
        )
        title.pack(pady=30)
        
        # Your app content here
        content = tk.Label(
            self.root,
            text="Your app content goes here...",
            font=('Arial', 12)
        )
        content.pack(pady=50)
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            anchor=tk.W,
            relief=tk.SUNKEN
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def auto_check_update(self):
        """Automatically check for updates"""
        try:
            from auto_updater import check_and_prompt_update
            
            self.status_bar.config(text="Checking for updates...")
            
            found_update = check_and_prompt_update(
                parent_window=self.root,
                current_version=self.APP_VERSION,
                update_url=self.UPDATE_URL,
                app_name=self.APP_NAME
            )
            
            if not found_update:
                self.status_bar.config(text="Ready | Up to date")
                
        except Exception as e:
            self.status_bar.config(text=f"Ready | Update check failed")
            print(f"Auto-update check error: {e}")
    
    def check_update_manual(self):
        """Manual update check from menu"""
        try:
            from auto_updater import AutoUpdater, UpdaterGUI
            
            updater = AutoUpdater(
                self.APP_VERSION,
                self.UPDATE_URL,
                self.APP_NAME
            )
            
            self.status_bar.config(text="Checking for updates...")
            self.root.update()
            
            update_info = updater.check_for_updates(silent=False)
            
            if update_info:
                UpdaterGUI(self.root, updater, update_info)
                self.status_bar.config(text="Update available")
            else:
                messagebox.showinfo(
                    "No Updates",
                    f"You are using the latest version.\n\nVersion: {self.APP_VERSION}"
                )
                self.status_bar.config(text="Ready | Up to date")
                
        except Exception as e:
            messagebox.showerror(
                "Update Check Failed",
                f"Could not check for updates:\n\n{e}"
            )
            self.status_bar.config(text="Ready | Update check failed")
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About",
            f"{self.APP_NAME}\n"
            f"Version: {self.APP_VERSION}\n\n"
            f"Auto-update enabled\n"
            f"Update URL: {self.UPDATE_URL}"
        )


# Example 5: Using update_config.py
# Sử dụng file config tự động

def example_with_config():
    """Example using auto-generated update_config.py"""
    
    root = tk.Tk()
    root.title("App with Update Config")
    
    try:
        # Import config created by build_msi_gui
        from update_config import UPDATE_URL, APP_VERSION, APP_NAME
        
        root.title(f"{APP_NAME} v{APP_VERSION}")
        
        # Check for updates
        def check_updates():
            from auto_updater import check_and_prompt_update
            check_and_prompt_update(root, APP_VERSION, UPDATE_URL, APP_NAME)
        
        root.after(1000, check_updates)
        
        tk.Label(
            root,
            text=f"Configuration loaded:\n\n"
                 f"App: {APP_NAME}\n"
                 f"Version: {APP_VERSION}\n"
                 f"Update URL: {UPDATE_URL}",
            font=('Arial', 10),
            justify=tk.LEFT
        ).pack(pady=50, padx=30)
        
    except ImportError:
        tk.Label(
            root,
            text="⚠ update_config.py not found\n\n"
                 "Build with auto-update enabled\n"
                 "in build_msi_gui.py",
            font=('Arial', 12),
            fg='orange'
        ).pack(pady=50)
    
    root.mainloop()


# Run examples
if __name__ == "__main__":
    import sys
    
    print("\n" + "="*60)
    print("Auto-Update Integration Examples")
    print("="*60)
    print("\nSelect example to run:")
    print("1. Basic Integration")
    print("2. Manual Update Check")
    print("3. Background Update Check")
    print("4. Existing App Integration")
    print("5. Using update_config.py")
    print("\n0. Exit")
    print("="*60)
    
    choice = input("\nEnter choice (0-5): ").strip()
    
    if choice == "1":
        print("\n▶ Running Basic Integration Example...")
        example_basic_app()
    elif choice == "2":
        print("\n▶ Running Manual Check Example...")
        example_manual_check()
    elif choice == "3":
        print("\n▶ Running Background Check Example...")
        example_background_check()
    elif choice == "4":
        print("\n▶ Running Existing App Integration Example...")
        root = tk.Tk()
        app = ExistingApp(root)
        root.mainloop()
    elif choice == "5":
        print("\n▶ Running Config-based Example...")
        example_with_config()
    elif choice == "0":
        print("\n👋 Goodbye!")
        sys.exit(0)
    else:
        print("\n❌ Invalid choice!")
        sys.exit(1)
