# 🎙️ Gemini Assistant on Raspberry Pi

A lightweight voice assistant powered by **Gemini 2.5 Flash**, running on a **Raspberry Pi 5** with a connected **microphone** and **speaker**.

This project turns your Pi into a simple, privacy-friendly smart assistant capable of listening, thinking, and speaking back — all in one compact setup.

---

## 📦 Features

- 🎤 Voice input using a USB
- 🧠 Natural language understanding via **Gemini 2.5 Flash**
- 🔊 Text-to-speech output through a speaker
- 💬 Real-time conversations with voice feedback
- ⚡ Runs on Raspberry Pi (tested on Pi 5)
- 🕶️ Minimal UI — just talk to it

---

## 🧰 Hardware Requirements

- Raspberry Pi 4/5 (4GB or 8GB recommended, tested on a Pi 5)
- USB
- USB speaker (or Pi-compatible amplifier/speaker HAT)
- Internet connection (for Gemini access)

---

## 🚀 Getting Started

### 1. Clone the Repo

(first remember to put your api key then proceed)
```bash
git clone https://github.com/your-username/gemini-pi-assistant.git
cd gemini-pi-assistant
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
pip3 install -r requirements.txt
python main.py
