# Audio Translation Using Whisper

A Flask-based web application that translates spoken audio from one language to another using OpenAI’s Whisper model and returns translated speech output.

## Overview
This project allows users to upload an audio file, transcribe and translate the spoken content into a target language, and generate a translated audio output. It demonstrates end-to-end handling of audio input, speech-to-text, translation, and text-to-speech within a web application.

## Features
- Upload audio files for translation
- Automatic speech recognition using Whisper
- Language translation of transcribed text
- Audio output generation for translated speech
- Simple web interface built with Flask

## Tech Stack
- Python
- Langchain
- Gen AI
- Flask
- OpenAI Whisper Model
- HTML / CSS
- dotenv

## Project Structure
.
├── app.py               # Main Flask application  
├── demo.py              # Demo / testing script  
├── requirements.txt     # Python dependencies  
├── templates/  
│   └── index.html       # Web interface  
├── static/  
│   └── *.mp3            # Sample and generated audio files  
└── LICENSE  

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/<your-username>/Audio_translation_using_Whisper.git  
cd Audio_translation_using_Whisper  

### 2. Create and activate a virtual environment
python -m venv venv  
source venv/bin/activate  

### 3. Install dependencies
pip install -r requirements.txt  

### 4. Configure environment variables
Create a `.env` file in the root directory and add:
OPENAI_API_KEY=your_api_key_here  

### 5. Run the application
python app.py  

The application will be available at:
http://localhost:8080  

## Usage
1. Open the web interface in your browser.
2. Upload an audio file.
3. Select the target language.
4. Submit the request to receive translated audio output.

## Notes
- Uploaded and generated audio files are stored temporarily.
- Basic error handling is included for invalid inputs and API failures.
- This project is intended for learning and demonstration purposes.

## Future Improvements
- Support for additional audio formats
- Automatic language detection
- Improved UI and accessibility
- Production-ready deployment setup

## License
This project is licensed under the MIT License.
