from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    # Load your MP3 file
    audio = AudioSegment.from_mp3(mp3_path)
    # Export as WAV
    audio.export(wav_path, format="wav")
    print(f"Converted '{mp3_path}' to '{wav_path}' successfully.")

if __name__ == "__main__":
    mp3_file = "output.mp3"   # Replace with your mp3 file path
    wav_file = "output.wav"  # Replace with your desired wav output path

    convert_mp3_to_wav(mp3_file, wav_file)
