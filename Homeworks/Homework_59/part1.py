from dotenv import load_dotenv
from typing import Union
from langchain_core.tools import tool, render_text_description
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents.output_parsers import ReActSingleInputOutputParser
from langchain_classic.agents.format_scratchpad import format_log_to_str
from langchain_core.agents import AgentAction, AgentFinish

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


def find_tool_by_name(tools_list, tool_name):
    for t in tools_list:
        if t.name == tool_name:
            return t

    raise ValueError(f'Tool {tool_name} not found')


def run_tool(tool_to_use, tool_input):
    tool_for_run = find_tool_by_name(tools, tool_to_use)

    cleaned = str(tool_input).strip().strip('"').strip("'").strip()


    if cleaned in ('', '{}'):
        return str(tool_for_run.func())

    return str(tool_for_run.func(cleaned))


def build_agent(prompt):
    llm = ChatGoogleGenerativeAI(
        model='gemini-3.6-flash',
        temperature=0
    )


    llm_with_stop = llm.bind(stop=['\nObservation:', 'Observation:'])

    chain = ({
                 'input': lambda x: x['input'],
                 'agent_scratchpad': lambda x: format_log_to_str(x['agent_scratchpad'])
             }
             | prompt
             | llm_with_stop
             | ReActSingleInputOutputParser()
             )

    return chain


def main():
    template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

IMPORTANT RULES:
- Output ONLY ONE Thought and ONE Action per response, then STOP and wait for the Observation.
- NEVER write the Observation yourself. It will be provided to you.
- NEVER write Action and Final Answer in the same response.
- If a tool takes no input, write: Action Input: {{}}
- Write the Action Input as plain text without quotes.
- Write the Final Answer in the same language as the Question.

Begin!

Question: {input}
Thought: {agent_scratchpad}"""

    question = 'რომელ თაროზე და რა სართულზეა ბიბლიოთეკაში ამჟამად ყველაზე მოთხოვნადი წიგნი?'
    intermediate_steps = []

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=', '.join([t.name for t in tools])
    )

    agent = build_agent(prompt)

    max_steps = 5
    for step in range(max_steps):
        print(f'\n===== Step {step + 1} =====')

        agent_step: Union[AgentAction, AgentFinish] = agent.invoke(
            {'input': question, 'agent_scratchpad': intermediate_steps}
        )

        if isinstance(agent_step, AgentFinish):
            print(agent_step.log.strip())
            return agent_step.return_values['output']

        print(agent_step.log.strip())
        print(f'Action: {agent_step.tool}')
        print(f'Action Input: {agent_step.tool_input}')

        observation = run_tool(agent_step.tool, agent_step.tool_input)
        print(f'Observation: {observation}')

        intermediate_steps.append((agent_step, observation))

    return 'Stopped after reaching max_steps without a final answer'


if __name__ == '__main__':
    print('\nFinal Answer:', main())