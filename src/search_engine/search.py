def search(
    query: str, inverted_index: dict[str, dict[str, list[int]]], and_mode: bool = True
) -> list[str] | None:
    query_terms = query.split()
    results = set()
    for term in query_terms:
        if not and_mode and term in inverted_index:
            results.update(inverted_index[term].keys())
        elif and_mode and term in inverted_index:
            if not results:
                results = set(inverted_index[term].keys())
            else:
                results.intersection_update(inverted_index[term].keys())
        elif and_mode and term not in inverted_index:
            return None
    return list(results) if results else None
