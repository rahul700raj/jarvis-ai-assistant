# 🤖 JARVIS AI Assistant

An advanced AI assistant inspired by JARVIS from Iron Man. This voice-activated assistant runs locally on your PC with natural language processing, system control, and automation capabilities.

## ✨ Features

- 🎤 **Voice Recognition** - Speak commands naturally
- 🔊 **Text-to-Speech** - JARVIS responds with voice
- 🧠 **AI-Powered** - Uses OpenAI GPT for intelligent responses
- 💻 **System Control** - Control your PC with voice commands
- 🌐 **Web Automation** - Search, browse, and fetch information
- ⚡ **Fast & Lightweight** - Runs efficiently on your local machine
- 🔧 **Modular Design** - Easy to extend and customize

## 🚀 Quick Installation

### Prerequisites
- Python 3.8 or higher
- Microphone for voice input
- Speakers for audio output
- OpenAI API key (get from https://platform.openai.com)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/rahul700raj/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

2. **Run the installer**
```bash
python install.py
```

3. **Configure your API key**
```bash
# Edit config.json and add your OpenAI API key
```

4. **Start JARVIS**
```bash
python jarvis.py
```

## 📋 Manual Installation

If you prefer manual setup:

```bash
# Install dependencies
pip install -r requirements.txt

# Copy config template
cp config.example.json config.json

# Edit config.json with your settings
# Run JARVIS
python jarvis.py
```

## 🎯 Usage

### Voice Commands

- **"Hey JARVIS"** - Wake word to activate
- **"What time is it?"** - Get current time
- **"Open YouTube"** - Open websites
- **"Search for Python tutorials"** - Web search
- **"What's the weather?"** - Weather information
- **"Tell me a joke"** - Entertainment
- **"Exit"** or **"Goodbye"** - Stop JARVIS

### Example Conversations

```
You: "Hey JARVIS, what's the weather today?"
JARVIS: "The current temperature is 72°F with clear skies."

You: "Open YouTube"
JARVIS: "Opening YouTube for you, sir."

You: "Search for AI news"
JARVIS: "Searching for AI news..."
```

## 🛠️ Configuration

Edit `config.json` to customize:

```json
{
  "openai_api_key": "your-api-key-here",
  "wake_word": "hey jarvis",
  "voice_engine": "pyttsx3",
  "speech_rate": 150,
  "volume": 0.9
}
```

## 📁 Project Structure

```
jarvis-ai-assistant/
├── jarvis.py              # Main application
├── install.py             # Automated installer
├── requirements.txt       # Python dependencies
├── config.example.json    # Configuration template
├── modules/
│   ├── speech.py         # Speech recognition
│   ├── voice.py          # Text-to-speech
│   ├── brain.py          # AI processing
│   ├── system.py         # System controls
│   └── web.py            # Web automation
├── utils/
│   ├── logger.py         # Logging utilities
│   └── helpers.py        # Helper functions
└── README.md
```

## 🔧 Advanced Features

### Custom Commands

Add custom commands in `modules/brain.py`:

```python
def custom_command(self, query):
    if "custom action" in query:
        # Your custom code here
        return "Custom response"
```

### Plugin System

Create plugins in `plugins/` folder for extended functionality.

## 🐛 Troubleshooting

**Microphone not working?**
- Check system permissions
- Install PyAudio: `pip install pyaudio`

**API errors?**
- Verify your OpenAI API key
- Check internet connection

**Voice not working?**
- Install espeak: `sudo apt-get install espeak` (Linux)
- Check audio output settings

## 📝 Requirements

- Python 3.8+
- Internet connection (for AI features)
- Microphone
- Speakers/Headphones

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

MIT License - feel free to use and modify!

## 🙏 Credits

Inspired by JARVIS from Marvel's Iron Man
Built with ❤️ by Rahul Mishra

## 🔗 Links

- [GitHub Repository](https://github.com/rahul700raj/jarvis-ai-assistant)
- [Report Issues](https://github.com/rahul700raj/jarvis-ai-assistant/issues)
- [Documentation](https://github.com/rahul700raj/jarvis-ai-assistant/wiki)

---

**Made with 🤖 by Rahul Mishra**
