from src.pipeline import multimodal_summarizer_pipeline

def get_summary(file_path, file_type):
    """
    Main function to get a summary for a given file.
    """
    summary = multimodal_summarizer_pipeline(file_path, file_type)
    return summary

if __name__ == "__main__":
    # Example usage (for testing)
    # You would replace these with actual file paths and types
    print("Testing PDF summarization (requires a dummy.pdf in the root directory)...")
    # with open("dummy.pdf", "w") as f:
    #     f.write("This is a dummy PDF content.") # This won't create a valid PDF, just for demonstration
    # pdf_summary = get_summary("dummy.pdf", "pdf")
    # print(f"PDF Summary: {pdf_summary}")

    print("\nTesting text file summarization (requires a dummy.txt in the root directory)...")
    with open("dummy.txt", "w") as f:
        f.write("This is a test text file. It contains some sentences that need to be summarized. The quick brown fox jumps over the lazy dog. This is another sentence to make it longer.")
    text_summary = get_summary("dummy.txt", "text")
    print(f"Text Summary: {text_summary}")
    import os
    os.remove("dummy.txt") # Clean up dummy file
    
    print("\nNote: Audio and video summarization require actual audio/video files and ffmpeg installed.")