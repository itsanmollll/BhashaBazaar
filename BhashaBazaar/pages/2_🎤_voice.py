import streamlit as st
import wave 
import pyaudio
from google.oauth2 import service_account
from google.cloud import speech_v1p1beta1 as speech

@st.cache_data()
def transcribe(audio):
    clientFile = '/Users/anmol/Desktop/Work/basicPractice/bhashabazaar-b14fbe10ecd5.json'
    credentials = service_account.Credentials.from_service_account_file(clientFile)
    client = speech.SpeechClient(credentials=credentials)
    audio = speech.RecognitionAudio(content=audio)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100, #range(8-something)
        language_code="en-US",
        enable_automatic_punctuation=True,
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript

@st.cache_data()
def recordAudio(filename, seconds=5):
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

def main(): 
    st.title("Voice")
    if st.button("Record Audio"):
        recordAudio("recorded_audio.wav")
        st.write("Recording finished. Click 'Transcribe' to convert speech to text.")
    if st.button("Transcribe"):
        audio = open("recorded_audio.wav", "rb").read()
        text = transcribe(audio)
        st.write("Transcribed Text:")
        st.write(text)


if __name__ == '__main__':
    main()