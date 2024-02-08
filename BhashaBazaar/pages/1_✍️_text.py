import streamlit as st  
from googletrans import Translator
def translateText(text, targetLang):
    translator = Translator()
    if isinstance(text,bytes):
        inputText = text.decode('utf-8')
    detectedLang = translator.detect(text).lang
    translation= translator.translate(text, src=detectedLang,dest=targetLang)
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
    targetLang = st.selectbox("Select Target Language", languages)
    text = st.text_area("Enter Text to Translate")
    if st.button("Translate"):
        if text:
            translatedText = translateText(text,target_lang)
            st.write("Translated Text:")
            st.write(translatedText)
        else:
            st.write("Please enter text to translate.")

if __name__ == '__main__':
    main()