from db import get_connection
from services.embedding_service import get_embedding


def search(question, top_k=5):

    embedding = get_embedding(question)

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            filename,
            page,
            chunk_id,
            content,
            embedding <=> %s::vector AS distance
        FROM medical_chunks
        ORDER BY embedding <=> %s::vector
        LIMIT %s;
        """,
        (
            embedding,
            embedding,
            top_k
        )
    )

    results = cursor.fetchall()

    cursor.close()

    conn.close()

    return results