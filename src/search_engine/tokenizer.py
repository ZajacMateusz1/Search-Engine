import re
from search_engine.stop_words import STOP_WORDS


def document_tokenizer(text: str) -> list[str]:
    pass


def serach_tokenizer(query: str) -> list[str]:
    words = re.findall(r"\b\w+\b", query)
    return [word for word in words if word not in STOP_WORDS]
