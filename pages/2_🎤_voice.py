import os 
import wave
import streamlit as st
import pyaudio
from google.oauth2 import service_account
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import texttospeech


recordFiles =[]
@st.cache_data()
def deletePreviousAudio(filename):
    if os.path.exists(filename):
        os.remove(filename)

@st.cache_data()
def transcribe(audio_content,language_code):
    clientFile = '/Users/anmol/Desktop/Work/BhashaBazaar/bhashabazaar-b14fbe10ecd5.json' # Replace this with your own client file
    credentials = service_account.Credentials.from_service_account_file(clientFile)
    client = speech.SpeechClient(credentials=credentials)
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100, #range(8-something)
        language_code=language_code,
        enable_automatic_punctuation=True,
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript

@st.cache_data()
def recordAudio(filename, seconds=5):
    deletePreviousAudio(filename)
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames = [stream.read(chunk) for _ in range(0, int(fs / chunk * seconds))]
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b"".join(frames))
    recordFiles.append(filename)

@st.cache_data()
def clearRecordedFiles():
    for filename in recordFiles:
        deletePreviousAudio(filename)
    recordFiles.clear()

@st.cache_data()
def generate_audio(text_block):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/anmol/Desktop/Work/basicPractice/bhashabazaar-b14fbe10ecd5.json'
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text_block)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN",
        name="en-IN-Wavenet-D",
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        effects_profile_id=["handset-class-device"],
        speaking_rate=1.0,
        pitch=1
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response.audio_content

def main(): 
    st.title("Voice 🗣")
    st.subheader("Do Audio Related Work Here: ")
    st.markdown("This page allows you to perform speech-to-text and text-to-speech operations. You can record audio and convert it to text, or enter text and convert it to audio.")
    st.markdown("---")
    cols = st.columns([10,1,10])
    with cols[0]:
        st.title("Speech-to-Text")
        st.subheader("Generate text from speach")
        # language_code = st.selectbox("Select Language", ["en-US","hi-IN","bn-IN","gu-IN","kn-IN","ml-IN","mr-IN","or-IN","pa-IN","ta-IN"])
        uploaded_file = st.file_uploader("Upload Audio File", type=["wav"])
        language_code = st.selectbox("Select Language", ["en-US", "hi-IN", "bn-IN", "gu-IN", "kn-IN", "ml-IN", "mr-IN", "or-IN", "pa-IN", "ta-IN"])
        # if uploaded_file is not None:
        #     # Read the uploaded audio file
        #     audio_content = uploaded_file.read()
        #     st.info("Recording finished. Click 'Transcribe' to convert speech to text.")
        # if st.button("Transcribe"):
        #     text = transcribe(audio_content,language_code)
        #     st.subheader("Transcribed Text 🖨")
        #     st.text(' ')
        #     st.markdown(f"**{text}**")
        if st.button("#### 🎙 \n #### Record Audio"):
            recordAudio(f"recorded_audio.wav") 
            st.info("Recording finished. Click 'Transcribe' to convert speech to text.")
        if st.button("Transcribe"):
            audio = open("recorded_audio.wav", "rb").read()
            text = transcribe(audio,language_code)
            st.subheader("Transcribed Text 🖨")
            st.text(' ')
            st.markdown(f"**{text}**")
            
    with cols[2]:
        st.title("Text-to-Speech")
        st.subheader("Generate audio from text")
        text_block = st.text_area("### Enter Text")
        if st.button("Generate Audio"):
            st.info("Generating audio...")
            audio_content = generate_audio(text_block)
            with open("audio.mp3", "wb") as output:
                output.write(audio_content)
                st.audio("audio.mp3")
            
if __name__ == '__main__':
    main()