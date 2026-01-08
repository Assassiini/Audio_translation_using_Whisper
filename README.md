# Audio Translation Using Whisper Model

A Flask-based web application that translates spoken audio into a target language using OpenAI’s Whisper model and generates translated speech output. The project demonstrates end-to-end audio upload handling, speech-to-text translation, and audio generation in a web application.

## Overview
This application allows users to upload an audio file through a web interface. The audio is processed using OpenAI’s Whisper model to transcribe and translate the speech. The translated text is then converted into an audio file and returned to the user.

The project focuses on practical integration of speech models into a backend service, including secure file handling and cleanup.

## Features
- Audio file upload via web interface
- Speech-to-text translation using OpenAI Whisper
- Translated speech audio generation
- Temporary file handling with automatic cleanup
- Flask-based backend with HTML frontend

## Tech Stack
- Python
- Langchain
- Gen AI
- Flask
- OpenAI Whisper API
- HTML / CSS

## Project Structure
  
    ├── app.py                   # Main Flask application and API logic
    ├── demo.py                  # Standalone Whisper translation test script
    ├── requirements.txt         # Python dependencies
    ├── templates/
    │   └── index.html           # Web interface
    ├── static/                  # Generated and sample audio files
    ├── *.mp3                    # Sample audio inputs
    ├── LICENSE
    └── .gitignore

## How It Works
1. User uploads an audio file through the web interface.
2. The server saves the file securely with a unique filename.
3. Whisper translates the spoken content into text.
4. The translated text is converted into speech audio.
5. The translated audio file is returned to the user.
6. Temporary input and output files are deleted after processing.

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
OPENAI_API_KEY=your_openai_api_key  

### 5. Run the application
python app.py  

The application will be available at:
http://localhost:8080  

## Usage
- Open the web interface in a browser
- Upload an audio file containing spoken language
- Receive translated speech output as an audio file

## Notes
- Uploaded and generated audio files are deleted after processing.
- The demo.py file is provided for testing Whisper translation independently.
- SSL verification is disabled in demo.py for local testing purposes only.

## Future Improvements
- Support for additional audio formats
- Language auto-detection
- Improved frontend UI
- Production-ready deployment configuration

## License
This project is licensed under the MIT License.
