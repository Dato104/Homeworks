from google.genai import Client
from dotenv import load_dotenv
import psycopg2


load_dotenv()

client = Client()


def get_pg_connection():
    return psycopg2.connect(user='postgres', password='datobase003', host='localhost', port='5432', database='homeworks')



connection = get_pg_connection()
cursor = connection.cursor()


input_text = input("Please input text here: ")


embedded_text = client.models.embed_content(
    model='gemini-embedding-2',
    contents=input_text
)

vector = embedded_text.embeddings[0].values
vector = '[' + ','.join(str(x) for x in vector) + ']'


cursor.execute("select id, content, vector <=> %s as distance from document order by distance limit 3", (vector, ))

rows = cursor.fetchall()

cursor.close()
connection.close()

print(f"1. [id={rows[0][0]}] distance={rows[0][2]} | content: {rows[0][1]}")
print(f"2. [id={rows[1][0]}] distance={rows[1][2]} | content: {rows[1][1]}")
print(f"3. [id={rows[2][0]}] distance={rows[2][2]} | content: {rows[2][1]}")













