from typing import List
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
from pydantic import BaseModel


load_dotenv(".env")


MODEL = "gemini-3.6-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


class Book(BaseModel):
    title: str
    author: str
    year: int
    genres: List[str]


txt = "Recommend a book from any genre for me to read."

prompt = f"Extract information from {txt}"

response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.1,
        response_schema=Book,
        response_mime_type="application/json",
    )
)

book = Book.model_validate_json(response.text)
# print(book)
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.year}")
print(f"Genres: {book.genres}")






