"""
Helper Utilities
Common helper functions for JARVIS
"""

import json
from pathlib import Path

def load_config():
    """Load configuration from config.json"""
    config_path = Path("config.json")
    
    if not config_path.exists():
        print("⚠️  config.json not found. Using default configuration.")
        return {
            "openai_api_key": "",
            "wake_word": "hey jarvis",
            "voice_engine": "pyttsx3",
            "speech_rate": 150,
            "volume": 0.9
        }
        
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}
        
def save_config(config):
    """Save configuration to config.json"""
    try:
        with open("config.json", 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False
