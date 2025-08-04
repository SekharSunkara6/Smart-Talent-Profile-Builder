import openai

def whisper_transcribe(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file
        )
    return transcript['text']
