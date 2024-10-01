import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

audio_buffer = text_to_speech("Good")

st.audio(audio_buffer, format="audio/mp3")
