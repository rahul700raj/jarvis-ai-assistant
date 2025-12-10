#!/usr/bin/env python3
"""
JARVIS AI Assistant - Automated Installer
This script automates the installation process for JARVIS
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path

class JarvisInstaller:
    def __init__(self):
        self.system = platform.system()
        self.python_version = sys.version_info
        
    def print_header(self):
        print("""
        ╔═══════════════════════════════════════════╗
        ║   JARVIS AI Assistant - Installer        ║
        ║   Advanced Voice-Activated AI             ║
        ╚═══════════════════════════════════════════╝
        """)
        
    def check_python_version(self):
        print("🔍 Checking Python version...")
        if self.python_version < (3, 8):
            print("❌ Python 3.8 or higher is required!")
            print(f"   Current version: {sys.version}")
            sys.exit(1)
        print(f"✅ Python {self.python_version.major}.{self.python_version.minor} detected")
        
    def install_system_dependencies(self):
        print("\n📦 Installing system dependencies...")
        
        if self.system == "Linux":
            print("   Detected Linux system")
            try:
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install", "-y", 
                              "portaudio19-dev", "python3-pyaudio", "espeak", "ffmpeg"], 
                              check=True)
                print("✅ System dependencies installed")
            except subprocess.CalledProcessError:
                print("⚠️  Could not install system dependencies. Please install manually:")
                print("   sudo apt-get install portaudio19-dev python3-pyaudio espeak ffmpeg")
                
        elif self.system == "Darwin":  # macOS
            print("   Detected macOS system")
            try:
                subprocess.run(["brew", "install", "portaudio", "espeak", "ffmpeg"], check=True)
                print("✅ System dependencies installed")
            except subprocess.CalledProcessError:
                print("⚠️  Could not install system dependencies. Please install Homebrew first:")
                print("   /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
                
        elif self.system == "Windows":
            print("   Detected Windows system")
            print("✅ Windows dependencies will be installed with pip")
        
    def install_python_packages(self):
        print("\n📚 Installing Python packages...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                          check=True)
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                          check=True)
            print("✅ Python packages installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing packages: {e}")
            sys.exit(1)
            
    def create_config(self):
        print("\n⚙️  Creating configuration file...")
        
        config_template = {
            "openai_api_key": "",
            "wake_word": "hey jarvis",
            "voice_engine": "pyttsx3",
            "speech_rate": 150,
            "volume": 0.9,
            "language": "en-US",
            "timeout": 5,
            "phrase_time_limit": 10
        }
        
        config_path = Path("config.json")
        
        if config_path.exists():
            print("⚠️  config.json already exists. Skipping...")
        else:
            with open(config_path, 'w') as f:
                json.dump(config_template, f, indent=4)
            print("✅ Configuration file created: config.json")
            print("\n⚠️  IMPORTANT: Edit config.json and add your OpenAI API key!")
            
    def create_directories(self):
        print("\n📁 Creating project directories...")
        directories = ['modules', 'utils', 'plugins', 'logs']
        
        for directory in directories:
            Path(directory).mkdir(exist_ok=True)
            
        print("✅ Directories created")
        
    def run_installation(self):
        self.print_header()
        self.check_python_version()
        self.create_directories()
        self.install_system_dependencies()
        self.install_python_packages()
        self.create_config()
        
        print("""
        ╔═══════════════════════════════════════════╗
        ║   ✅ Installation Complete!               ║
        ╚═══════════════════════════════════════════╝
        
        📝 Next Steps:
        
        1. Get your OpenAI API key from: https://platform.openai.com
        2. Edit config.json and add your API key
        3. Run JARVIS: python jarvis.py
        
        🎤 Say "Hey JARVIS" to activate!
        
        For help: https://github.com/rahul700raj/jarvis-ai-assistant
        """)

if __name__ == "__main__":
    installer = JarvisInstaller()
    try:
        installer.run_installation()
    except KeyboardInterrupt:
        print("\n\n❌ Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Installation failed: {e}")
        sys.exit(1)
