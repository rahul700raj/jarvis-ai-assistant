"""
Speech Recognition Module
Handles voice input and speech-to-text conversion
"""

import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self, config):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.config = config
        
        # Adjust for ambient noise
        with self.microphone as source:
            print("🎤 Calibrating microphone for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Microphone ready")
            
    def listen(self, timeout=5, phrase_time_limit=10):
        """Listen for audio input"""
        try:
            with self.microphone as source:
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                return audio
        except sr.WaitTimeoutError:
            return None
        except Exception as e:
            print(f"Error listening: {e}")
            return None
            
    def recognize(self, audio):
        """Convert audio to text"""
        if not audio:
            return None
            
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            return None
