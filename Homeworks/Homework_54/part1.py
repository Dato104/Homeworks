from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

MODEL = "gemini-3.6-flash"
chat_gemini = ChatGoogleGenerativeAI(model=MODEL)


class Book(BaseModel):
    title: str
    author: str
    year: int
    genres: list[str]
    pages: int


structured_model = chat_gemini.with_structured_output(Book)


response = structured_model.invoke("George Orwell's famous novel 1984 was published in 1949. It is a dystopian political fiction book with 328 pages.")
print(f"Title: {response.title}")
print(f"Author: {response.author}")
print(f"Year: {response.year}")
print(f"Genres: {response.genres}")
print(f"Pages: {response.pages}")



