import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.signal import find_peaks
from openai import OpenAI
import time

# === CONFIG ===
OPENAI_API_KEY = "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"  # Replace with your key
THRESHOLD = 0.01           # Silence level (lower = more sensitive)
SILENCE_DURATION = 1.5     # Stop if silent for this many seconds
SAMPLERATE = 16000
CHANNELS = 1
WAV_FILE = "input.wav"
TEXT_FILE = "text.txt"

# === Init OpenAI ===
client = OpenAI(api_key=OPENAI_API_KEY)

# === Record until silence ===
def record_to_wav():
    print("🎙️ Listening... Speak now.")
    buffer = []
    silent_chunks = 0
    chunk_duration = 0.2  # 200ms
    frames_per_chunk = int(SAMPLERATE * chunk_duration)

    def is_silent(data):
        return np.abs(data).mean() < THRESHOLD

    with sd.InputStream(samplerate=SAMPLERATE, channels=CHANNELS) as stream:
        while True:
            data, _ = stream.read(frames_per_chunk)
            buffer.append(data)
            if is_silent(data):
                silent_chunks += 1
            else:
                silent_chunks = 0
            if silent_chunks * chunk_duration > SILENCE_DURATION:
                print("🛑 Silence detected. Stopping.")
                break

    audio = np.concatenate(buffer, axis=0)
    sf.write(WAV_FILE, audio, SAMPLERATE)
    print(f"✅ Saved to {WAV_FILE}")

# === Main ===
if __name__ == "__main__":
    record_to_wav()
