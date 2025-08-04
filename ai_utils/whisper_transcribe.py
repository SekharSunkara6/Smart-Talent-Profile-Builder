import openai

def whisper_transcribe(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
    return transcript['text']
