import streamlit as st
import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
import os
import tempfile

# Initialize recognizer
recognizer = sr.Recognizer()

# Record audio using Streamlit audio recorder
audio_bytes = audio_recorder()

if audio_bytes:
    # Instead of showing the audio, we process it directly
    # Create a temporary file for the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        audio_file_path = temp_audio_file.name
        temp_audio_file.write(audio_bytes)

    # Use speech recognition to transcribe the audio
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            # Transcribe the audio
            transcription = recognizer.recognize_google(audio_data)
            st.write("Transcription: ", transcription)
        except sr.UnknownValueError:
            st.write("Could not understand the audio.")
        except sr.RequestError as e:
            st.write(f"Error with the transcription service: {e}")
    
    # Clean up the temporary file after use
    os.remove(audio_file_path)
