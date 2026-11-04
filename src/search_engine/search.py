def search(inverted_index: dict[str, tuple[str, list[int]]]):
    query = input("Provide you input: ")
    return [doc_id for doc_id, positions in inverted_index[query]]
