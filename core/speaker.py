from openai import OpenAI
from config.settings import OPENAI_API_KEY
import subprocess
import tempfile
import os

client = OpenAI(api_key=OPENAI_API_KEY)

def speak(text: str):
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )
    
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        f.write(response.content)
        temp_path = f.name
    
    subprocess.run(["afplay", temp_path])
    os.unlink(temp_path)