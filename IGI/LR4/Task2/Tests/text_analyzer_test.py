import pytest
from Lab4.Task2.text_analyzer import TextAnalyzer

class TestTextAnalyzer:
    @pytest.fixture
    def sample_text(self):
        return '''This is test123. "Quote1", valid: 123456. Smiles: :) ;-) :-(. Words: a1, b2cd, 3e4f5.'''

    def test_words_with_a_o_digits(self, sample_text):
        analyzer = TextAnalyzer(sample_text)
        result = analyzer.find_words_with_a_o_digits()
        assert set(result) == {"a1", "b2cd", "3e4f5"}

    def test_six_digit_validation(self):
        analyzer = TextAnalyzer("")
        assert analyzer.check_six_digit_number("123456") is True
        assert analyzer.check_six_digit_number("012345") is False


    def test_letter_frequency(self, sample_text):
        analyzer = TextAnalyzer(sample_text)
        stats = analyzer.count_letters()
        assert stats['e'] >= 3
