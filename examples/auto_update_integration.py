#!/usr/bin/env python3
"""
Auto-Update Integration Example

This example shows how to add auto-update functionality to your Tkinter application.
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from auto_updater import check_and_prompt_update, AutoUpdater


def example_1_simple_integration():
    """Example 1: One-line integration (easiest)"""
    print("Example 1: Simple one-line integration")
    print("-" * 50)
    
    root = tk.Tk()
    root.title("My App with Auto-Update")
    root.geometry("400x300")
    
    # Add your app content
    tk.Label(root, text="My Application", font=("Arial", 16, "bold")).pack(pady=20)
    tk.Label(root, text="Version 1.0.0").pack()
    tk.Button(root, text="Do Something", command=lambda: print("Button clicked")).pack(pady=20)
    
    # ONE LINE: Check for updates on startup
    check_and_prompt_update(
        root,
        current_version="1.0.0",
        update_url="https://raw.githubusercontent.com/user/repo/main/version.json",
        app_name="MyApp"
    )
    
    root.mainloop()
    print("✅ App closed\n")


def example_2_manual_check():
    """Example 2: Manual update check button"""
    print("Example 2: Manual update check")
    print("-" * 50)
    
    class MyApp(tk.Tk):
        def __init__(self):
            super().__init__()
            
            self.title("My App - Manual Updates")
            self.geometry("400x300")
            
            # App version
            self.version = "1.0.0"
            self.update_url = "https://raw.githubusercontent.com/user/repo/main/version.json"
            
            # UI
            tk.Label(self, text="My Application", font=("Arial", 16, "bold")).pack(pady=20)
            tk.Label(self, text=f"Version {self.version}").pack()
            
            # Manual update button
            tk.Button(
                self,
                text="Check for Updates",
                command=self.check_updates,
                bg="#4CAF50",
                fg="white",
                font=("Arial", 10, "bold")
            ).pack(pady=20)
            
            tk.Button(self, text="Quit", command=self.quit).pack()
        
        def check_updates(self):
            """Check for updates manually"""
            try:
                updater = AutoUpdater(self.version, self.update_url, "MyApp")
                update_info = updater.check_for_updates()
                
                if update_info:
                    message = f"New version {update_info['version']} is available!\n\n"
                    message += update_info.get('changelog', 'No changelog available')
                    
                    if messagebox.askyesno("Update Available", message + "\n\nUpdate now?"):
                        self.perform_update(updater, update_info)
                else:
                    messagebox.showinfo("No Updates", "You're running the latest version!")
            
            except Exception as e:
                messagebox.showerror("Update Check Failed", f"Error: {e}")
        
        def perform_update(self, updater, update_info):
            """Download and apply update"""
            try:
                # Download
                zip_path = updater.download_update(update_info['download_url'])
                
                # Verify
                if updater.verify_checksum(zip_path, update_info['checksum']):
                    # Apply
                    if updater.apply_update(zip_path):
                        messagebox.showinfo("Update Complete", "Update installed! Restart the app.")
                        self.quit()
                    else:
                        messagebox.showerror("Update Failed", "Failed to apply update")
                else:
                    messagebox.showerror("Update Failed", "Checksum verification failed")
            
            except Exception as e:
                messagebox.showerror("Update Error", f"Error: {e}")
    
    app = MyApp()
    app.mainloop()
    print("✅ App closed\n")


def example_3_background_check():
    """Example 3: Background update check (non-blocking)"""
    print("Example 3: Background update check")
    print("-" * 50)
    
    import threading
    
    class MyAppWithBackground(tk.Tk):
        def __init__(self):
            super().__init__()
            
            self.title("My App - Background Updates")
            self.geometry("400x300")
            
            self.version = "1.0.0"
            self.update_url = "https://raw.githubusercontent.com/user/repo/main/version.json"
            
            # UI
            tk.Label(self, text="My Application", font=("Arial", 16, "bold")).pack(pady=20)
            tk.Label(self, text=f"Version {self.version}").pack()
            
            self.status_label = tk.Label(self, text="Checking for updates...", fg="gray")
            self.status_label.pack(pady=20)
            
            # Start background check
            self.check_updates_background()
        
        def check_updates_background(self):
            """Check for updates in background thread"""
            def worker():
                try:
                    updater = AutoUpdater(self.version, self.update_url, "MyApp")
                    update_info = updater.check_for_updates()
                    
                    # Update UI in main thread
                    self.after(0, self.on_update_check_complete, update_info)
                except Exception as e:
                    self.after(0, self.on_update_check_error, str(e))
            
            thread = threading.Thread(target=worker, daemon=True)
            thread.start()
        
        def on_update_check_complete(self, update_info):
            """Called when update check completes"""
            if update_info:
                self.status_label.config(
                    text=f"Update available: v{update_info['version']}",
                    fg="green"
                )
                
                tk.Button(
                    self,
                    text="View Update",
                    command=lambda: self.show_update_details(update_info)
                ).pack()
            else:
                self.status_label.config(text="Up to date ✓", fg="green")
        
        def on_update_check_error(self, error):
            """Called if update check fails"""
            self.status_label.config(text=f"Update check failed", fg="red")
            print(f"Error: {error}")
        
        def show_update_details(self, update_info):
            """Show update dialog"""
            message = f"Version {update_info['version']} is available!\n\n"
            message += update_info.get('changelog', 'No changelog')
            messagebox.showinfo("Update Available", message)
    
    app = MyAppWithBackground()
    app.mainloop()
    print("✅ App closed\n")


def example_4_auto_update_config():
    """Example 4: Using auto-generated config"""
    print("Example 4: Using auto_update_helper")
    print("-" * 50)
    
    # If you used auto_update_helper to generate update_config.py
    # you can import it directly
    
    try:
        # Try to import generated config
        sys.path.insert(0, '.')
        from update_config import UPDATE_URL, CURRENT_VERSION, APP_NAME
        
        root = tk.Tk()
        root.title(f"{APP_NAME} - Auto Config")
        root.geometry("400x300")
        
        tk.Label(root, text=APP_NAME, font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(root, text=f"Version {CURRENT_VERSION}").pack()
        
        # Use config values
        check_and_prompt_update(
            root,
            current_version=CURRENT_VERSION,
            update_url=UPDATE_URL,
            app_name=APP_NAME
        )
        
        root.mainloop()
        print("✅ App closed\n")
    
    except ImportError:
        print("⚠️  update_config.py not found")
        print("   Run auto_update_helper.py first to generate it")
        print()


def example_5_custom_ui():
    """Example 5: Custom update notification UI"""
    print("Example 5: Custom update UI")
    print("-" * 50)
    
    class CustomUpdateDialog(tk.Toplevel):
        def __init__(self, parent, update_info):
            super().__init__(parent)
            
            self.title("Update Available")
            self.geometry("500x400")
            self.resizable(False, False)
            
            # Header
            header_frame = tk.Frame(self, bg="#4CAF50", height=80)
            header_frame.pack(fill=tk.X)
            header_frame.pack_propagate(False)
            
            tk.Label(
                header_frame,
                text=f"🎉 Version {update_info['version']} Available!",
                font=("Arial", 14, "bold"),
                bg="#4CAF50",
                fg="white"
            ).pack(expand=True)
            
            # Changelog
            tk.Label(self, text="What's New:", font=("Arial", 11, "bold")).pack(anchor=tk.W, padx=20, pady=(20, 5))
            
            changelog_text = tk.Text(self, height=10, wrap=tk.WORD, bg="#f5f5f5")
            changelog_text.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
            changelog_text.insert('1.0', update_info.get('changelog', 'No details available'))
            changelog_text.config(state='disabled')
            
            # Buttons
            button_frame = tk.Frame(self)
            button_frame.pack(pady=20)
            
            tk.Button(
                button_frame,
                text="Update Now",
                command=self.update_now,
                bg="#4CAF50",
                fg="white",
                font=("Arial", 10, "bold"),
                width=15
            ).pack(side=tk.LEFT, padx=5)
            
            tk.Button(
                button_frame,
                text="Later",
                command=self.destroy,
                width=15
            ).pack(side=tk.LEFT, padx=5)
        
        def update_now(self):
            print("✅ User clicked Update Now")
            self.destroy()
    
    # Demo
    root = tk.Tk()
    root.title("My App")
    root.geometry("400x300")
    
    tk.Label(root, text="My Application", font=("Arial", 16, "bold")).pack(pady=20)
    
    # Simulate update available
    demo_update = {
        'version': '1.1.0',
        'changelog': '• Fixed bug in image converter\n• Added dark mode\n• Improved performance\n• Updated dependencies'
    }
    
    tk.Button(
        root,
        text="Show Update Dialog (Demo)",
        command=lambda: CustomUpdateDialog(root, demo_update)
    ).pack(pady=20)
    
    root.mainloop()
    print("✅ App closed\n")


if __name__ == "__main__":
    print("=" * 50)
    print("Auto-Update Integration Examples")
    print("=" * 50)
    print()
    print("Choose an example to run:")
    print("1. Simple one-line integration")
    print("2. Manual update check button")
    print("3. Background update check")
    print("4. Using auto-generated config")
    print("5. Custom update UI")
    print()
    
    choice = input("Enter number (1-5) or 'all': ").strip()
    
    if choice == '1':
        example_1_simple_integration()
    elif choice == '2':
        example_2_manual_check()
    elif choice == '3':
        example_3_background_check()
    elif choice == '4':
        example_4_auto_update_config()
    elif choice == '5':
        example_5_custom_ui()
    elif choice.lower() == 'all':
        print("Running all examples...")
        print("Close each window to see the next example\n")
        example_1_simple_integration()
        example_2_manual_check()
        example_3_background_check()
        example_4_auto_update_config()
        example_5_custom_ui()
    else:
        print("Invalid choice. Please run again and select 1-5 or 'all'")
    
    print("=" * 50)
    print("Examples complete!")
    print("=" * 50)
