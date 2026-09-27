
def get_weather(city: str):
    mock_data_weather = {
        'Tbilisi': {'condition': 'Sunny', 'temperature_c': 25},
        'New-York': {'condition': 'Rainy', 'temperature_c': 20},
        'Baku': {'condition': 'Sunny', 'temperature_c': 26},
    }
    result = mock_data_weather.get(city, {'condition': 'Unknown', 'temperature_c': None})
    return result


def search_news(topic: str):
    return f'Some news about {topic}'


def calculate(expression: str):
    try:
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}


def get_currency_rate(from_currency: str, to_currency: str):
    rates = {
        ("USD", "GEL"): 2.71,
        ("EUR", "USD"): 1.08,
        ("EUR", "GEL"): 2.92,
        ("USD", "EUR"): 0.93,
    }
    rate = rates.get((from_currency.upper(), to_currency.upper()))
    if rate is None:
        return {"error": "კურსი ვერ მოიძებნა"}
    return {"rate": rate}


weather_tool_schema = {
    'name': 'get_weather',
    'description': 'Get current weather condition for a given city',
    'parameters': {
        'type': 'object',
        'properties': {
            'city': {'type': 'string', 'description': 'The name of the city, e.g. Tbilisi'}
        },
        'required': ['city']
    }
}

news_tool_schema = {
    'name': 'search_news',
    'description': 'Search news about given topic',
    'parameters': {
        'type': 'object',
        'properties': {
            'topic': {'type': 'string', 'description': 'Topic to search news for.'}
        },
        'required': ['topic']
    }
}

calculate_tool_schema = {
    'name': 'calculate',
    'description': 'Evaluate a mathematical expression and return the numeric result.',
    'parameters': {
        'type': 'object',
        'properties': {
            'expression': {'type': 'string', 'description': 'A mathematical expression, e.g. "27 * 14"'}
        },
        'required': ['expression']
    }
}

currency_tool_schema = {
    'name': 'get_currency_rate',
    'description': 'Get the mock exchange rate between two currencies.',
    'parameters': {
        'type': 'object',
        'properties': {
            'from_currency': {'type': 'string', 'description': 'Currency code to convert from, e.g. USD'},
            'to_currency': {'type': 'string', 'description': 'Currency code to convert to, e.g. GEL'}
        },
        'required': ['from_currency', 'to_currency']
    }
}