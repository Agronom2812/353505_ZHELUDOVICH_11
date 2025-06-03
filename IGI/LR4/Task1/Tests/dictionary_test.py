"""
Tests for SynonymDictionary core functionality
"""
import unittest
from ..dictionary import SynonymDictionary


class TestSynonymDictionary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_pairs = [("happy", "joyful"), ("big", "large")]

    def setUp(self):
        self.dict = SynonymDictionary(self.test_pairs)

    def test_add_pair(self):
        self.dict.add_pair("fast", "quick")
        self.assertEqual(self.dict.get_synonym("fast"), "quick")
        self.assertEqual(self.dict.get_synonym("quick"), "fast")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.dict.add_pair("", "word")

    def test_synonym_lookup(self):
        self.assertEqual(self.dict.get_synonym("happy"), "joyful")
        with self.assertRaises(KeyError):
            self.dict.get_synonym("unknown")

    def test_last_word(self):
        self.assertEqual(self.dict.get_last_word_synonym(), ("big", "large"))


if __name__ == "__main__":
    unittest.main()
