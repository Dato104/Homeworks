from dotenv import load_dotenv
from google.genai import Client
from google.genai import types
from tools import (
    get_weather, search_news, calculate, get_currency_rate,
    weather_tool_schema, news_tool_schema,
    calculate_tool_schema, currency_tool_schema,
)

load_dotenv()

MODEL = 'gemini-3.6-flash'

TOOL_REGISTRY = {
    'get_weather': lambda kwargs: get_weather(**kwargs),
    'search_news': lambda kwargs: search_news(**kwargs),
    'calculate': lambda kwargs: calculate(**kwargs),
    'get_currency_rate': lambda kwargs: get_currency_rate(**kwargs),
}

weather_tool = types.Tool(function_declarations=[weather_tool_schema])
news_tool = types.Tool(function_declarations=[news_tool_schema])
calculate_tool = types.Tool(function_declarations=[calculate_tool_schema])
currency_tool = types.Tool(function_declarations=[currency_tool_schema])

config = types.GenerateContentConfig(
    tools=[weather_tool, news_tool, calculate_tool, currency_tool]
)

client = Client()

questions = [
    'გამოთვალე 27 * 14.',
    'რა არის 125 გაყოფილი 5-ზე.',
    'მითხარი რა კურსია ევროს დოლართან?',
    'გამოთვალე (18 + 7) * 3',
]

for question in questions:
    print(f"\n=== კითხვა: {question} ===")

    response = client.models.generate_content(
        model=MODEL,
        contents=question,
        config=config
    )

    function_responses = []
    for part in response.parts:
        if part.function_call:
            call = part.function_call
            result = TOOL_REGISTRY[call.name](dict(call.args))

            function_response_part = types.Part.from_function_response(
                name=call.name, response={'result': result}
            )
            function_responses.append(function_response_part)
        else:
            if part.text:
                print(part.text)

    if function_responses:
        follow_up = client.models.generate_content(
            model=MODEL,
            contents=[question, response.parts, function_responses],
            config=config
        )
        print(follow_up.text)

