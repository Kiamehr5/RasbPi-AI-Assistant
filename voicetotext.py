from openai import OpenAI

# Initialize client
client = OpenAI(api_key="")  # Replace with your real API key

def transcribe_wav(file_path="input.wav"):
    with open(file_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    with open("text.txt", "w") as file:
        file.write(f"Simply explain, {transcript.text}")

if __name__ == "__main__":
    transcribe_wav()
