from search_engine import add_document, tokenize, build_index, search

documents: dict[str, dict[str, str]] = {}
inverted_index: dict[str, tuple[str, list[int]]] = {}


def main() -> None:
    for file in ["doc1.txt", "doc2.txt", "doc3.txt"]:
        id, content = add_document(f"./data/{file}")
        documents[id] = {"file": file, "content": content}
        words = tokenize(content)
        index = build_index(words, id)
        for key, value in index.items():
            if key not in inverted_index:
                inverted_index[key] = [value]
            else:
                inverted_index[key].append(value)
    print(inverted_index)
    doc_ids = search(inverted_index)
    result = [documents[doc_id]["file"] for doc_id in doc_ids]
    print(result)


if __name__ == "__main__":
    main()
