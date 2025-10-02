# graph/config/llm.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("Falta GOOGLE_API_KEY. Agrégala al .env o al entorno.")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
