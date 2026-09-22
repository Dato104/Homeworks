from google.genai import Client
from dotenv import load_dotenv
from pgvector import Vector
from pgvector.psycopg2 import register_vector
import psycopg2

load_dotenv()


def embed_chunk(client: Client, chunk_text: str):
    model = 'gemini-embedding-2'
    result = client.models.embed_content(model=model, contents=chunk_text)

    return Vector(result.embeddings[0].values)


def ingest_info_pgvector(source_document: str, chunk_index: int, content: str, embedding: Vector):
    connection = psycopg2.connect(user='postgres', password='datobase003', host='localhost', port='5432', database='homeworks')
    register_vector(connection)

    cursor = connection.cursor()

    cursor.execute('''
        insert into document_chunks(source_document, chunk_index, content, embedding)
        values (%s, %s, %s, %s)
    ''',
    (source_document, chunk_index, content, embedding)
    )

    connection.commit()
    cursor.close()
    connection.close()

    print(f'Ingestion completed for chunk {chunk_index} from {source_document}')


def search_best_results(query_text: str, top_k: int = 3, max_distance: float = 0.5) -> list:
    client = Client()
    embedded_query = embed_chunk(client, query_text)

    connection = psycopg2.connect(user='postgres', password='datobase003', host='localhost', port='5432', database='homeworks')
    register_vector(connection)

    cursor = connection.cursor()

    cursor.execute('''
        select source_document, chunk_index, content, embedding <=> %s as distance
        from document_chunks
        where embedding <=> %s < %s
        order by distance
        limit %s
    ''', (embedded_query, embedded_query, max_distance, top_k))

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    results = []
    for source_document, chunk_index, content, distance in rows:
        results.append({
            'source_document': source_document,
            'chunk_index': chunk_index,
            'content': content,
            'distance': distance
        })

    return results


def check_search_best_results():
    results = search_best_results('how much paid vacation do employees get?', top_k=3, max_distance=0.5)

    for r in results:
        print(r['source_document'], r['chunk_index'], r['distance'])
        print(r['content'])
        print('---')

check_search_best_results()




