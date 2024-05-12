import openai 
import os 

def transcript_summarize(transcript):
    
  # Retrieve OpenAI API key from environment variable
  client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  prompt = f"Summarize the following transcript of a video: {transcript}"
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an assistant whose role is to summarize the transcript of a video. Be short, concise and precise."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=150,
    n=1,
  )
  summary = response.choices[0].message.content.strip()
  return summary

