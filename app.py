from flask import Flask, request, render_template, jsonify
from src.accent_classifier import classify_audio
from src.audio_extractor import extract_audio
from src.explanation_generator import generate_explanation
from src.video_downloader import download_video_temp
from src.file_manager import TempFileManager

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/get-accent", methods=["POST"])
def get_accent():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400
    try:
        temporary_manager = TempFileManager()
        # Generate temporary file paths for audio and video
        audio_path, video_path = temporary_manager.get_audio_video_paths()
        # Download video to a temporary file
        download_video_temp(url=url, video_path=video_path)
        # Extract audio from the video
        extract_audio(video_path=video_path, audio_path=audio_path)
        # Classify the audio to get the accent
        predicted_accent, probability = classify_audio(audio_path=audio_path)
        # Generate a user-friendly explanation of the accent
        explanation = generate_explanation(predicted_accent=predicted_accent)

        res = {
            "accent": predicted_accent,
            "probability": probability,
            "summary": explanation,
        }

        return jsonify(res), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        if temporary_manager:
            temporary_manager.remove_temp_files()


if __name__ == "__main__":
    app.run()
