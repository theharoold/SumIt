import openai 
import os 

def video_transcribe(audio_file):
    
  # Retrieve OpenAI API key from environment variable
  client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  return client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )

