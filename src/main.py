from search_engine import add_document, tokenize, build_index, search

documents: dict[str, dict[str, str]] = {}
inverted_index: dict[str, dict[str, list[int]]] = {}


def main() -> None:
    for file in ["doc1.txt", "doc2.txt", "doc3.txt"]:
        id, content = add_document(f"./data/{file}")
        documents[id] = {"file": file, "content": content}
        words = tokenize(content)
        inverted_index.update(build_index(words, id))
    search_result = search("python backend ai", inverted_index, and_mode=False)
    if search_result is None:
        print("Could not find any documents matching your query.")
    else:
        results = [documents[doc_id] for doc_id in search_result]
        for result in results:
            print(f"{result['file']}: {result['content']}")


if __name__ == "__main__":
    main()
