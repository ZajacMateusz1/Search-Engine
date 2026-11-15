import re
from search_engine.stop_words import STOP_WORDS


def document_tokenizer(text: str) -> list[tuple[int, str]]:
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)
    return [(i, word) for i, word in enumerate(words) if word not in STOP_WORDS]


def search_tokenizer(query: str) -> list[str]:
    query = query.lower()
    words = re.findall(r"\b\w+\b", query)
    return [word for word in words if word not in STOP_WORDS]
