import re

STOP_WORDS = {"is", "a", "the", "and", "or", "in", "on", "of", "to"}


def tokenize(text: str) -> list[str]:
    text = text.lower()
    return [
        (i, word)
        for i, word in enumerate(re.split(r"\W+", text))
        if word and word not in STOP_WORDS
    ]
