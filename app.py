import streamlit as st
from audio_recorder_streamlit import audio_recorder
import asyncio
from utils import send_audio_for_transcription

# Set up Streamlit interface
st.set_page_config(page_title="Real-time Transcription", page_icon="🎙️", layout="centered")
st.title("🎙️ Real-time Transcription with OpenAI Whisper")
st.markdown("## Click the button below to start recording")

# Style adjustments to ensure visibility
st.markdown("""
    <style>
        .stButton > button {
            width: 100%;
            font-size: 20px;
            padding: 10px;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            font-size: 12px;
            color: #555;
        }
    </style>
    """, unsafe_allow_html=True)

# Container for the microphone and audio recording
footer_container = st.container()
with footer_container:
    st.markdown("### 🎤 Record your audio")
    audio_bytes = audio_recorder()

# Process the recorded audio if it meets the minimum length requirement
if audio_bytes:
    with st.spinner("Transcribing..."):
        if len(audio_bytes) >= 1600:  # Roughly 0.1 seconds of audio
            st.info("Audio data recorded, sending to server for transcription")
            transcript = asyncio.run(send_audio_for_transcription(audio_bytes))
            if transcript:
                st.session_state["messages"] = st.session_state.get("messages", [])
                st.session_state.messages.append({"role": "user", "content": transcript})
                st.success("Transcription successful!")
                st.text_area("📝 Transcribed Text", value=transcript, height=200)
            else:
                st.error("Failed to receive transcription.")
        else:
            st.warning("Audio file is too short. Please record for at least 0.1 seconds.")

# Add a footer with some styling
st.markdown("""
    <div class="footer">
        Made with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)
