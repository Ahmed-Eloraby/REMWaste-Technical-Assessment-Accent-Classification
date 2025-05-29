from moviepy import VideoFileClip


def extract_audio(video_path: str, audio_path) -> str:
    """
    Extracts audio from the video file and saves it as WAV.
    """
    try:
        clip = VideoFileClip(video_path)

        clip.audio.write_audiofile(
            audio_path,
            fps=16000,
        )
        clip.close()
    except Exception as e:
        raise Exception(f"Failed to extract audio: {e}")
