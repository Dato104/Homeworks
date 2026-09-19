from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

MODEL = "gemini-3.6-flash"
chat_gemini = ChatGoogleGenerativeAI(model=MODEL)


class Product(BaseModel):
    name: str
    price: float
    currency: str
    in_stock: bool
    colors: list[str]


structured_model = chat_gemini.with_structured_output(Product)

template = PromptTemplate.from_template(
    "Extract information about products from this text"
    "\n\n{input_text}"
)

chain = template | structured_model


response = chain.invoke({"input_text": "The new wireless headphones cost 149.99 USD. Available in black, white and blue. Currently in stock."})
print(f"Name: {response.name}")
print(f"Price: {response.price}")
print(f"Currency: {response.currency}")
print(f"In stock: {response.in_stock}")
print(f"Colors: {response.colors}")



