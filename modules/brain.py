"""
AI Brain Module
Handles intelligent responses using OpenAI
"""

from openai import OpenAI

class AIBrain:
    def __init__(self, config):
        self.config = config
        api_key = config.get('openai_api_key')
        
        if api_key:
            self.client = OpenAI(api_key=api_key)
            self.enabled = True
        else:
            self.enabled = False
            print("⚠️  OpenAI API key not configured. AI features disabled.")
            
        self.conversation_history = []
        
    def get_response(self, query):
        """Get AI-powered response to user query"""
        if not self.enabled:
            return "I apologize, but my AI capabilities are not configured. Please add an OpenAI API key."
            
        try:
            # Add user message to history
            self.conversation_history.append({
                "role": "user",
                "content": query
            })
            
            # Create system message
            system_message = {
                "role": "system",
                "content": """You are JARVIS, an advanced AI assistant inspired by Iron Man's AI. 
                You are helpful, intelligent, and slightly formal. Address the user as 'sir' occasionally.
                Keep responses concise and natural for voice interaction. Be witty when appropriate."""
            }
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[system_message] + self.conversation_history[-10:],  # Keep last 10 messages
                max_tokens=150,
                temperature=0.7
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return "I apologize, sir. I'm having trouble processing that request at the moment."
            
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
