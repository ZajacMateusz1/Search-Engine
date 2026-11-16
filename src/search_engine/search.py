import math
from search_engine.tokenizer import search_tokenizer


def search(
    query: str,
    inverse_index: dict[str, dict[str, list[int]]],
    documents: dict[str, str],
):
    result: dict[str, int] = {}
    query_tokens = search_tokenizer(query)
    all_tokens = len(query_tokens)
    for token in query_tokens:
        for document in documents.keys():
            tf = calculate_tf(document, token, inverse_index, all_tokens)
            idf = calculate_idf(documents, token, inverse_index)
            result[document] = result.get(document, 0) + (tf * idf)
    return sorted(result.items(), key=lambda x: x[1], reverse=True)


def calculate_tf(
    doc_id: str,
    token: str,
    inverse_index: dict[str, dict[str, list[int]]],
    all_tokens: int,
):
    token_count = len(inverse_index.get(token, {}).get(doc_id, []))
    return token_count / all_tokens


def calculate_idf(
    documents: dict[str, str],
    token: str,
    inverse_index: dict[str, dict[str, list[int]]],
):
    document_count = len(documents)
    token_document_count = len(inverse_index.get(token, {}))
    if token_document_count == 0:
        return 0
    return math.log(document_count / token_document_count)
