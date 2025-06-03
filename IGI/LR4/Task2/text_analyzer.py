from collections import Counter
from .regex_patterns import RegexPatterns


class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.patterns = RegexPatterns()

    def analyze(self):
        return {
            "variant11": {
                "words_with_a_o_digits": self.find_words_with_a_o_digits(),
                "is_valid_number": self.check_six_digit_number("123456"),
                "quoted_words_count": len(self.find_quoted_words()),
                "letter_frequency": self.count_letters(),
                "word_pairs": self.find_word_pairs()
            },
            "common": {
                "sentences_count": len(self.split_sentences()),
                "declarative": len(self.patterns.DECLARATIVE.findall(self.text)),
                "interrogative": len(self.patterns.INTERROGATIVE.findall(self.text)),
                "imperative": len(self.patterns.IMPERATIVE.findall(self.text)),
                "avg_sentence_length": self.avg_sentence_length(),
                "avg_word_length": self.avg_word_length(),
                "smiles_count": len(self.patterns.SMILE.findall(self.text))
            }
        }

    def find_words_with_a_o_digits(self) -> list:
        return self.patterns.WORD_WITH_A_O_AND_DIGITS.findall(self.text)

    def check_six_digit_number(self, number_str: str) -> bool:
        return bool(self.patterns.SIX_DIGIT_NUMBER.match(number_str))

    def find_quoted_words(self):
        return self.patterns.QUOTED_WORDS.findall(self.text)

    def count_letters(self):
        letters = self.patterns.LETTER_COUNT.findall(self.text.lower())
        return dict(Counter(letters))

    def find_word_pairs(self):
        pairs = self.patterns.WORD_PAIRS.findall(self.text)
        return [f"{first}, {second}" for first, second in pairs]

    def split_sentences(self):
        return [s.strip() for s in self.patterns.SENTENCES.split(self.text) if s.strip()]

    def avg_sentence_length(self):
        sentences = self.split_sentences()
        if not sentences:
            return 0
        words = sum(len(self.patterns.WORDS.findall(s)) for s in sentences)
        return words / len(sentences)

    def avg_word_length(self):
        words = self.patterns.WORDS.findall(self.text)
        if not words:
            return 0
        return sum(len(w) for w in words) / len(words)
