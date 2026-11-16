import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")
STOP_WORDS = set(stopwords.words("english"))
stemmer = PorterStemmer()


def document_tokenizer(text: str) -> list[tuple[int, str]]:
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)
    words = [stemmer.stem(word) for word in words]
    return [(i, word) for i, word in enumerate(words) if word not in STOP_WORDS]


def search_tokenizer(query: str) -> list[str]:
    query = query.lower()
    words = re.findall(r"\b\w+\b", query)
    return [stemmer.stem(word) for word in words if word not in STOP_WORDS]
