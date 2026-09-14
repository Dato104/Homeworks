from dotenv import load_dotenv
from google import genai
from google.genai import types
import os



load_dotenv(".env")


MODEL = "gemini-3.6-flash"
API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


history = []

for i in range(22):
    history.append(types.UserContent(f"How many days are in a month?(User Content Turn: {i})"))
    history.append(types.ModelContent(f"There are either 28,29,30 or 31 days in a month(Model Content Turn: {i})"))


def trim_history(history: list, max_turns: int):

    trimmed_history = history[-max_turns:]
    return trimmed_history

def count_history_tokens(contents):
    response = client.models.count_tokens(
        model=MODEL,
        contents=contents
    )
    return response.total_tokens




print(f"ტოკენების რაოდენობა ჯამში: {count_history_tokens(history)}")

trimmed_history_1 = trim_history(history=history, max_turns=4)
# print(trimmed_history_1)
print(f"1 დარჩენილი შეტყობინებების რაოდენობა: {len(trimmed_history_1) * 2}")
print(f"დარჩენილი ტოკენების რაოდენობა: {count_history_tokens(trimmed_history_1)}")

trimmed_history_2 = trim_history(history=history, max_turns=6)
# print(trimmed_history_2)
print(f"2 დარჩენილი შეტყობინებების რაოდენობა: {len(trimmed_history_2) * 2}")
print(f"დარჩენილი ტოკენების რაოდენობა: {count_history_tokens(trimmed_history_2)}")

trimmed_history_3 = trim_history(history=history, max_turns=10)
# print(trimmed_history_3)
print(f"3 დარჩენილი შეტყობინებების რაოდენობა: {len(trimmed_history_3) * 2}")
print(f"დარჩენილი ტოკენების რაოდენობა: {count_history_tokens(trimmed_history_3)}")










