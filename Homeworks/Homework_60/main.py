from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import START, END, StateGraph
from typing import TypedDict


load_dotenv()


CHAT_MODEL = "gemini-3.6-flash"

RAW_IDEA = '''
We spend too much time on our phones.   

It hurts our eyes
and also affects our sleep quality.
'''

class Pipeline(TypedDict):
    raw_idea: str
    cleaned_idea: str
    expanded_content: str
    final_post: str


def clean_idea(state: Pipeline):
    cleaned = state["raw_idea"].strip().replace("\n", " ")
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    return {"cleaned_idea": cleaned}


def expand_content(state: Pipeline):
    chat = ChatGoogleGenerativeAI(model=CHAT_MODEL)
    question = f"Expand this idea into fully developed text(min of 4-6 sentences): \n\n{state["cleaned_idea"]}"

    response = chat.invoke(question)
    return {"expanded_content": response.text}

def create_final_post(state: Pipeline):
    chat = ChatGoogleGenerativeAI(model=CHAT_MODEL)
    question = (
        "Turn this text into a ready-to-publish blog post. "
        "Add a catchy title at the top and a short conclusion at the end:\n\n"
        f"{state['expanded_content']}"
    )

    response = chat.invoke(question)
    return {"final_post": response.text}


def build_graph():
    builder = StateGraph(Pipeline)

    builder.add_node("clean_idea", clean_idea)
    builder.add_node("expand_content", expand_content)
    builder.add_node("create_final_post", create_final_post)

    builder.add_edge(START, "clean_idea")
    builder.add_edge("clean_idea", "expand_content")
    builder.add_edge("expand_content", "create_final_post")
    builder.add_edge("create_final_post", END)

    return builder.compile()


def run_graph():
    graph = build_graph()

    result = graph.invoke({"raw_idea": RAW_IDEA})

    print(result["final_post"])


run_graph()


