import os
from google import genai
from google.genai import types

def send_prompt_to_gemini(prompt: str) -> str:
    """Sends a prompt to Gemini and returns the text response."""
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "[Error]: GEMINI_API_KEY environment variable not found!"
    
    client = genai.Client(api_key = api_key)

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt,
            config = types.GenerateContentConfig(
                temperature= 0.7,
            )
        )
        return response.text.strip()

    except Exception as e:
        return f"[API Error]: {e}"