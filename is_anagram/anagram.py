from unicodedata import normalize


def is_anagram(first_word: str, second_word: str):
    first_word = ''.join(normalize('NFD', ''.join(first_word.lower().split())))
    second_word = ''.join(normalize('NFD', ''.join(second_word.lower().split())))
    a = sorted(filter(str.isalpha, first_word))
    b = sorted(filter(str.isalpha, second_word))
    return a == b
