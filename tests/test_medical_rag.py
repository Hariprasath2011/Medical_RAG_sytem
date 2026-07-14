from services.medical_rag_service import retrieve_context


def main():

    question = input("Question: ")

    result = retrieve_context(question)

    print("\nResult")
    print("=" * 60)

    print(result)


if __name__ == "__main__":
    main()