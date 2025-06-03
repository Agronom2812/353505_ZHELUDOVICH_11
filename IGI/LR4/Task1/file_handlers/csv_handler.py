"""
CSV serialization/deserialization for SynonymDictionary.
"""

import csv
from ..dictionary import SynonymDictionary

def save_to_csv(dictionary: SynonymDictionary, file_path: str) -> None:
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "Synonym"])
            seen = set()
            for word, synonym in dictionary.synonyms.items():
                if (word, synonym) not in seen and (synonym, word) not in seen:
                    writer.writerow([word, synonym])
                    seen.add((word, synonym))
    except IOError as e:
        raise IOError(f"CSV write error: {e}")

def load_from_csv(file_path: str) -> SynonymDictionary:
    dictionary = SynonymDictionary()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) != 2:
                    raise ValueError("Invalid CSV format")
                word, synonym = row
                dictionary.add_pair(word.strip(), synonym.strip())
        return dictionary
    except IOError as e:
        raise IOError(f"CSV read error: {e}")
