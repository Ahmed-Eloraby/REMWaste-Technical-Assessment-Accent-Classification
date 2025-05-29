from google import genai
from src.config import prompt_api_key


def generate_explanation(predicted_accent):
    """
    Generate a user-friendly explanation of the accent prediction using Google GenAI.
    """
    try:
        client = genai.Client(api_key=prompt_api_key)

        prompt = f"""
                    Do not use latex, bold, or italic styling. Analyze this accent prediction from an audio file:  
                    - Predicted accent: {predicted_accent}  

                    Provide a concise, user-friendly explanation as a single paragraph:  
                    1. The most likely accent  
                    2. Brief reasoning in simple terms  
                """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text
    except Exception as e:
        return ""
