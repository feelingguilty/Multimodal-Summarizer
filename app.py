import streamlit as st
import os
from src.main import get_summary
import mimetypes

# Set page title
st.set_page_config(page_title="Multimodal Summarizer", layout="wide")

st.title("📄 Multimodal Summarizer")
st.markdown("""
    Choose an input method to get a concise summary!
    **Note:** For audio/video processing, ensure `ffmpeg` is installed on your system.
""")

# Radio buttons for input method selection - moved to sidebar
with st.sidebar:
    st.header("Input Method")
    input_method = st.radio(
        "Select Input Type:",
        ("Direct Text Input", "Upload Document (PDF/Text)", "Upload Multimodal (Audio/Video)")
    )
    st.sidebar.info("Select how you want to provide content for summarization.")


summary = None

if input_method == "Direct Text Input":
    st.subheader("Summarize Direct Text Input")
    text_input = st.text_area("Paste or type your text here:", height=300)
    if st.button("Summarize Text") and text_input:
        with st.spinner("Generating summary..."):
            # Create a temporary file for direct text input
            os.makedirs("temp", exist_ok=True)
            temp_file_path = os.path.join("temp", "direct_text_input.txt")
            with open(temp_file_path, "w", encoding="utf-8") as f:
                f.write(text_input)
            
            summary = get_summary(temp_file_path, "text")
            os.remove(temp_file_path) # Clean up temp file
            try:
                os.rmdir("temp")
            except OSError:
                pass
elif input_method == "Upload Document (PDF/Text)":
    st.subheader("Upload Document for Summarization")
    uploaded_file = st.file_uploader("Choose a document (PDF, TXT)", type=["txt", "pdf"])
    if uploaded_file is not None:
        file_type = None
        mime_type = mimetypes.guess_type(uploaded_file.name)[0]

        if mime_type:
            if mime_type.startswith('text'):
                file_type = "text"
            elif mime_type == 'application/pdf':
                file_type = "pdf"
        
        if not file_type:
            st.error("Could not determine file type. Please upload a supported document (txt, pdf).")
        else:
            st.write(f"Detected file type: {file_type}")

            os.makedirs("temp", exist_ok=True)
            temp_file_path = os.path.join("temp", uploaded_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.info("File uploaded successfully! Processing for summarization...")

            with st.spinner("Generating summary... This might take a while for large files."):
                summary = get_summary(temp_file_path, file_type)
            
            os.remove(temp_file_path)
            try:
                os.rmdir("temp")
            except OSError:
                pass

elif input_method == "Upload Multimodal (Audio/Video)":
    st.subheader("Upload Audio or Video for Summarization")
    uploaded_file = st.file_uploader("Choose an audio or video file", type=["mp3", "wav", "mp4", "avi", "mov"])
    if uploaded_file is not None:
        file_type = None
        mime_type = mimetypes.guess_type(uploaded_file.name)[0]

        if mime_type:
            if mime_type.startswith('audio'):
                file_type = "audio"
            elif mime_type.startswith('video'):
                file_type = "video"
        
        if not file_type:
            st.error("Could not determine file type. Please upload a supported file (mp3, wav, mp4, avi, mov).")
        else:
            st.write(f"Detected file type: {file_type}")

            os.makedirs("temp", exist_ok=True)
            temp_file_path = os.path.join("temp", uploaded_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.info("File uploaded successfully! Processing for summarization...")

            with st.spinner("Generating summary... This might take a while for large files or video/audio."):
                summary = get_summary(temp_file_path, file_type)
            
            os.remove(temp_file_path)
            try:
                os.rmdir("temp")
            except OSError:
                pass

if summary:
    st.success("Summary Generated!")
    st.subheader("Summary:")
    st.write(summary)
elif summary is not None and not summary: # This covers cases where summary is None due to error
    st.error("Failed to generate summary. Please check the Streamlit console for more details or try a different input.")


st.sidebar.header("About")
st.sidebar.info("This Multimodal Summarizer leverages OpenAI Whisper for audio transcription and a quantized LaMini-Flan-T5 model for text summarization. It can process text, PDF, audio, and video inputs.")
