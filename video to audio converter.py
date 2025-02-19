import streamlit as st
from moviepy import VideoFileClip
import os

def video_to_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = os.path.splitext(video_path)[0] + '.mp3'
    video.audio.write_audiofile(audio_path)
    return audio_path


st.title("Video to Audio Converter")

uploaded_files = st.file_uploader("Upload MP4 files", accept_multiple_files=True, type=["mp4"])

if st.button("Convert"):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            video_path = os.path.join(os.getcwd(), uploaded_file.name)
            with open(video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            with st.spinner("Converting..."):
                audio_path = video_to_audio(video_path)
            st.success(f"Converted: {audio_path}")
            st.audio(audio_path, format='audio/mp3')
    else:
        st.warning("Please upload at least one MP4 file")
