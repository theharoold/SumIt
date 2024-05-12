from flask import Flask, request, jsonify
import os
from transcribe import video_transcribe 
from summarize import transcript_summarize 

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Check if the POST request has a file attached
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Check if the file is allowed
    allowed_extensions = {'mp4', 'mov', 'avi', 'wav'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Unsupported file type'})

    # Save the video file
    video_path = 'uploads/' + file.filename
    file.save(video_path)

    # Convert video to audio (mp3)
    audio_path = 'uploads/audio.mp3'
    os.system(f'ffmpeg -i {video_path} -vn -acodec libmp3lame -ar 44100 -ac 2 -ab 192k -y {audio_path}')

    # Call OpenAI function to transcribe audio
    with open(audio_path, 'rb') as audio_file:
        transcription = video_transcribe(audio_file)

    summarization = transcript_summarize(transcription)
    # Return the transcription
    return jsonify({'text': summarization})

if __name__ == '__main__':
    app.run(debug=True)