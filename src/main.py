from search_engine import add_document, tokenize, build_index, search, ranking

documents: dict[str, dict[str, str]] = {}
inverted_index: dict[str, dict[str, list[int]]] = {}


def main() -> None:
    for file in ["doc1.txt", "doc2.txt", "doc3.txt"]:
        id, content = add_document(f"./data/{file}")
        documents[id] = {"file": file, "content": content}
        words = tokenize(content)
        new_index = build_index(words, id)
        for key, value in new_index.items():
            if key not in inverted_index:
                inverted_index[key] = value
            else:
                inverted_index[key].update(value)
    search_result = search("programming", inverted_index, and_mode=False)
    print(inverted_index)
    if search_result is None:
        print("Could not find any documents matching your query.")
    ranking(search_result, inverted_index, documents)


if __name__ == "__main__":
    main()
