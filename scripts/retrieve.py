from services.retrieval_service import search


def main():

    print("=" * 60)
    print("Medical RAG Retriever")
    print("=" * 60)

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        results = search(question)

        print("\nTop Matching Chunks\n")

        for index, row in enumerate(results, start=1):

            filename, page, chunk_id, content, distance = row

            print("=" * 60)
            print(f"Rank      : {index}")
            print(f"Filename  : {filename}")
            print(f"Page      : {page}")
            print(f"Chunk ID  : {chunk_id}")
            print(f"Distance  : {distance:.4f}")
            print()
            print(content)
            print()


if __name__ == "__main__":
    main()