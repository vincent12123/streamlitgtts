import streamlit as st
from gtts import gTTS

def text_to_speech(text, language="en"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")

def main():
    st.title("Aplikasi Pembaca File Teks")

    uploaded_file = st.file_uploader("Unggah file txt", type=["txt"])

    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")

        st.text("Isi File:")
        display_long_text(content)

        language = st.selectbox("Pilih bahasa", ("en", "de", "fr", "es", "it", "zh-TW"))

        if st.button("Putar"):
            if content:
                text_to_speech(content, language)
            else:
                st.warning("Harap berikan teks untuk dikonversi menjadi ucapan.")

def display_long_text(text, max_lines=20):
    lines = text.split("\n")
    num_lines = len(lines)

    if num_lines <= max_lines:
        st.text(text)
    else:
        st.text("\n".join(lines[:max_lines]))
        if st.button("Tampilkan lebih banyak"):
            st.text("\n".join(lines[max_lines:]))

if __name__ == "__main__":
    main()
