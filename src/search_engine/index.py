def build_index(tokens: list[tuple[int, str]]) -> dict:
    local_index = {}
    for i, token in tokens:
        if token not in local_index:
            local_index[token] = [i]
        else:
            local_index[token].append(i)
    return local_index
