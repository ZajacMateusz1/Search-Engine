import math
from search_engine.tokenizer import search_tokenizer


def search(
    query: str,
    inverse_index: dict[str, dict[str, list[int]]],
    documents: dict[str, str],
):
    result: dict[str, int] = {}
    query_tokens = search_tokenizer(query)
    for token in query_tokens:
        for document in documents.keys():
            print(calculate_tf(document, token, inverse_index, documents))
            print(calculate_idf(documents, token, inverse_index))
            print(" ")
    return result


def calculate_tf(
    doc_id: str,
    token: str,
    inverse_index: dict[str, dict[str, list[int]]],
    documents: dict[str, str],
):
    token_count = len(inverse_index.get(token, {}).get(doc_id, []))
    document_length = len(documents.get(doc_id, ""))
    return token_count / document_length if document_length > 0 else 0


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
