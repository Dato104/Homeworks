from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv(".env")

MODEL = "gemini-3.6-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

system_prompt_formal = "You are professional,careful and direct working assistant"
system_prompt_friendly = "You are direct, friendly and understandable assistant"
system_prompt_joker = "You are light,ironic toned working assistant"

messages = [
    types.UserContent("can i get refund if i change my mind about purchase?"),
]

# response = client.models.generate_content(
#     model=MODEL,
#     contents=messages,
#     config=types.GenerateContentConfig(temperature=0, system_instruction=system_prompt_formal)
# )

# response = client.models.generate_content(
#     model=MODEL,
#     contents=messages,
#     config=types.GenerateContentConfig(temperature=0, system_instruction=system_prompt_friendly,)
# )


response = client.models.generate_content(
    model=MODEL,
    contents=messages,
    config=types.GenerateContentConfig(temperature=0, system_instruction=system_prompt_joker,)
)

print(response.text)


