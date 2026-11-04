import uuid


def build_index(tokens: list[tuple[int, str]], id: uuid.UUID) -> dict[str, list[int]]:
    local_index = {}
    for i, token in tokens:
        if token not in local_index:
            local_index[token] = (id, [i])
        else:
            local_index[token][1].append(i)
    return local_index
