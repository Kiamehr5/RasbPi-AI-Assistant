from google import genai
from google.genai import types
import subprocess as sp 
import voicetotext as vtt
import texttovoice as ttv
import mp3towav
import voicer


# Configure the client
client = genai.Client(api_key="") # Replace with your API key

# Define the grounding tool
grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

# Configure generation settings
config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

voicer.record_to_wav()
vtt.transcribe_wav()
uinput = open("text.txt").read()

# Make the request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{uinput}",
    config=config,
)

ttv.text_to_speech(response.text)
mp3towav.convert_mp3_to_wav("output.mp3", "output.wav")
sp.run("paplay output.wav", shell=True)

