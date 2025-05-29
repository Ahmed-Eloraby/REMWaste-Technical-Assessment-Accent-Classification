from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env


prompt_api_key = os.getenv("API_KEY")
TEMP_DIR = "TEMP"
