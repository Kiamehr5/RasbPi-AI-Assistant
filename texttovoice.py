from openai import OpenAI

client = OpenAI(api_key="")  # Replace with your API key

def text_to_speech(text, voice="onyx", filename="output.mp3"):
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"✅ Audio saved to {filename}")

if __name__ == "__main__":
    text_to_speech("Hello, this is a test of the OpenAI text to speech system.")
