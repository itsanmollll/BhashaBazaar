import streamlit as st  
from googletrans import Translator
def translate_text(text, target_lang):
    translator = Translator()
    if isinstance(text,bytes):
        input_text = text.decode('utf-8')
    detected_lang = translator.detect(text).lang
    translation= translator.translate(text, src=detected_lang,dest=target_lang)
    return translation.text

def main():
    st.title("Indic Language  Text Translator")
    languages = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Japanese": "ja",
        "Hindi": "hi",
        # Add more Indic languages here
        "Bengali": "bn",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Odia": "or",
        "Punjabi": "pa",
        "Tamil": "ta",
        "Telugu": "te",
        # Add more Indic languages as needed
    }
    target_lang = st.selectbox("Select Target Language", languages)
    text = st.text_area("Enter Text to Translate")
    if st.button("Translate"):
        if text:
            translated_text = translate_text(text,target_lang)
            st.write("Translated Text:")
            st.write(translated_text)
        else:
            st.write("Please enter text to translate.")

if __name__ == '__main__':
    main()