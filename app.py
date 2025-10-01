import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, url_for
from werkzeug.utils import secure_filename
from openai import OpenAI
import uuid # Used for generating unique filenames

# --- Initialization ---
load_dotenv()

try:
    client = OpenAI()
except Exception as e:
    print("Error: OpenAI API key not found.")
    exit()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"

# --- Main Application Route ---
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if "file" not in request.files or not request.files["file"].filename:
            return jsonify({"error": "No file part"}), 400
        if "language" not in request.form or not request.form["language"]:
            return jsonify({"error": "No language selected"}), 400

        file = request.files["file"]
        language = request.form["language"]
        
        # Use a unique filename for the uploaded file to prevent conflicts
        original_filename = secure_filename(file.filename)
        unique_id = uuid.uuid4().hex
        input_filename = f"{unique_id}_{original_filename}"
        input_filepath = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
        file.save(input_filepath)

        output_audio_path = None # Initialize path for cleanup

        try:
            # 1. Transcribe the audio in its original language
            with open(input_filepath, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            
            # 2. Translate the transcribed text to the target language
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant. You will be provided with text in an unknown language, and your task is to translate it into {language}."},
                    {"role": "user", "content": transcript.text}
                ],
                temperature=0,
                max_tokens=256
            )
            
            translated_text = response.choices[0].message.content

            # --- NEW: Convert the translated text back to audio ---
            # 3. Generate speech from the translated text
            output_filename = f"translated_{unique_id}.mp3"
            output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            
            speech_response = client.audio.speech.create(
                model="tts-1",
                voice="alloy", # You can choose from alloy, echo, fable, onyx, nova, shimmer
                input=translated_text
            )
            
            # Save the generated audio to a file
            speech_response.stream_to_file(output_filepath)
            
            # Get a URL for the audio file that the browser can access
            output_audio_url = url_for('static', filename=output_filename)

            return jsonify({
                'translated_text': translated_text,
                'audio_url': output_audio_url # <-- NEW: Send the audio URL back
            })

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500

        finally:
            # Clean up both the uploaded and generated files
            if os.path.exists(input_filepath):
                os.remove(input_filepath)
            if output_audio_path and os.path.exists(output_audio_path):
                os.remove(output_audio_path)
                
    return render_template("index.html")

# --- Run the App ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)