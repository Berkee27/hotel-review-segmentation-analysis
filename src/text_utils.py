import re
from nltk.tokenize import RegexpTokenizer


STOP_WORDS = {
    "ve", "veya", "ile", "ama", "fakat", "çok", "bir", "bu", "şu", "o",
    "da", "de", "ki", "için", "gibi", "daha", "en", "ben", "biz", "ise",
    "olarak", "her", "hiç", "kadar", "sonra", "önce", "var", "yok"
}

TOKENIZER = RegexpTokenizer(r"[A-Za-zÇĞİÖŞÜçğıöşü]+")


def clean_text(text):
    text = str(text)
    text = text.replace("İ", "i").replace("I", "ı").lower()
    text = re.sub(r"[^a-zçğıöşü\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def turkish_tokenizer(text):
    tokens = TOKENIZER.tokenize(text)

    cleaned_tokens = [
        token
        for token in tokens
        if token not in STOP_WORDS and len(token) > 2
    ]

    return cleaned_tokens