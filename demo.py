import openai
import os
from dotenv import load_dotenv
import requests # Make sure to import requests
import ssl
import sys

print("--- DEBUGGING ENVIRONMENT VARIABLES ---")
print(f"Python Executable: {sys.executable}")
print(f"REQUESTS_CA_BUNDLE = {os.getenv('REQUESTS_CA_BUNDLE')}")
print(f"M2_APP_UUID = {os.getenv('M2_APP_UUID')}")
print("---------------------------------------")

# --- SSL Bypass Patch for the 'requests' library ---
# This code forces every request made by the 'requests' library to ignore SSL verification.
# It will work here because the openai library uses 'requests'.
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
warnings.simplefilter('ignore', InsecureRequestWarning)

for method in ("get", "post", "put", "delete", "head", "options", "patch"):
    original = getattr(requests, method)
    def insecure_request(*args, _original=original, **kwargs):
        kwargs["verify"] = False
        return _original(*args, **kwargs)
    setattr(requests, method, insecure_request)
# ----------------------------------------------------

ssl._create_default_https_context = ssl._create_unverified_context

# Your original code
load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPEN_AI_API_KEY

try:
    audio_file = open("t2.mp3", "rb")
    output = openai.Audio.translate("whisper-1", audio_file)
    print(output)
except Exception as e:
    print(f"An error occurred: {e}")