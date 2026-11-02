import re

STOP_WORDS = {"is", "a", "the", "and", "or", "in", "on", "of", "to"}


def tokenize(text: str) -> list[str]:
    text = text.lower()
    return [word for word in re.split(r"\W+", text) if word not in STOP_WORDS]
