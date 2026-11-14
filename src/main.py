from search_engine import serach_tokenizer, add_document

documents: dict[str, str] = {}


def main():
    print(serach_tokenizer("Hello word !"))
    for path in [
        "./src/data/information_retrieval.txt",
        "./src/data/python_basics.txt",
    ]:
        document = add_document(path)
        if document:
            documents[document[0]] = document[1]
    print(documents)


if __name__ == "__main__":
    main()
