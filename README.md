# Multimodal Summarizer

A Python-based multimodal summarization tool that integrates OpenAI's Whisper for transcription and a quantized LaMini-Flan-T5 model for text summarization. It provides a unified pipeline to ingest and process text, PDF, audio, and video content, significantly reducing cross-media content analysis time.

## Features

*   **Multimodal Input:** Summarize content from various sources:
    *   **Text files (.txt)**
    *   **PDF documents (.pdf)**
    *   **Audio files (.mp3, .wav)**
    *   **Video files (.mp4, .avi, .mov)**
*   **Audio Transcription:** Utilizes OpenAI's Whisper model to accurately transcribe speech from audio and video inputs.
*   **Text Summarization:** Leverages a quantized LaMini-Flan-T5 model from Hugging Face for efficient and effective text summarization.
*   **User-Friendly Interface:** A Streamlit web application for easy interaction and summary generation.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Multimodal-Summarizer.git
cd Multimodal-Summarizer
```

### 2. System Dependencies (FFmpeg)

For audio and video processing, you need to have `ffmpeg` installed on your system.

*   **Windows:**
    1.  Download a build from [ffmpeg.org](https://ffmpeg.org/download.html).
    2.  Extract the archive and add the `bin` directory (e.g., `C:\ffmpeg\bin`) to your system's PATH environment variable.
*   **macOS:**
    ```bash
    brew install ffmpeg
    ```
*   **Linux (Debian/Ubuntu):**
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

### 3. Python Environment Setup

It is highly recommended to use a virtual environment.

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## How to Run the Application

1.  **Activate your virtual environment (if not already active):**
    ```bash
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser.

## Project Structure

```
Multimodal-Summarizer/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
└── src/
    ├── __init__.py
    ├── main.py
    └── pipeline.py
```

*   `app.py`: The Streamlit frontend application.
*   `src/main.py`: Entry point for the summarization logic, calling the pipeline.
*   `src/pipeline.py`: Contains the core multimodal summarization pipeline, including functions for PDF extraction, audio/video processing, transcription, and text summarization.
*   `requirements.txt`: Lists all Python dependencies.
*   `.gitignore`: Specifies intentionally untracked files to ignore.

## Model Information

*   **Transcription:** OpenAI's Whisper (base model)
*   **Summarization:** LaMini-Flan-T5-783M (quantized version from Hugging Face)

---