import yt_dlp


def download_video_temp(url: str, video_path) -> str:
    """
    Downloads the video to a temporary directory.
    """
    try:
        ydl_opts = {
            "outtmpl": video_path,
            "format": "mp4/best",
            "quiet": True,
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception:
        raise Exception(
            "Failed to download video. Please check the URL or your internet connection."
        )
