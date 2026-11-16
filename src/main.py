from search_engine import (
    document_tokenizer,
    add_document,
    add_to_index,
    search,
)

documents: dict[str, str] = {}
inverse_index: dict[str, dict[str, list[int]]] = {}


def main():
    for path in [
        "./src/data/information_retrieval.txt",
        "./src/data/python_basics.txt",
    ]:
        document = add_document(path)
        if not document:
            continue
        id, content = document
        documents[id] = content
        tokens = document_tokenizer(content)

        add_to_index(inverse_index, tokens, id)
    result = search("Python is great!", inverse_index, documents)
    for document, score in result:
        print(f"{document}: {documents[document]} (score: {score}) \n")


if __name__ == "__main__":
    main()
