import os
import yt_dlp
from moviepy import VideoFileClip
import tempfile
import shutil
from speechbrain.pretrained import EncoderClassifier
from google import genai
import torch
import numpy as np

# Set the audio backend to 'soundfile' for compatibility with SpeechBrain
# torchaudio.set_audio_backend("soundfile")


model = EncoderClassifier.from_hparams(source="pretrained_models")
label_encoder = model.hparams.label_encoder
print(label_encoder.decode_torch(np.arange(len(label_encoder))))


def download_video_temp(url: str, filename: str = "video.mp4") -> str:
    """
    Downloads the video to a temporary directory using yt_dlp and returns the video path.
    """
    temp_dir = tempfile.mkdtemp()
    output_path = os.path.join(temp_dir, filename)
    print(f"Downloading video from {url} to {output_path}...")
    ydl_opts = {
        "outtmpl": output_path,
        "format": "mp4/best",
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"Video downloaded to: {output_path}")
    return output_path, temp_dir


def extract_audio(video_path: str, audio_path: str):
    """
    Extracts audio from the video file and saves it as MP3 or WAV.
    """
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(
        audio_path,
        fps=16000,
    )
    clip.close()
    print(f"Audio extracted and saved to: {audio_path}")


def classify_audio(audio_path: str):
    """
    Classify the audio file using the pre-trained accent identification model.
    """

    logits, _, index, pred = model.classify_file(audio_path)
    predicted_label = pred[0]
    print(f"Probabilities: {logits}")
    print(f"Index: {index}")
    print(f"Prediction: {predicted_label}")

    # Add batch dimension

    # Convert logits to probabilities (softmax)
    probs = torch.softmax(logits, dim=1).squeeze(0)
    probability = f"{probs[index][0] * 100:0.2f}%"

    print(f"Probabilities: {probs}")
    print(probability)

    return


def generate_explanation(pred):
    """
    Generate a user-friendly explanation of the accent prediction using Google GenAI.
    """
    client = genai.Client(api_key="AIzaSyALf-KDrwjwjntX9iLi7g3Gyo1hWCQrHAw")

    prompt = f"""
                Do not use latex, bold, or italic styling. Analyze this accent prediction from an audio file:  
                - Predicted accent: {pred[0]}  

                Provide a concise, user-friendly explanation as a single paragraph:  
                1. The most likely accent  
                2. Brief reasoning in simple terms  
            """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text


def main():
    # 🔧 Set your video URL and audio output filename
    video_url = "https://www.loom.com/share/ed2e41bee0de406a8580967d35e76b09"
    output_audio_path = "audio.wav"  # or "audio.wav"

    print("Downloading video...")
    video_path, temp_dir = download_video_temp(video_url)

    try:
        print("Extracting audio...")
        extract_audio(video_path, output_audio_path)
        print(f"✅ Audio saved as: {output_audio_path}")
        print("Classifying audio...")
        classify_audio(output_audio_path)
    finally:
        # Clean up the temporary directory and video file
        shutil.rmtree(temp_dir)
        print("Temporary files cleaned up.")


if __name__ == "__main__":
    main()
