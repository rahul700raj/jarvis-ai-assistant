"""
Voice Engine Module
Handles text-to-speech conversion
"""

import pyttsx3

class VoiceEngine:
    def __init__(self, config):
        self.engine = pyttsx3.init()
        self.config = config
        
        # Configure voice properties
        rate = config.get('speech_rate', 150)
        volume = config.get('volume', 0.9)
        
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Try to set a male voice
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'male' in voice.name.lower() and 'female' not in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
                
    def speak(self, text):
        """Convert text to speech"""
        print(f"🤖 JARVIS: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error speaking: {e}")
            
    def stop(self):
        """Stop speaking"""
        try:
            self.engine.stop()
        except:
            pass
