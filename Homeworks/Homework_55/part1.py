from google.genai import Client
from dotenv import load_dotenv
import numpy as np


load_dotenv()

client = Client()


def cosine_similarity(vec_a, vec_b):
    a = np.array(vec_a)
    b = np.array(vec_b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))



dog_vector = client.models.embed_content(
    model="gemini-embedding-2",
    contents="A small dog running in the park"
)

puppy_vector = client.models.embed_content(
    model="gemini-embedding-2",
    contents="A puppy playing outside"
)

laptop_vector = client.models.embed_content(
    model="gemini-embedding-2",
    contents="A new laptop with a fast processor"
)

python_vector = client.models.embed_content(
    model="gemini-embedding-2",
    contents="I love programming in Python"
)

programming_vector = client.models.embed_content(
    model="gemini-embedding-2",
    contents="Python is a great programming language"
)

france_vector = client.models.embed_content(
    model="gemini-embedding-2",
    contents="The capital of France is Paris"
)


filtered_dog_vector = dog_vector.embeddings[0].values
filtered_puppy_vector = puppy_vector.embeddings[0].values
filtered_laptop_vector = laptop_vector.embeddings[0].values
filtered_python_vector = python_vector.embeddings[0].values
filtered_programming_vector = programming_vector.embeddings[0].values
filtered_france_vector = france_vector.embeddings[0].values


cosine_dog_puppy = cosine_similarity(filtered_dog_vector, filtered_puppy_vector)
cosine_dog_laptop = cosine_similarity(filtered_dog_vector, filtered_laptop_vector)
cosine_python_programming = cosine_similarity(filtered_python_vector, filtered_programming_vector)
cosine_python_france = cosine_similarity(filtered_python_vector, filtered_france_vector)

print(f"1. {cosine_dog_puppy}")
print(f"2. {cosine_dog_laptop}")
print(f"3. {cosine_python_programming}")
print(f"4. {cosine_python_france}")

