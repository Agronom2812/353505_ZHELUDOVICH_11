"""
Tests for CSV serialization
"""
import unittest
import tempfile
from pathlib import Path
from ..dictionary import SynonymDictionary
from ..file_handlers.csv_handler import save_to_csv, load_from_csv


class TestCSVHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "test.csv"
        self.dict = SynonymDictionary([("happy", "joyful")])

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_roundtrip(self):
        save_to_csv(self.dict, str(self.test_file))
        loaded = load_from_csv(str(self.test_file))
        self.assertEqual(loaded.get_synonym("happy"), "joyful")

    def test_file_handling(self):
        with self.assertRaises(IOError):
            load_from_csv("nonexistent.csv")


if __name__ == "__main__":
    unittest.main()
