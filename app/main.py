from pathlib import Path


def load_documents():
    data_folder = Path("data")
    documents = {}

    for file_path in data_folder.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        documents[file_path.name] = text

    return documents


def search_documents(documents, query):
    query_words = query.lower().split()
    results = []

    for filename, text in documents.items():
        text_lower = text.lower()
        score = 0

        for word in query_words:
            score += text_lower.count(word)

        if score > 0:
            results.append((filename, score))

    results.sort(key=lambda result: result[1], reverse=True)

    return results


def main():
    documents = load_documents()

    query = input("What do you want to search for? ")

    results = search_documents(documents, query)

    print("\nSearch results:")

    if not results:
        print("No matching documents found.")
        return

    for filename, matches in results:
        print(f"- {filename} ({matches} matching words)")


if __name__ == "__main__":
    main()