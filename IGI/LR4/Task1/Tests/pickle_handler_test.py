"""
Tests for pickle serialization
"""
import unittest
import tempfile
from pathlib import Path
from ..dictionary import SynonymDictionary
from ..file_handlers.pickle_handler import save_to_pickle, load_from_pickle


class TestPickleHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp_dir.name) / "test.pkl"
        self.dict = SynonymDictionary([("big", "large")])

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_roundtrip(self):
        save_to_pickle(self.dict, str(self.test_file))
        loaded = load_from_pickle(str(self.test_file))
        self.assertEqual(loaded.get_synonym("big"), "large")

    def test_corrupted_file(self):
        with open(self.test_file, 'w') as f:
            f.write("invalid data")
        with self.assertRaises(IOError):
            load_from_pickle(str(self.test_file))


if __name__ == "__main__":
    unittest.main()
