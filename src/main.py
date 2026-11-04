from search_engine import add_document, tokenize, build_index

inverted_index: dict[str, list[int]] = {}


def main() -> None:
    for path in ["./data/doc1.txt", "./data/doc2.txt", "./data/doc3.txt"]:
        id, document = add_document(path)
        words = tokenize(document)
        # print(words, len(words))
        index = build_index(words, id)
        for key, value in index.items():
            if key not in inverted_index:
                inverted_index[key] = [value]
            else:
                inverted_index[key].append(value)
    print(inverted_index)


if __name__ == "__main__":
    main()
