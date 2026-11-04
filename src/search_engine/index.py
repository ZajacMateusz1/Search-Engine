def build_index(
    tokens: list[tuple[int, str]], doc_id: str
) -> dict[str, tuple[str, list[int]]]:
    local_index = {}
    for i, token in tokens:
        if token not in local_index:
            local_index[token] = (doc_id, [i])
        else:
            local_index[token][1].append(i)
    return local_index
