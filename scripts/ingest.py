import os

from services.pdf_service import extract_pages
from services.chunk_service import create_chunks
from services.embedding_service import get_embedding
from services.vector_service import insert_chunk


# =====================================================
# Configuration
# =====================================================

DATA_FOLDER = "data"


# =====================================================
# Ingest Single PDF
# =====================================================

def ingest_pdf(pdf_path):

    filename = os.path.basename(pdf_path)

    print("\n" + "=" * 60)
    print(f"Processing : {filename}")
    print("=" * 60)

    # ------------------------------------------
    # Extract pages
    # ------------------------------------------

    pages = extract_pages(pdf_path)

    print(f"Pages      : {len(pages)}")

    # ------------------------------------------
    # Create chunks
    # ------------------------------------------

    chunks = create_chunks(pages)

    print(f"Chunks     : {len(chunks)}")

    # ------------------------------------------
    # Process each chunk
    # ------------------------------------------

    for index, chunk in enumerate(chunks, start=1):

        print(f"Embedding Chunk {index}/{len(chunks)}")

        embedding = get_embedding(
            chunk["content"]
        )

        insert_chunk(
            chunk=chunk,
            filename=filename,
            embedding=embedding
        )

    print(f"Finished : {filename}")


# =====================================================
# Main
# =====================================================

def main():

    if not os.path.exists(DATA_FOLDER):

        print(f"Folder '{DATA_FOLDER}' not found.")

        return

    pdf_files = [
        file
        for file in os.listdir(DATA_FOLDER)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:

        print("No PDF files found.")

        return

    print("=" * 60)
    print(f"Found {len(pdf_files)} PDF(s)")
    print("=" * 60)

    for pdf in pdf_files:

        ingest_pdf(
            os.path.join(DATA_FOLDER, pdf)
        )

    print("\n" + "=" * 60)
    print("All PDFs ingested successfully.")
    print("=" * 60)


# =====================================================
# Entry Point
# =====================================================

if __name__ == "__main__":
    main()