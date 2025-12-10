#!/usr/bin/env python3
"""
JARVIS AI Assistant - Main Application
Advanced voice-activated AI assistant for PC
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime

# Import modules
from modules.speech import SpeechRecognizer
from modules.voice import VoiceEngine
from modules.brain import AIBrain
from modules.system import SystemController
from modules.web import WebAutomation
from utils.logger import Logger
from utils.helpers import load_config

class JARVIS:
    def __init__(self):
        self.logger = Logger()
        self.config = load_config()
        
        # Initialize components
        self.speech = SpeechRecognizer(self.config)
        self.voice = VoiceEngine(self.config)
        self.brain = AIBrain(self.config)
        self.system = SystemController()
        self.web = WebAutomation()
        
        self.wake_word = self.config.get('wake_word', 'hey jarvis').lower()
        self.running = False
        
    def greet(self):
        """Greet the user based on time of day"""
        hour = datetime.now().hour
        
        if hour < 12:
            greeting = "Good morning, sir."
        elif hour < 18:
            greeting = "Good afternoon, sir."
        else:
            greeting = "Good evening, sir."
            
        self.voice.speak(f"{greeting} JARVIS at your service. How may I assist you today?")
        
    def process_command(self, command):
        """Process user command and execute appropriate action"""
        command = command.lower()
        
        # Exit commands
        if any(word in command for word in ['exit', 'goodbye', 'quit', 'stop']):
            self.voice.speak("Goodbye, sir. It was a pleasure serving you.")
            self.running = False
            return
            
        # Time query
        if 'time' in command:
            current_time = datetime.now().strftime("%I:%M %p")
            self.voice.speak(f"The current time is {current_time}")
            return
            
        # Date query
        if 'date' in command:
            current_date = datetime.now().strftime("%B %d, %Y")
            self.voice.speak(f"Today is {current_date}")
            return
            
        # Open applications
        if 'open' in command:
            app = command.replace('open', '').strip()
            if self.system.open_application(app):
                self.voice.speak(f"Opening {app}, sir.")
            else:
                self.voice.speak(f"I couldn't open {app}. Please check if it's installed.")
            return
            
        # Web search
        if 'search' in command or 'google' in command:
            query = command.replace('search', '').replace('google', '').replace('for', '').strip()
            self.web.search(query)
            self.voice.speak(f"Here are the search results for {query}")
            return
            
        # System controls
        if 'volume' in command:
            if 'up' in command or 'increase' in command:
                self.system.volume_up()
                self.voice.speak("Volume increased")
            elif 'down' in command or 'decrease' in command:
                self.system.volume_down()
                self.voice.speak("Volume decreased")
            return
            
        # AI-powered response for everything else
        try:
            response = self.brain.get_response(command)
            self.voice.speak(response)
        except Exception as e:
            self.logger.error(f"Error processing command: {e}")
            self.voice.speak("I apologize, sir. I encountered an error processing your request.")
            
    def listen_for_wake_word(self):
        """Listen for wake word activation"""
        print(f"🎤 Listening for wake word: '{self.wake_word}'...")
        
        while self.running:
            try:
                audio = self.speech.listen(timeout=3)
                if audio:
                    text = self.speech.recognize(audio)
                    if text and self.wake_word in text.lower():
                        self.voice.speak("Yes, sir?")
                        return True
            except Exception as e:
                continue
                
        return False
        
    def listen_for_command(self):
        """Listen for user command after wake word"""
        print("🎤 Listening for command...")
        
        try:
            audio = self.speech.listen(timeout=5)
            if audio:
                command = self.speech.recognize(audio)
                if command:
                    print(f"📝 You said: {command}")
                    self.logger.log(f"Command: {command}")
                    return command
        except Exception as e:
            self.logger.error(f"Error listening for command: {e}")
            
        return None
        
    def run(self):
        """Main application loop"""
        print("""
        ╔═══════════════════════════════════════════╗
        ║        JARVIS AI Assistant v1.0           ║
        ║     Advanced Voice-Activated AI           ║
        ╚═══════════════════════════════════════════╝
        """)
        
        # Check API key
        if not self.config.get('openai_api_key'):
            print("❌ Error: OpenAI API key not found in config.json")
            print("Please add your API key to config.json")
            return
            
        self.running = True
        self.greet()
        
        try:
            while self.running:
                # Listen for wake word
                if self.listen_for_wake_word():
                    # Listen for command
                    command = self.listen_for_command()
                    
                    if command:
                        self.process_command(command)
                    else:
                        self.voice.speak("I didn't catch that, sir. Could you repeat?")
                        
        except KeyboardInterrupt:
            print("\n\n👋 JARVIS shutting down...")
            self.voice.speak("Shutting down. Goodbye, sir.")
        except Exception as e:
            self.logger.error(f"Fatal error: {e}")
            print(f"❌ Fatal error: {e}")
            
def main():
    jarvis = JARVIS()
    jarvis.run()

if __name__ == "__main__":
    main()
