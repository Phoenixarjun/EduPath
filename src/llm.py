from src.prompt import system_instruction
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")

message = [
    {"role": "user", "parts": [{"text": system_instruction}]}
]

def ask_tech(messages, model=model, temperature=0):
    response = model.generate_content(
        messages,
        generation_config={"temperature": temperature},
    )
    return response.text

