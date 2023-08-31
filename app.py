import streamlit as st
from gtts import gTTS  # Corrected import statement

def text_to_speech(text, language="en"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")

st.title("Text to Speech")
text = st.text_input("Enter text")
language = st.selectbox("Select language", ("en", "de", "fr", "es", "it"))

if st.button("Play"):
    text_to_speech(text, language)
