from search_engine import add_document, tokenize, build_index


def main() -> None:
    document = add_document("./data/doc1.txt")
    words = tokenize(document)
    print(words, len(words))


if __name__ == "__main__":
    main()
