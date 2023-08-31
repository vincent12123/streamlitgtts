import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech Recognition App")
    
    recognizer = sr.Recognizer()
    audio = None  # Initialize the audio variable

    with st.sidebar:
        st.header("Settings")
        language = st.selectbox("Select Language", ["en-US", "id-ID"])
        audio_source = st.radio("Select Audio Source", ["Microphone", "Upload Audio"])

    if audio_source == "Microphone":
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)

    else:
        audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
        if audio_file:
            audio = sr.AudioFile(audio_file)
            with audio as source:
                audio = recognizer.record(source)

    if audio:
        try:
            st.write("Transcription:")
            text = recognizer.recognize_google(audio, language=language)
            st.write(text)
        except sr.UnknownValueError:
            st.write("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
