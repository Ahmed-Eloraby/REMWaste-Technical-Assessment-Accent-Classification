import os
from src.config import TEMP_DIR
from time import time_ns


class TempFileManager:
    """
    A class to manage temporary files and directories for audio and video processing.
    Handles creation, path generation, and cleanup of temporary files.
    """

    def __init__(self):
        """
        Initialize the TempFileManager and ensure the temp directory exists.
        """
        self.create_temp_dir_if_not_exists()

    def create_temp_dir_if_not_exists(self):
        """
        Creates the temporary directory if it does not already exist.

        Returns:
            str: The path to the temporary directory.
        """
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)
        return TEMP_DIR

    def get_audio_file_path(self):
        """
        Generates a unique path for an audio file in the temporary directory.

        Returns:
            str: The path to the audio file.
        """
        audio_file_name = f"audio_{time_ns()}.wav"
        self.audio_file_path = os.path.join(TEMP_DIR, audio_file_name)
        return self.audio_file_path

    def get_video_file_path(self):
        """
        Generates a unique path for a video file in the temporary directory.

        Returns:
            str: The path to the video file.
        """
        video_file_name = f"video_{time_ns()}.mp4"
        self.video_file_path = os.path.join(TEMP_DIR, video_file_name)
        return self.video_file_path

    def remove_temp_files(self):
        """
        Removes all temporary files and the temporary directory.
        """
        if os.path.exists(self.audio_file_path):
            os.unlink(self.audio_file_path)
        if os.path.exists(self.video_file_path):
            os.unlink(self.video_file_path)

    def get_audio_video_paths(self):
        """
        Generates and returns paths for both audio and video files.

        Returns:
            tuple: A tuple containing (audio_path, video_path).
        """
        self.get_audio_file_path()
        self.get_video_file_path()
        return self.audio_file_path, self.video_file_path
