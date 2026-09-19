from google.genai import Client
from dotenv import load_dotenv
import psycopg2


load_dotenv()

client = Client()


def get_pg_connection():
    return psycopg2.connect(user='postgres', password='datobase003', host='localhost', port='5432', database='homeworks')


connection = get_pg_connection()
cursor = connection.cursor()

texts = [
    "A small dog running in the park",
    "A puppy playing outside",
    "A new laptop with a fast processor",
    "I love programming in Python",
    "Machine learning is a subset of artificial intelligence",
    "The weather is very cold today",
    "Cats are independent animals",
    "Deep learning uses neural networks",
]


for text in texts:
    vector = client.models.embed_content(
        model='gemini-embedding-2',
        contents=text
    )

    cursor.execute("insert into document(content, vector) values (%s, %s)", (text, vector.embeddings[0].values))


connection.commit()
cursor.close()
connection.close()



