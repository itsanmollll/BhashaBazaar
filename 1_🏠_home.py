import streamlit as st
st.set_page_config(page_title="BhashaBazaar", page_icon="🌐", layout="wide")
st.markdown("""<h1 id="title-h"><span data-id="s1" class="spans">BHASHA</span><span data-id="s2">-BAZAAR 🎙️:</span></h1><br><h2><span data-id="s3 style="font-size: smaller;>Your Gateway to Multilingual Communication</h2>""",
            unsafe_allow_html=True)

def main():
    st.markdown('# Features of the app')

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📝️Text Translation (API) 🕉")
        st.markdown('''The app offers text translation functionality powered by an API. Users can seamlessly translate text between multiple languages with ease. Whether it's translating a single phrase or an entire document, the translation feature ensures accurate and efficient language conversion.''')
        st.markdown('''
        1. **Advanced Customization**
        2. **Wide Language Support**
        3. **Consistent Performance**
        4. **Real-time Updates**
        5. **Scalability and Reliability**''')
    

    with col2:
        st.markdown("### 📝️Text Translation (Model)🕉")
        st.markdown('''The app offers text translation functionality powered by the mBart model. Users can seamlessly translate text between multiple languages with ease. Whether it's translating a single phrase or an entire document, the translation feature ensures accurate and efficient language conversion.''')
        st.markdown('''
        1. **Open-Source Availability**
        2. **Cost-Effectiveness**
        3. **Privacy and Data Control**
        4. **Domain-specific Adaptation**
        5. **Offline Capabilities**
        ''')

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("#### 🗣️Speach-to-Text Translation🗒")
        st.markdown(''' The app offers seamless speech-to-text functionality, allowing users to easily convert spoken words into written text. With this feature, users can simply speak into their device's microphone, and the app will transcribe their speech into text in real-time.''')
        st.markdown('''
        1. **Accurate Transcription**
        2. **Real-time Transcription**
        3. **Accurate Speech Recognition**
        4. **Multi-language Support**
        5. **Multi-platform Integration**
        ''')
    with col4:
        st.markdown("#### 📃Text-to-Speech Conversion🔊")
        st.markdown('''The app provides text-to-speech conversion functionality, enabling users to convert written text into spoken words. With this feature, users can listen to synthesized speech generated from written text, enhancing accessibility and communication.''')
        st.markdown('''
        1. **Natural-sounding Speech**
        2. **Multi-language Support**
        3. **Customizable Voice Options**
        4. **High-quality Audio Output**
        5. **Real-time Synthesis**
        ''')

    st.text('')
    st.text('')
    st.markdown('# Dependecies:')

    st.markdown('''
    1. **Cloud Translation API** - The API is taken from [Google Cloud](https://cloud.google.com/?hl=en).
    2. **MBart(Model)** - The historical data is taken from [MBart](https://huggingface.co/docs/transformers/en/model_doc/mbart).
    3. **Cloud Speech-to-Text API** - The API is taken from [Google Cloud](https://cloud.google.com/?hl=en).
    4. **Cloud Text-to-Speech API** - The API is taken from [Google Cloud](https://cloud.google.com/?hl=en).
    ''')


if __name__ == "__main__":
    main()
