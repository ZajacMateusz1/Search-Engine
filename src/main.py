from search_engine import add_document, tokenize, build_index, search

documents: dict[str, dict[str, str]] = {}
inverted_index: dict[str, dict[str, list[int]]] = {}


def main() -> None:
    for file in ["doc1.txt", "doc2.txt", "doc3.txt"]:
        id, content = add_document(f"./data/{file}")
        documents[id] = {"file": file, "content": content}
        words = tokenize(content)
        index = build_index(words, id)
        for key, value in index.items():
            doc_id, positions = value
            if key not in inverted_index:
                inverted_index[key] = {doc_id: positions}
            else:
                inverted_index[key][doc_id] = positions
    print(inverted_index)
    # search_result = search(inverted_index)
    # if search_result is None:
    #     print("Could not find any documents matching your query.")
    # else:
    #     results = [documents[doc_id] for doc_id in search_result]
    #     for result in results:
    #         print(f"{result['file']}: {result['content']}")


if __name__ == "__main__":
    main()
