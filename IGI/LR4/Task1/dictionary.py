"""
Core class for synonym dictionary operations.
"""

from typing import Dict, List, Tuple, Optional


class SynonymDictionary:
    """Main dictionary class with synonym operations."""

    def __init__(self, initial_pairs: Optional[List[Tuple[str, str]]] = None):
        self._synonyms: Dict[str, str] = {}
        if initial_pairs:
            for word, synonym in initial_pairs:
                self.add_pair(word, synonym)

    @property
    def synonyms(self) -> Dict[str, str]:
        return self._synonyms

    def add_pair(self, word: str, synonym: str) -> None:
        if not word or not synonym:
            raise ValueError("Both words must be non-empty")
        self._synonyms[word] = synonym
        self._synonyms[synonym] = word

    def get_synonym(self, word: str) -> str:
        if word not in self._synonyms:
            raise KeyError(f"Word '{word}' not found")
        return self._synonyms[word]

    def get_last_word_synonym(self) -> tuple[str, ...] | None:
        """
        Get the synonym for the last word added to the dictionary.
        Returns the pair in alphabetical order to ensure consistent results.
        """
        if not self._synonyms:
            return None

        last_word = next(reversed(self._synonyms))
        synonym = self._synonyms[last_word]

        return tuple(sorted((last_word, synonym)))
