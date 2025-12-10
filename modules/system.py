"""
System Controller Module
Handles system-level operations and controls
"""

import os
import platform
import subprocess
import webbrowser

class SystemController:
    def __init__(self):
        self.system = platform.system()
        
    def open_application(self, app_name):
        """Open an application by name"""
        app_name = app_name.lower().strip()
        
        try:
            if self.system == "Windows":
                # Common Windows applications
                apps = {
                    'notepad': 'notepad.exe',
                    'calculator': 'calc.exe',
                    'paint': 'mspaint.exe',
                    'chrome': 'chrome.exe',
                    'firefox': 'firefox.exe',
                    'edge': 'msedge.exe',
                    'explorer': 'explorer.exe',
                    'cmd': 'cmd.exe',
                    'powershell': 'powershell.exe'
                }
                
                if app_name in apps:
                    os.startfile(apps[app_name])
                    return True
                    
            elif self.system == "Darwin":  # macOS
                apps = {
                    'safari': 'Safari',
                    'chrome': 'Google Chrome',
                    'firefox': 'Firefox',
                    'terminal': 'Terminal',
                    'finder': 'Finder',
                    'notes': 'Notes',
                    'calculator': 'Calculator'
                }
                
                if app_name in apps:
                    subprocess.run(['open', '-a', apps[app_name]])
                    return True
                    
            elif self.system == "Linux":
                # Try to open with xdg-open
                subprocess.run(['xdg-open', app_name])
                return True
                
            # Try opening as URL for websites
            if any(site in app_name for site in ['youtube', 'google', 'facebook', 'twitter', 'github']):
                url = f"https://www.{app_name}.com"
                webbrowser.open(url)
                return True
                
            return False
            
        except Exception as e:
            print(f"Error opening application: {e}")
            return False
            
    def volume_up(self):
        """Increase system volume"""
        try:
            if self.system == "Windows":
                from ctypes import cast, POINTER
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                current = volume.GetMasterVolumeLevelScalar()
                volume.SetMasterVolumeLevelScalar(min(1.0, current + 0.1), None)
                
            elif self.system == "Darwin":
                subprocess.run(['osascript', '-e', 'set volume output volume (output volume of (get volume settings) + 10)'])
                
            elif self.system == "Linux":
                subprocess.run(['amixer', 'set', 'Master', '10%+'])
                
            return True
        except:
            return False
            
    def volume_down(self):
        """Decrease system volume"""
        try:
            if self.system == "Windows":
                from ctypes import cast, POINTER
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                current = volume.GetMasterVolumeLevelScalar()
                volume.SetMasterVolumeLevelScalar(max(0.0, current - 0.1), None)
                
            elif self.system == "Darwin":
                subprocess.run(['osascript', '-e', 'set volume output volume (output volume of (get volume settings) - 10)'])
                
            elif self.system == "Linux":
                subprocess.run(['amixer', 'set', 'Master', '10%-'])
                
            return True
        except:
            return False
