import edge_tts
import asyncio
import tempfile
import os
from playsound import playsound

async def say_utterance(text, voice="pt-BR-AntonioNeural"):
    if 'speech' in text:
        communicate = edge_tts.Communicate(text=text['speech'], voice=voice)
    else:
        communicate = edge_tts.Communicate(text=text['text'], voice=voice)
    chunks = []

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            chunks.append(chunk["data"])

    audio_data = b"".join(chunks)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(audio_data)
        temp_filename = temp_audio.name

    playsound(temp_filename)
    os.remove(temp_filename)
    return text['speech'] if 'speech' in text else text['text']