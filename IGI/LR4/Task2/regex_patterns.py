import re


class RegexPatterns:
    WORD_WITH_A_O_AND_DIGITS = re.compile(r'\b(?:[a-o]+\d+|\d+[a-o]+)[a-o\d]*\b', re.IGNORECASE)
    SIX_DIGIT_NUMBER = re.compile(r'^[1-9]\d{5}$')
    QUOTED_WORDS = re.compile(r'\"(\w+)\"')

    SENTENCES = re.compile(r'[.!?]+[\s\n]')
    DECLARATIVE = re.compile(r'\.\s')
    INTERROGATIVE = re.compile(r'\?\s')
    IMPERATIVE = re.compile(r'!\s')
    WORDS = re.compile(r'\b\w+\b')
    SMILE = re.compile(r'[:;]-*[()[\]{}]+')
    LETTER_COUNT = re.compile(r'[a-zA-Zа-яА-Я]')
    WORD_PAIRS = re.compile(r'\b(\w+),\s(\w+)\b')
