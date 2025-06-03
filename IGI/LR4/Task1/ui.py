"""
Synonym Dictionary UI
Implements the same interface pattern as other tasks
"""

import os
import pickle
from pathlib import Path
from .dictionary import SynonymDictionary
from Lab4.Task1.file_handlers.csv_handler import save_to_csv, load_from_csv
from Lab4.Task1.file_handlers.pickle_handler import save_to_pickle, load_from_pickle

class Task1UI:
    """User interface for synonym dictionary task"""

    def __init__(self):
        self.dictionary = SynonymDictionary()
        self.data_dir = Path(__file__).parent / "data"
        os.makedirs(self.data_dir, exist_ok=True)

    def run(self):
        """Main entry point"""
        while True:
            self._show_menu()
            choice = input("Enter choice (1-6): ").strip()

            if choice == '1':
                self._add_pair()
            elif choice == '2':
                self._find_synonym()
            elif choice == '3':
                self._show_last()
            elif choice == '4':
                self._save_load_csv()
            elif choice == '5':
                self._save_load_pickle()
            elif choice == '6':
                return
            else:
                print("Invalid input. Please enter 1-6")

    @staticmethod
    def _show_menu():
        """Display task menu"""
        menu = [
            "\n=== SYNONYM DICTIONARY ===",
            "1. Add word pair",
            "2. Find synonym",
            "3. Show last entry",
            "4. CSV operations",
            "5. Pickle operations",
            "6. Back to main menu"
        ]
        print('\n'.join(menu))

    def _add_pair(self):
        """Add new word pair"""
        print("\nAdd new synonym pair")
        word = input("Enter word: ").strip()
        synonym = input("Enter synonym: ").strip()

        if not word or not synonym:
            print("Error: Both fields are required")
            return

        try:
            self.dictionary.add_pair(word, synonym)
            print(f"Added: {word} ↔ {synonym}")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def _find_synonym(self):
        """Find synonym for word"""
        if not self.dictionary.synonyms:
            print("Dictionary is empty. Add words first.")
            return

        word = input("Enter word to find synonym: ").strip()
        try:
            synonym = self.dictionary.get_synonym(word)
            print(f"Synonym for '{word}': {synonym}")
        except KeyError:
            print(f"Word '{word}' not found in dictionary")

    def _show_last(self):
        """Show last added pair"""
        result = self.dictionary.get_last_word_synonym()
        if result:
            word, synonym = result
            print(f"\nLast entry: {word} ↔ {synonym}")
        else:
            print("Dictionary is empty")

    def _save_load_csv(self):
        """Handle CSV operations"""
        print("\nCSV Operations:")
        print("1. Save to CSV")
        print("2. Load from CSV")
        choice = input("Select operation: ").strip()

        file_path = self.data_dir / "synonyms.csv"

        if choice == '1':
            try:
                save_to_csv(self.dictionary, file_path)
                print(f"Saved to {file_path}")
            except IOError as e:
                print(f"Save error: {str(e)}")
        elif choice == '2':
            try:
                self.dictionary = load_from_csv(file_path)
                print(f"Loaded from {file_path}")
            except (IOError, ValueError) as e:
                print(f"Load error: {str(e)}")
        else:
            print("Invalid choice")

    def _save_load_pickle(self):
        """Handle pickle operations"""
        print("\nPickle Operations:")
        print("1. Save to pickle")
        print("2. Load from pickle")
        choice = input("Select operation: ").strip()

        file_path = self.data_dir / "synonyms.pkl"

        if choice == '1':
            try:
                save_to_pickle(self.dictionary, file_path)
                print(f"Saved to {file_path}")
            except IOError as e:
                print(f"Save error: {str(e)}")
        elif choice == '2':
            try:
                self.dictionary = load_from_pickle(file_path)
                print(f"Loaded from {file_path}")
            except (IOError, pickle.UnpicklingError) as e:
                print(f"Load error: {str(e)}")
        else:
            print("Invalid choice")
