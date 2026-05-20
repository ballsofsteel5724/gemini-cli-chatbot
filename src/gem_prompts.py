import os
from google import genai
from google.genai import types

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("[Error]: GEMINI_API_KEY environment variable not found")
    
client = genai.Client(api_key = api_key)

def start_chat_session():
    """
    Initializes a continuous chat session with Gemini so it remembers the context
    of the conversation automatically.
    """



    chat = client.chats.create(
        model = 'gemini-2.5-flash',
        config = types.GenerateContentConfig(
            temperature = 0.7,
        )
    )
    return chat