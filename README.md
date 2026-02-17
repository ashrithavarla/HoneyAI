# 🎙️ Honey AI Voice Assistant

Honey AI is a **Python-based voice assistant** that listens to voice commands, opens apps & websites, speaks responses using text-to-speech, and integrates with **Ollama (Mistral model)** for AI conversations.

It combines:

* 🎤 Speech Recognition (`speech_recognition`)
* 🔊 Text-to-Speech (`pyttsx3`)
* 🤖 Local LLM via `ollama`
* 🌐 App & Website Automation

---

# ✨ Features

✅ Voice command recognition (English - India)
✅ Open Windows apps (camera, calculator, cmd, word, excel, etc.)
✅ Open websites (YouTube, Google, Gmail, Instagram, etc.)
✅ AI conversation using Mistral via Ollama
✅ Save AI-generated responses to files
✅ Speak responses using offline TTS
✅ Chat memory with reset option

---

# 🧱 Project Structure

```
project/
│
├── main.py        # Main voice assistant logic
├── aitest.py      # Simple Ollama test script
└── AI/            # Generated AI response files (auto-created)
```

---

# ⚙️ Requirements

* Python 3.9+
* Windows OS (app commands use Windows paths)
* Microphone enabled

Install dependencies:

```bash
pip install speechrecognition pyttsx3 ollama pyaudio
```

⚠️ If `pyaudio` fails:

```bash
pip install pipwin
pipwin install pyaudio
```

---

# 🤖 Install Ollama + Mistral Model

1. Install Ollama:
   https://ollama.com

2. Pull mistral model:

```bash
ollama pull mistral
```

---

# ▶️ Running the Assistant

Start the main program:

```bash
python main.py
```

You will hear:

```
Hello, I am Honey AI
```

Then speak commands into your microphone.

---

# 🗣️ Example Voice Commands

## 📱 Open Applications

* "Open camera"
* "Open calculator"
* "Open command prompt"
* "Open word"
* "Open excel"

## 🌐 Open Websites

* "Open youtube"
* "Open google"
* "Open linkedin"
* "Open instagram"

## 🎵 Other Commands

* "Open music"
* "What is the time"
* "Reset chat"
* "Honey quit"

## 🤖 AI Mode

Say:

```
using artificial intelligence ...
```

Honey will generate a response and save it inside `/AI` folder.

---

# 🧪 Test Ollama Separately

Run:

```bash
python aitest.py
```

This sends a prompt to Mistral and prints the AI response.

---

# 🧠 How Chat Works

The assistant stores conversation history inside:

```
chatStr
```

Each new voice input is appended and sent to Ollama to maintain context.

---

# ⚠️ Notes

* Designed mainly for **Windows** due to `os.system("start ...")`.
* Requires active microphone.
* Google Speech Recognition needs internet.
* Ollama runs locally — no external API key required.

---

# 🚀 Future Improvements (Ideas)

* Add wake-word detection ("Hey Honey")
* Add GUI interface
* Streaming responses
* Async processing for faster replies
* Add more apps & websites dynamically
* Replace global chat string with structured messages list

---

# 👩‍💻 Author

Honey AI – Local Voice Assistant using Python + Ollama
