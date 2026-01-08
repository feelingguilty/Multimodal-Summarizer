import pypdf
import os
import whisper
from transformers import pipeline
import pydub # Added pydub for audio processing

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
    return text

def extract_audio_from_video(video_path, output_audio_path="temp_audio.mp3"):
    """
    Extracts audio from a video file using pydub.
    Requires ffmpeg to be installed and accessible in the system's PATH.
    """
    try:
        video = pydub.AudioSegment.from_file(video_path)
        video.export(output_audio_path, format="mp3")
        return output_audio_path
    except Exception as e:
        print(f"Error extracting audio from video: {e}")
        return None

def transcribe_audio(audio_path):
    """
    Transcribes audio using OpenAI's Whisper model.
    """
    try:
        model = whisper.load_model("base") # You can choose a different model size like "small", "medium", "large"
        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

def summarize_text(text):
    """
    Summarizes text using a Hugging Face model (e.g., LaMini-Flan-T5).
    """
    try:
        # Using a quantized LaMini-Flan-T5 model
        summarizer = pipeline("summarization", model="MBZUAI/LaMini-Flan-T5-783M", device=-1) # device=-1 for CPU, 0 for GPU
        # For quantized model, you might need to load it differently or ensure it's handled by the pipeline
        # For simplicity, using the direct model name which should pull a suitable version
        summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error summarizing text: {e}")
        return None

def multimodal_summarizer_pipeline(file_path, file_type):
    """
    Unified pipeline to ingest and process various content types for summarization.
    """
    extracted_text = None
    audio_path = None
    summary = None

    if file_type == "text":
        with open(file_path, 'r', encoding='utf-8') as f:
            extracted_text = f.read()
    elif file_type == "pdf":
        extracted_text = extract_text_from_pdf(file_path)
    elif file_type == "audio":
        extracted_text = transcribe_audio(file_path)
    elif file_type == "video":
        audio_path = extract_audio_from_video(file_path)
        if audio_path:
            extracted_text = transcribe_audio(audio_path)
            os.remove(audio_path) # Clean up temporary audio file
    
    if extracted_text:
        summary = summarize_text(extracted_text)
    
    return summary
