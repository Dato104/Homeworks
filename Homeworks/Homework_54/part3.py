from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import  ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()

MODEL = "gemini-3.6-flash"
chat_gemini = ChatGoogleGenerativeAI(model=MODEL)


class FantasyQuest(BaseModel):
    quest_name: str
    hero_name: str
    enemy: str
    magical_item: str
    danger_level: int = Field(ge=1, le=10)
    reward: str
    side_quests: list[str]
    is_cursed: bool



system_message = SystemMessage(content=(
    "You are an epic fantasy chronicler. Extract quest information from the given text "
    "in a maximally epic high-fantasy style. If some information is missing from the text, "
    "invent a logical and interesting detail yourself, but always return it inside the "
    "required structure. The danger_level must be a realistic assessment (1-10) based on "
    "the information given, not an arbitrary number. Answer in the same language as the input text."
))

structured_model = chat_gemini.with_structured_output(FantasyQuest)

template = ChatPromptTemplate.from_messages([
    system_message,
    ("human", "Extract the quest information from this text:\n\n{input_text}"),
])

chain = template | structured_model

response = chain.invoke({"input_text": "ახალგაზრდა ჯადოქარი სახელად ლირა უნდა გაემგზავროს ჩრდილოეთის ტყეებში, რათა იპოვოს დაკარგული მთვარის ხმალი. გზად მას ელოდება უძველესი ტყის სული, რომელიც სძულს ადამიანებს. თუ წარმატებას მიაღწევს, მიიღებს უკვდავების ელექსირს."})
print(response)






