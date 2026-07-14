import re


def clean_text(text: str) -> str:
    """
    Normalize retrieved text before returning it.
    """

    text = text.replace("\n", " ")

    text = re.sub(r"\s+", " ", text)

    text = text.replace("\uf0b7", "•")

    return text.strip()