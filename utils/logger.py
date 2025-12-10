"""
Logger Utility
Handles logging for JARVIS
"""

import os
from datetime import datetime
from pathlib import Path

class Logger:
    def __init__(self):
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        
        self.log_file = self.log_dir / f"jarvis_{datetime.now().strftime('%Y%m%d')}.log"
        
    def log(self, message, level="INFO"):
        """Log a message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error writing to log: {e}")
            
    def error(self, message):
        """Log an error"""
        self.log(message, "ERROR")
        
    def warning(self, message):
        """Log a warning"""
        self.log(message, "WARNING")
        
    def info(self, message):
        """Log info"""
        self.log(message, "INFO")
