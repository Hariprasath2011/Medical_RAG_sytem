from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


def create_chunks(pages):

    chunks = []

    chunk_id = 0

    for page in pages:

        splits = splitter.split_text(page["text"])

        for split in splits:

            chunks.append(
                {
                    "page": page["page"],
                    "chunk_id": chunk_id,
                    "content": split
                }
            )

            chunk_id += 1

    return chunks