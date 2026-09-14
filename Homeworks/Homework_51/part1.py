from google import genai
from google.genai import types
from dotenv import load_dotenv
import os


# ფაილის ატვირთვა ვერ მოვახერხე გიტმა არ ამატვირთვინა, მგონი რაღაც .env ფაილის პრობლემა არის ვერ გავიგე

load_dotenv(".env")


MODEL = "gemini-3.6-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

system_prompt_friendly = "You are direct, friendly and understandable assistant"

messages = [
    types.UserContent("Hello, can you tell me how many days are in a week?"),
    types.ModelContent("Yes, there are seven days in a week"),
    types.UserContent("How many days are in a year?"),
    types.ModelContent("there are 365 days in a year"),
    types.UserContent("What was my first question?"),
]

response = client.models.generate_content(
    model=MODEL,
    contents=messages,
    config=types.GenerateContentConfig(temperature=0, system_instruction=system_prompt_friendly)
)

usage_metadata = response.usage_metadata

print(response.text)
print(f"prompt token count: {usage_metadata.prompt_token_count}")
print(f"candidates token count: {usage_metadata.candidates_token_count}")
print(f"thoughts token count: {usage_metadata.thoughts_token_count}")
print(f"total token count: {usage_metadata.total_token_count}")




