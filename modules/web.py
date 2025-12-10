"""
Web Automation Module
Handles web browsing and search operations
"""

import webbrowser
import requests

class WebAutomation:
    def __init__(self):
        pass
        
    def search(self, query):
        """Perform a web search"""
        try:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            return True
        except Exception as e:
            print(f"Error performing search: {e}")
            return False
            
    def open_url(self, url):
        """Open a URL in the default browser"""
        try:
            if not url.startswith('http'):
                url = 'https://' + url
            webbrowser.open(url)
            return True
        except Exception as e:
            print(f"Error opening URL: {e}")
            return False
            
    def youtube_search(self, query):
        """Search YouTube"""
        try:
            url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            webbrowser.open(url)
            return True
        except Exception as e:
            print(f"Error searching YouTube: {e}")
            return False
