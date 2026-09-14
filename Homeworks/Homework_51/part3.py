from google import genai
from google.genai import errors
from dotenv import load_dotenv
import os

load_dotenv(".env")

API_KEY = os.getenv("GEMINI_API_KEY")


def error_handler():

    try:
        client = genai.Client(api_key=None)
        client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Hello",
        )
    except Exception as e:
        print(f"[{type(e).__name__}] API გასაღები არ არის მითითებული.")
        print("დააყენეთ გარემოს ცვლადი GEMINI_API_KEY, ან შექმენით .env ფაილი")

    try:
        client = genai.Client(api_key="not-a-real-key")
        client.models.generate_content(
            model="gemini-3.6-flash",
            contents="Hello",
        )
    except errors.ClientError as e:
        print(f"[status: {e.code}] API გასაღები არასწორია.")
        print("პრობლემა აირს credentials-ში და არა კოდის სინტაქსში.შეამოწმეთ გასაღების სისწორე.")

    try:
        client = genai.Client(api_key=API_KEY)
        client.models.generate_content(
            model="gemini-nonexistent-model-123",
            contents="Hello",
        )
    except errors.ClientError as e:
        print(f"[status: {e.code}] მითითებული მოდელი არ არსებობს.")
        print(f"გამოიყენეთ ვალიდური მოდელის სახელი, მაგალითად: (gemini-2.0-flash)")

    try:
        client = genai.Client(api_key=API_KEY)
        client.models.generate_content(
            model="gemini-3.6-flash",
            contents="Hello",
            config={"invalid_param": True}
        )
    except Exception as e:
        print(f"[{type(e).__name__}] მოულოდნელი შეცდომა API-სთან კომუნიკაციისას.")
        print(f"შესაძლოა კონფიგურაცია იყოს არასწორი. დეტალური ინფორმაცია: {e}")


if __name__ == "__main__":
    error_handler()


