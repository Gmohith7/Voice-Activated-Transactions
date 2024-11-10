import sounddevice as sd
import numpy as np
from transformers import pipeline

# Initialize the Whisper ASR pipeline
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3-turbo")

def record_audio(duration=5, sample_rate=16000):
    """
    Records audio from the microphone for a specified duration and converts it to a numpy array.
    """
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Recording completed.")
    
    # Convert the recorded audio to numpy array format required by the pipeline
    return audio_data.flatten() / 32768.0  # Normalizing int16 audio to float32 format for the model

def transcribe_audio(audio_array, sample_rate=16000):
    """
    Transcribes the recorded audio numpy array using Whisper ASR model.
    """
    try:
        # Use Whisper pipeline to transcribe audio from numpy array
        transcription = pipe({"array": audio_array, "sampling_rate": sample_rate})
        return transcription['text']
    except Exception as e:
        return f"Error in transcription: {e}"
