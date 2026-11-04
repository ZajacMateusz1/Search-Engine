def search(inverted_index: dict[str, tuple[str, list[int]]]) -> list[str] | None:
    query = input("Provide you input: ").lower()
    if query not in inverted_index:
        return
    return [doc_id for doc_id, positions in inverted_index[query]]
