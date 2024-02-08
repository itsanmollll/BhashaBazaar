import streamlit as st  
from googletrans import Translator
from transformers import MBartForConditionalGeneration, MBartTokenizer
@st.cache_data()
def loadModel():
    model_name = "facebook/mbart-large-50-one-to-many-mmt"
    tokenizer_name = "facebook/mbart-large-en-ro"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBartTokenizer.from_pretrained(tokenizer_name, src_lang="en_XX")
    return model, tokenizer
@st.cache_data()
def translateModel(article_en, target_language):
    model, tokenizer = loadModel()
    model_inputs = tokenizer(article_en, return_tensors="pt")
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[target_language]
    )
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return translation[0]
@st.cache_data()
def translateText_Api(text, targetLang):
    translator = Translator()
    if isinstance(text,bytes):
        text = text.decode('utf-8')
    detectedLang = translator.detect(text).lang
    translation= translator.translate(text, src=detectedLang, dest=targetLang)
    return translation.text

def main():
    st.title("Indic Language  Text Translator")
    languages = {
        "English": "en",
        "Hindi": "hi",
        "Bengali": "bn",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Marathi": "mr",
        "Odia": "or",
        "Punjabi": "pa",
        "Tamil": "ta",
        "Telugu": "te",
    }
    targetLang = st.selectbox("Select Target Language", languages)
    text = st.text_area("Enter Text to Translate")
    if st.button("Translate"):
        if text:
            translatedText = translateText_Api(text,targetLang)
            st.write("Translated Text:")
            st.write(translatedText)
        else:
            st.write("Please enter text to translate.")

    article_en = st.text_area("Enter Text to Translate using Model")
    target_language = st.selectbox("Select Target Language", ["en_XX","hi_IN","bn_IN","gu_IN","kn_IN","ml_IN","mr_IN","or_IN","pa_IN","ta_IN"])
    if st.button("Translate using Model"):
        if article_en:
            translatedText = translateModel(article_en, target_language)
            st.write("Translated Text:")
            st.write(translatedText)
        else:
            st.write("Please enter text to translate.")

if __name__ == '__main__':
    main()