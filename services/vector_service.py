import uuid

from db import get_connection


def insert_chunk(chunk, filename, embedding):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO medical_chunks
        (
            id,
            filename,
            page,
            chunk_id,
            content,
            embedding
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """,
        (
            str(uuid.uuid4()),
            filename,
            chunk["page"],
            chunk["chunk_id"],
            chunk["content"],
            embedding,
        )
    )

    conn.commit()

    cursor.close()

    conn.close()