"""
Pickle serialization for SynonymDictionary.
"""

import pickle
from ..dictionary import SynonymDictionary

def save_to_pickle(dictionary: SynonymDictionary, file_path: str) -> None:
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(dictionary.synonyms, file)
    except (IOError, pickle.PicklingError) as e:
        raise IOError(f"Pickle write error: {e}")

def load_from_pickle(file_path: str) -> SynonymDictionary:
    dictionary = SynonymDictionary()
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            if not isinstance(data, dict):
                raise ValueError("Invalid pickle data format")
            dictionary._synonyms = data
        return dictionary
    except (IOError, pickle.UnpicklingError) as e:
        raise IOError(f"Pickle read error: {e}")
