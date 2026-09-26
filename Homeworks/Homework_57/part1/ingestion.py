from google.genai import Client
from pgvector import Vector
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector
import psycopg2

load_dotenv()

EMBEDDING_MODEL = 'gemini-embedding-2'
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
SOURCE_FILE = 'company_handbook.md'


def get_pg_connection():
    connection = psycopg2.connect(user='postgres', password='datobase003', host='localhost', port='5432', database='homeworks')
    register_vector(connection)
    return connection


def create_table_if_not_exists(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS document_chunks (
            id SERIAL PRIMARY KEY,
            source_document TEXT NOT NULL,
            chunk_index INTEGER NOT NULL,
            content TEXT NOT NULL,
            embedding vector(3072)
        );
    """)
    connection.commit()
    cursor.close()


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def embed_chunk(client: Client, chunk: str) -> Vector:
    result = client.models.embed_content(model=EMBEDDING_MODEL, contents=chunk)
    return Vector(result.embeddings[0].values)


def insert_chunk(connection, source_document: str, chunk_index: int, content: str, embedding: Vector):
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO document_chunks (source_document, chunk_index, content, embedding)
        VALUES (%s, %s, %s, %s)
        """,
        (source_document, chunk_index, content, embedding)
    )
    connection.commit()
    cursor.close()


def main():
    client = Client()
    connection = get_pg_connection()

    create_table_if_not_exists(connection)

    with open(SOURCE_FILE, 'r', encoding='utf-8') as file:
        raw_text = file.read()

    chunks = chunk_text(raw_text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)

    for index, chunk in enumerate(chunks):
        embedding = embed_chunk(client, chunk)
        insert_chunk(connection, SOURCE_FILE, index, chunk, embedding)
        print(f'Inserted chunk {index}/{len(chunks) - 1}')

    connection.close()


if __name__ == "__main__":
    main()


