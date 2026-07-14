from services.retrieval_service import search


def retrieve_context(question: str, top_k: int = 5):
    """
    Retrieve relevant document chunks and return a
    structured response for downstream AI Agents.

    Parameters
    ----------
    question : str
        User's question.

    top_k : int
        Number of chunks to retrieve.

    Returns
    -------
    dict
        JSON-serializable retrieval response.
    """

    rows = search(question, top_k)

    results = []

    for filename, page, chunk_id, content, distance in rows:

        similarity = 1 - float(distance)

        results.append(
            {
                "text": content.strip(),
                "score": round(similarity, 4),
                "source": {
                    "document": filename,
                    "page": page
                }
            }
        )

    return {
        "question": question,
        "count": len(results),
        "context": results
    }