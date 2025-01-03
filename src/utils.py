import cv2
# import subprocess
import os
from openai import OpenAI
# import sounddevice as sd
# import soundfile as sf
# import requests
# from pydub import AudioSegment
import pyscreenshot

openai_api_key = os.environ.get('OPENAI_API_KEY')
# xi_api_key = os.environ.get('ELEVEN_LABS_API_KEY')

def take_picture():
    cap = cv2.VideoCapture(0)
    ramp_frames = 30 
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    for i in range(ramp_frames):
        ret, frame = cap.read()

    cap.release()
    if ret:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        print("Error: Could not read frame.")
        return None

def take_screenshots():
    try:
        # Capture the full screen
        image = pyscreenshot.grab()
        
        # Save the image
        save_filepath = os.path.dirname(os.path.dirname(__file__))+"/screenshots/screen_1.png"
        os.makedirs(os.path.dirname(save_filepath), exist_ok=True)
        image.save(save_filepath)
        
        return [save_filepath]
    except Exception as e:
        print(f"Screenshot error: {e}")
        return None

def get_number_of_screens():
    return 1

def text_to_speech_deprecated(text):
    # Temporarily disable TTS
    print("Text-to-speech functionality temporarily disabled")
    return None
    client = OpenAI(api_key=openai_api_key)
    voice = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    voice_save_path = os.path.dirname(__file__)+"/yell_voice.wav"
    voice.stream_to_file(voice_save_path)
    audio_data, sample_rate = sf.read(voice_save_path)
    sd.play(audio_data, sample_rate)
    sd.wait()


def get_text_to_speech(text, voice="Harry"):
    # Temporarily disable TTS
    print("Text-to-speech functionality temporarily disabled")
    return None
    character_dict = {
        "Adam" : "pNInz6obpgDQGcFmaJgB",
        "Arnold" : "VR6AewLTigWG4xSOukaG",
        "Emily" : "LcfcDJNUP1GQjkzn1xUU",
        "Harry" : "SOYHLrjzK2X1ezoPC6cr",
        "Josh": "TxGEqnHWrfWFTfGW9XjX",
        "Patrick" : "ODq5zmih8GrVes37Dizd"
    }
    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{character_dict[voice]}"
    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": xi_api_key
    }
    data = {
    "text": text,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    voice_path_mp3 = os.path.dirname(__file__)+"/yell_voice.mp3"
    with open(voice_path_mp3, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    voice_path_wav = os.path.dirname(__file__)+"/yell_voice.wav"
    audio = AudioSegment.from_mp3(voice_path_mp3)
    audio.export(voice_path_wav, format="wav")
    return voice_path_wav

def play_text_to_speech(voice_file):
    # Temporarily disable TTS
    print("Text-to-speech functionality temporarily disabled")
    return None
    data, samplerate = sf.read(voice_file)
    sd.play(data, samplerate)
    sd.wait()


# def run_applescript(script_path):
#     subprocess.call(['osascript', script_path])

# def mute_applications():
#     run_applescript(os.path.dirname(__file__)+'/mute_apps.applescript')

# def unmute_applications():
#     run_applescript(os.path.dirname(__file__)+'/unmute_apps.applescript')
