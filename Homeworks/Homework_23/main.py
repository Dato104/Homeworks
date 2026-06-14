import json
import requests
from pydantic import BaseModel, ValidationError
from requests.exceptions import HTTPError, ConnectTimeout

BASE_URL = "https://crudcrud.com/api/565118274a2a41d2ac8f51f345314b03"

# ---1----
class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str


# ---2----
with open("recipes.json") as file:
    recipes = json.load(file)

for item in recipes:
    try:
        recipe = Recipe(**item)
        response = requests.post(f"{BASE_URL}/recipes", json=recipe.model_dump(), timeout=5)
        response.raise_for_status()
        print(response.json())

    except HTTPError as e:
        print(f"შეცდომა: {e.response.status_code}")

    except ConnectTimeout as e:
        print("შეცდომა: სერვერი არ პასუხობს")

    except ValidationError as e:
        print(e)

# ---3----
try:
    response = requests.get(f"{BASE_URL}/recipes", timeout=5)
    response.raise_for_status()
    recipes_from_api = response.json()
    for item in recipes_from_api:
        print(f"{item['name']}: {item['cuisine']}")

except HTTPError as e:
    print(f"შეცდომა: {e.response.status_code}")

except ConnectTimeout as e:
    print("შეცდომა: სერვერი არ პასუხობს")

except ValidationError as e:
    print(e)


# # ---4----
try:
    _id = "6a2eaf46ee62c203e8572a2e"
    response = requests.get(f"{BASE_URL}/recipes/{_id}", timeout=5)
    response.raise_for_status()
    first_recipe = response.json()
    print(first_recipe)

except HTTPError as e:
    print(f"შეცდომა: {e.response.status_code}")

except ConnectTimeout as e:
    print("შეცდომა: სერვერი არ პასუხობს")

except ValidationError as e:
    print(e)



# ---5----
updated = {
    'name': 'Lobiani',
    'cuisine': 'Georgian',
    'time_minutes': '35'
}

try:
    recipe = Recipe(**updated)
    response = requests.put(f"{BASE_URL}/recipes/{_id}", json=recipe.model_dump(), timeout=5)
    response.raise_for_status()
    print("განახლდა")

except HTTPError as e:
    print(f"შეცდომა: {e.response.status_code}")

except ConnectTimeout as e:
    print("შეცდომა: სერვერი არ პასუხობს")

except ValidationError as e:
    print(e)


# ---6----

_last_id = "6a2eaf47ee62c203e8572a30"
try:
    response = requests.delete(f"{BASE_URL}/recipes/{_last_id}", timeout=5)
    response.raise_for_status()
    print("რეცეპტი წაიშალა")

    response = requests.get(f"{BASE_URL}/recipes", timeout=5)
    response.raise_for_status()
    for i in response.json():
        print(i)

except HTTPError as e:
    print(f"შეცდომა: {e.response.status_code}")

except ConnectTimeout as e:
    print("შეცდომა: სერვერი არ პასუხობს")

except ValidationError as e:
    print(e)



















