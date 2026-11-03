from search_engine import add_document, tokenize, build_index

inverted_index = {}


def main() -> None:
    document = add_document("./data/doc1.txt")
    words = tokenize(document)
    # print(words, len(words))
    index = build_index(words)
    for key, value in index.items():
        if key not in inverted_index:
            inverted_index[key] = [value]
        else:
            inverted_index[key].append(value)
    print(inverted_index)


if __name__ == "__main__":
    main()
