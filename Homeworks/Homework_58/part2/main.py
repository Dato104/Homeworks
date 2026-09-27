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


def call_tool(name: str, kwargs: dict):
    """უსაფრთხოდ იძახებს tool-ს mapping-იდან; თუ არ არსებობს - აბრუნებს error dict-ს."""
    handler = TOOL_REGISTRY.get(name)
    if handler is None:
        return {"error": f"tool '{name}' ვერ მოიძებნა mapping-ში"}
    try:
        return handler(dict(kwargs))
    except Exception as e:
        return {"error": str(e)}


def run_question(question: str):
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
            print(f"-> tool-ის გამოძახება: {call.name}({dict(call.args)})")

            result = call_tool(call.name, call.args)

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


questions = [
    'გამოთვალე 45 * 8 და ამავე დროს მითხარი რა კურსია დოლარის ლართან და ევროს დოლართან',
    'რა არის 1000 გაყოფილი 25-ზე? ასევე მითხარი დღევანდელი კურსი USD-GEL',
    'გამოთვალე 9 ** 3 და მითხარი რა ღირს 50 ევრო ლარში',
]

for q in questions:
    run_question(q)

