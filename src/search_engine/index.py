def add_to_index(
    inverse_index: dict[str, dict[str, list[int]]],
    tokens: list[tuple[int, str]],
    doc_id: str,
) -> None:
    for i, word in tokens:
        if word not in inverse_index:
            inverse_index[word] = {doc_id: [i]}
        elif doc_id not in inverse_index[word]:
            inverse_index[word][doc_id] = [i]
        else:
            inverse_index[word][doc_id].append(i)
