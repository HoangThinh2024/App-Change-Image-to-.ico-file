#!/usr/bin/env python3
"""
Auto-Updater Module
Module tự động cập nhật ứng dụng mà không cần cài đặt lại
"""

import os
import sys
import json
import hashlib
import shutil
import tempfile
import zipfile
import requests
from pathlib import Path
from packaging import version
import tkinter as tk
from tkinter import messagebox, ttk


class AutoUpdater:
    """
    Auto-updater class with version checking and update downloading
    """
    
    def __init__(self, current_version, update_url=None, app_name="MyApp"):
        """
        Initialize updater
        
        Args:
            current_version: Current app version (e.g., "1.0.0")
            update_url: URL to version.json file or GitHub API endpoint
            app_name: Application name
        """
        self.current_version = current_version
        self.update_url = update_url
        self.app_name = app_name
        self.app_dir = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path.cwd()
        self.temp_dir = Path(tempfile.gettempdir()) / f"{app_name}_update"
        
        # Default update server file
        self.version_file = "version.json"
        
    def check_for_updates(self, silent=False):
        """
        Check if new version is available
        
        Args:
            silent: If True, don't show message if no update
            
        Returns:
            dict: Update info if available, None otherwise
        """
        if not self.update_url:
            if not silent:
                print("⚠ Update URL không được cấu hình")
            return None
        
        try:
            # Download version info
            response = requests.get(self.update_url, timeout=10)
            response.raise_for_status()
            
            version_info = response.json()
            latest_version = version_info.get('version')
            
            if not latest_version:
                if not silent:
                    print("⚠ Không tìm thấy thông tin phiên bản")
                return None
            
            # Compare versions
            if version.parse(latest_version) > version.parse(self.current_version):
                print(f"✓ Phát hiện phiên bản mới: {latest_version} (hiện tại: {self.current_version})")
                return version_info
            else:
                if not silent:
                    print(f"✓ Bạn đang dùng phiên bản mới nhất: {self.current_version}")
                return None
                
        except requests.RequestException as e:
            if not silent:
                print(f"❌ Lỗi khi kiểm tra cập nhật: {e}")
            return None
        except Exception as e:
            if not silent:
                print(f"❌ Lỗi: {e}")
            return None
    
    def download_update(self, download_url, progress_callback=None):
        """
        Download update file
        
        Args:
            download_url: URL to download update
            progress_callback: Callback function for progress (percent)
            
        Returns:
            Path: Downloaded file path or None
        """
        try:
            # Create temp directory
            self.temp_dir.mkdir(parents=True, exist_ok=True)
            
            # Download file
            response = requests.get(download_url, stream=True, timeout=30)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            
            # Determine filename
            filename = download_url.split('/')[-1]
            if not filename.endswith(('.zip', '.exe', '.msi')):
                filename = 'update.zip'
            
            download_path = self.temp_dir / filename
            
            # Download with progress
            with open(download_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        if progress_callback and total_size > 0:
                            percent = int((downloaded / total_size) * 100)
                            progress_callback(percent)
            
            print(f"✓ Đã tải về: {download_path}")
            return download_path
            
        except Exception as e:
            print(f"❌ Lỗi khi tải file: {e}")
            return None
    
    def verify_checksum(self, file_path, expected_hash):
        """
        Verify file integrity with checksum
        
        Args:
            file_path: Path to file
            expected_hash: Expected SHA256 hash
            
        Returns:
            bool: True if valid
        """
        try:
            sha256_hash = hashlib.sha256()
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            
            file_hash = sha256_hash.hexdigest()
            is_valid = file_hash == expected_hash
            
            if is_valid:
                print("✓ Checksum hợp lệ")
            else:
                print(f"❌ Checksum không khớp!\n   Mong đợi: {expected_hash}\n   Nhận được: {file_hash}")
            
            return is_valid
            
        except Exception as e:
            print(f"❌ Lỗi khi kiểm tra checksum: {e}")
            return False
    
    def extract_update(self, zip_path, extract_to=None):
        """
        Extract update package
        
        Args:
            zip_path: Path to zip file
            extract_to: Destination directory (default: temp)
            
        Returns:
            Path: Extracted directory or None
        """
        if extract_to is None:
            extract_to = self.temp_dir / "extracted"
        
        try:
            extract_to.mkdir(parents=True, exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            
            print(f"✓ Đã giải nén vào: {extract_to}")
            return extract_to
            
        except Exception as e:
            print(f"❌ Lỗi khi giải nén: {e}")
            return None
    
    def apply_update(self, update_dir):
        """
        Apply update by copying files
        
        Args:
            update_dir: Directory containing update files
            
        Returns:
            bool: Success status
        """
        try:
            # Backup current version
            backup_dir = self.app_dir.parent / f"{self.app_name}_backup"
            if backup_dir.exists():
                shutil.rmtree(backup_dir)
            
            print("📦 Đang sao lưu phiên bản hiện tại...")
            shutil.copytree(self.app_dir, backup_dir)
            
            # Copy new files
            print("📥 Đang cài đặt cập nhật...")
            for item in update_dir.rglob('*'):
                if item.is_file():
                    rel_path = item.relative_to(update_dir)
                    dest_path = self.app_dir / rel_path
                    
                    # Create parent directories
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Copy file
                    shutil.copy2(item, dest_path)
                    print(f"   ✓ Đã cập nhật: {rel_path}")
            
            print("✓ Cập nhật thành công!")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi khi cài đặt: {e}")
            
            # Restore backup
            if backup_dir.exists():
                print("🔄 Đang khôi phục từ backup...")
                try:
                    shutil.rmtree(self.app_dir)
                    shutil.copytree(backup_dir, self.app_dir)
                    print("✓ Đã khôi phục phiên bản cũ")
                except Exception as restore_error:
                    print(f"❌ Lỗi khi khôi phục: {restore_error}")
            
            return False
    
    def cleanup(self):
        """Clean up temporary files"""
        try:
            if self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                print("✓ Đã dọn dẹp file tạm")
        except Exception as e:
            print(f"⚠ Không thể dọn dẹp: {e}")
    
    def run_update(self, update_info, progress_callback=None):
        """
        Run complete update process
        
        Args:
            update_info: Update information dict
            progress_callback: Progress callback function
            
        Returns:
            bool: Success status
        """
        try:
            download_url = update_info.get('download_url')
            checksum = update_info.get('checksum')
            
            if not download_url:
                print("❌ Thiếu URL tải về")
                return False
            
            # Step 1: Download
            if progress_callback:
                progress_callback(0, "Đang tải về...")
            
            download_path = self.download_update(download_url, 
                lambda p: progress_callback(p * 0.5, "Đang tải về...") if progress_callback else None)
            
            if not download_path:
                return False
            
            # Step 2: Verify checksum
            if checksum:
                if progress_callback:
                    progress_callback(50, "Đang kiểm tra tính toàn vẹn...")
                
                if not self.verify_checksum(download_path, checksum):
                    return False
            
            # Step 3: Extract
            if progress_callback:
                progress_callback(60, "Đang giải nén...")
            
            if download_path.suffix == '.zip':
                extract_dir = self.extract_update(download_path)
                if not extract_dir:
                    return False
            else:
                extract_dir = download_path.parent
            
            # Step 4: Apply update
            if progress_callback:
                progress_callback(80, "Đang cài đặt...")
            
            success = self.apply_update(extract_dir)
            
            # Step 5: Cleanup
            if progress_callback:
                progress_callback(95, "Đang dọn dẹp...")
            
            self.cleanup()
            
            if progress_callback:
                progress_callback(100, "Hoàn thành!")
            
            return success
            
        except Exception as e:
            print(f"❌ Lỗi trong quá trình cập nhật: {e}")
            self.cleanup()
            return False


class UpdaterGUI:
    """GUI for update process"""
    
    def __init__(self, parent, updater, update_info):
        """
        Initialize updater GUI
        
        Args:
            parent: Parent window
            updater: AutoUpdater instance
            update_info: Update information
        """
        self.parent = parent
        self.updater = updater
        self.update_info = update_info
        
        # Create dialog
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Cập nhật ứng dụng")
        self.dialog.geometry("500x300")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Center dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (300 // 2)
        self.dialog.geometry(f"500x300+{x}+{y}")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup UI"""
        # Title
        title_frame = tk.Frame(self.dialog, bg='#2c3e50', height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        tk.Label(
            title_frame,
            text="🔄 Cập nhật có sẵn",
            font=('Segoe UI', 16, 'bold'),
            bg='#2c3e50',
            fg='white'
        ).pack(pady=15)
        
        # Content
        content_frame = tk.Frame(self.dialog, bg='#f5f5f5', padx=30, pady=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Version info
        info_text = f"""Phiên bản mới: {self.update_info.get('version')}
Phiên bản hiện tại: {self.updater.current_version}

Nội dung cập nhật:
{self.update_info.get('changelog', 'Không có thông tin')}

Dung lượng: {self.update_info.get('size', 'N/A')}
"""
        
        info_label = tk.Label(
            content_frame,
            text=info_text,
            font=('Segoe UI', 10),
            bg='#f5f5f5',
            fg='#2c3e50',
            justify=tk.LEFT,
            anchor='w'
        )
        info_label.pack(fill=tk.BOTH, expand=True)
        
        # Progress bar (hidden initially)
        self.progress_frame = tk.Frame(content_frame, bg='#f5f5f5')
        
        self.progress_label = tk.Label(
            self.progress_frame,
            text="Đang chuẩn bị...",
            font=('Segoe UI', 9),
            bg='#f5f5f5',
            fg='#7f8c8d'
        )
        self.progress_label.pack()
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            mode='determinate',
            length=400
        )
        self.progress_bar.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.dialog, bg='#f5f5f5', pady=15)
        button_frame.pack(fill=tk.X)
        
        self.update_btn = tk.Button(
            button_frame,
            text="🔄 Cập nhật ngay",
            command=self.start_update,
            bg='#27ae60',
            fg='white',
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        self.update_btn.pack(side=tk.LEFT, padx=(30, 10))
        
        self.cancel_btn = tk.Button(
            button_frame,
            text="❌ Để sau",
            command=self.dialog.destroy,
            bg='#95a5a6',
            fg='white',
            font=('Segoe UI', 10, 'bold'),
            cursor='hand2',
            relief=tk.FLAT,
            padx=20,
            pady=8
        )
        self.cancel_btn.pack(side=tk.LEFT, padx=10)
    
    def update_progress(self, percent, status):
        """Update progress bar"""
        self.progress_frame.pack(pady=10)
        self.progress_bar['value'] = percent
        self.progress_label.config(text=f"{status} ({percent}%)")
        self.dialog.update_idletasks()
    
    def start_update(self):
        """Start update process"""
        self.update_btn.config(state='disabled')
        self.cancel_btn.config(state='disabled')
        
        # Run update
        success = self.updater.run_update(self.update_info, self.update_progress)
        
        if success:
            messagebox.showinfo(
                "Thành công",
                "Cập nhật thành công!\n\nỨng dụng sẽ khởi động lại.",
                parent=self.dialog
            )
            # Restart app
            self.restart_app()
        else:
            messagebox.showerror(
                "Lỗi",
                "Cập nhật thất bại!\n\nVui lòng thử lại sau.",
                parent=self.dialog
            )
            self.update_btn.config(state='normal')
            self.cancel_btn.config(state='normal')
    
    def restart_app(self):
        """Restart application"""
        try:
            python = sys.executable
            os.execl(python, python, *sys.argv)
        except Exception as e:
            print(f"❌ Không thể khởi động lại: {e}")
            self.dialog.destroy()


def check_and_prompt_update(parent_window, current_version, update_url, app_name="MyApp"):
    """
    Check for updates and show GUI if available
    
    Args:
        parent_window: Parent tkinter window
        current_version: Current app version
        update_url: Update server URL
        app_name: Application name
        
    Returns:
        bool: True if update was found
    """
    try:
        updater = AutoUpdater(current_version, update_url, app_name)
        update_info = updater.check_for_updates(silent=True)
        
        if update_info:
            UpdaterGUI(parent_window, updater, update_info)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Lỗi khi kiểm tra cập nhật: {e}")
        return False


# Example usage
if __name__ == "__main__":
    # Test updater
    updater = AutoUpdater(
        current_version="1.0.0",
        update_url="https://example.com/version.json",
        app_name="TestApp"
    )
    
    update_info = updater.check_for_updates()
    
    if update_info:
        print("\n🔄 Bắt đầu cập nhật...")
        success = updater.run_update(update_info)
        
        if success:
            print("✓ Cập nhật thành công!")
        else:
            print("❌ Cập nhật thất bại!")
    else:
        print("✓ Không có cập nhật mới")
