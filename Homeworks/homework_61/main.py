from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import tool
from langchain_core.messages import BaseMessage, ToolMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.graph import START, END, StateGraph
from typing import TypedDict, Annotated

load_dotenv()

CHAT_MODEL = 'gemini-3.6-flash'


def make_model():
    chat = ChatGoogleGenerativeAI(model=CHAT_MODEL)
    return chat



class TextState(TypedDict):
    user_request: str
    text: str
    response: str


def summarize_node(state: TextState):
    print('Calling summarize_node')
    chat = make_model()
    prompt = f'შეაჯამე შემდეგი ტექსტი 2-3 წინადადებით:\n\n{state["text"]}'
    result = chat.invoke(prompt)
    return {'response': result.text}


def translate_node(state: TextState):
    print('Calling translate_node')
    chat = make_model()
    prompt = f'Translate the following text to English:\n\n{state["text"]}'
    result = chat.invoke(prompt)
    return {'response': result.text}


def route_by_request(state: TextState):
    request = state['user_request'].lower()
    if 'შეჯამება' in request or 'summary' in request:
        return 'summarize'
    else:
        return 'translate'


def build_text_graph():
    builder = StateGraph(TextState)

    builder.add_node('summarize', summarize_node)
    builder.add_node('translate', translate_node)

    builder.add_conditional_edges(
        START,
        route_by_request,
        {'summarize': 'summarize', 'translate': 'translate'}
    )

    builder.add_edge('summarize', END)
    builder.add_edge('translate', END)

    return builder.compile()


def main_task1():
    graph = build_text_graph()

    text = (
        'თბილისი საქართველოს დედაქალაქია და მდებარეობს მდინარე მტკვრის ორივე ნაპირზე. '
        'ქალაქი დაარსდა V საუკუნეში და მას შემდეგ მრავალი ისტორიული მოვლენის მომსწრე გახდა. '
        'დღეს თბილისი მნიშვნელოვანი კულტურული და ტურისტული ცენტრია.'
    )

    result1 = graph.invoke({
        'user_request': 'გთხოვ, გააკეთე ამ ტექსტის შეჯამება',
        'text': text,
        'response': ''
    })
    print('--- Summary ---')
    print(result1['response'])

    result2 = graph.invoke({
        'user_request': 'გადათარგმნე ეს ტექსტი',
        'text': text,
        'response': ''
    })
    print('--- Translation ---')
    print(result2['response'])



class AssistantState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


@tool
def get_book_info(title: str):
    '''Get information about a book by its title'''
    fake_data = {
        '1984': 'Author: George Orwell, Year: 1949, Description: A dystopian novel about totalitarian surveillance and control.',
        'The Hobbit': 'Author: J.R.R. Tolkien, Year: 1937, Description: A fantasy adventure of Bilbo Baggins and a dragon.',
        'Dune': 'Author: Frank Herbert, Year: 1965, Description: A sci-fi epic about politics and power on a desert planet.',
    }
    return fake_data.get(title, 'Unknown')


@tool
def get_movie_info(title: str):
    '''Get information about a movie by its title'''
    fake_data = {
        'Inception': 'Director: Christopher Nolan, Year: 2010, Genre: Sci-Fi / Thriller',
        'The Matrix': 'Director: The Wachowskis, Year: 1999, Genre: Sci-Fi / Action',
        'Titanic': 'Director: James Cameron, Year: 1997, Genre: Romance / Drama',
    }
    return fake_data.get(title, 'Unknown')


TOOL_FUNCTIONS = {'get_book_info': get_book_info, 'get_movie_info': get_movie_info}


def call_model(state: AssistantState):
    chat = make_model().bind_tools([get_book_info, get_movie_info])
    response = chat.invoke(state['messages'])
    return {'messages': response}


def call_tools(state: AssistantState):
    last_message = state['messages'][-1]

    tool_messages = []
    for tool_call in last_message.tool_calls:
        tool_function = TOOL_FUNCTIONS[tool_call['name']]
        result = tool_function.invoke(tool_call['args'])
        tool_messages.append(ToolMessage(content=str(result), tool_call_id=tool_call['id']))

    return {'messages': tool_messages}


def should_continue(state: AssistantState):
    last_message = state['messages'][-1]
    if last_message.tool_calls:
        return 'call_tools'
    else:
        return END


def build_tool_graph():
    builder = StateGraph(AssistantState)

    builder.add_node('call_model', call_model)
    builder.add_node('call_tools', call_tools)

    builder.add_edge(START, 'call_model')
    builder.add_conditional_edges('call_model', should_continue, {'call_tools': 'call_tools', END: END})
    builder.add_edge('call_tools', 'call_model')

    return builder.compile()


def main_task2():
    graph = build_tool_graph()
    result = graph.invoke(
        {
            'messages': [
                HumanMessage('მითხარი რამე წიგნზე "1984" და ფილმზე "Inception"')
            ]
        },
        config={'recursion_limit': 10}
    )

    for message in result['messages']:
        print(f'[{message.__class__.__name__}]: {message.text}')


if __name__ == '__main__':
    main_task1()
    print('\n' + '=' * 60 + '\n')
    main_task2()

