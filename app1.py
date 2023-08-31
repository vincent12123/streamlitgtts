import streamlit as st
from gtts import gTTS

def text_to_speech(text, language="en"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")

st.title("Text to Speech")

# Pilihan untuk memilih sumber teks
source_option = st.radio("Select text source", ("Input Text", "Upload Text File"))

if source_option == "Input Text":
    text = st.text_input("Enter text")
else:
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")

language = st.selectbox("Select language", ("en", "de", "fr", "es", "it", "zh-TW"))

if st.button("Play"):
    if text:
        text_to_speech(text, language)
    else:
        st.warning("Please provide some text to convert to speech.")
