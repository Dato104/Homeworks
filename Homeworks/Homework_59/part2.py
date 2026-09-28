from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import AgentExecutor, create_react_agent
from langsmith import Client

load_dotenv()


@tool
def get_most_requested_book() -> str:
    """Returns the title of the currently most requested book in the library."""
    return "Clean Code"


@tool
def get_book_location(book_title: str) -> str:
    """Returns the shelf and floor location of the given book."""
    locations = {
        "Clean Code": "3rd floor, shelf B-17",
        "Design Patterns": "2nd floor, shelf A-09",
        "The Pragmatic Programmer": "4th floor, shelf C-04"
    }
    return locations.get(book_title, "Book not found")


tools = [get_most_requested_book, get_book_location]

client = Client()
prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)

llm = ChatGoogleGenerativeAI(
    model='gemini-3.6-flash',
    temperature=0,
    stop=['\nObservation', 'Observation']
)

agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=5,
    return_intermediate_steps=True,
    verbose=True
)

result = agent_executor.invoke(
    {'input': 'რომელ თაროზე და რა სართულზეა ბიბლიოთეკაში ამჟამად ყველაზე მოთხოვნადი წიგნი?'}
)

print('\n===== Intermediate Steps =====')
for action, observation in result['intermediate_steps']:
    print(f'Action: {action.tool}')
    print(f'Action Input: {action.tool_input}')
    print(f'Observation: {observation}')
    print('-' * 30)

print('\nFinal Answer:', result['output'])


