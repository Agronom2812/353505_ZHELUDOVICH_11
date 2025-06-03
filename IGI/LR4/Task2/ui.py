"""
Text analyzer UI for Task 2
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
from Lab4.Task2.text_analyzer import TextAnalyzer
from Lab4.Task2.file_operations import FileOperations


class Task2UI:
    """Handles user interface for text analysis."""

    def __init__(self) -> None:
        self.analyzer: Optional[TextAnalyzer] = None
        self.results: Optional[Dict[str, Any]] = None

    def run(self) -> None:
        """Main execution loop."""
        while True:
            self._display_menu()
            choice = input("Enter choice (1-4): ").strip()

            if choice == '1':
                self._analyze_text_flow()
            elif choice == '2':
                self._validate_number()
            elif choice == '3':
                self._show_letter_stats()
            elif choice == '4':
                return
            else:
                print("Invalid input. Enter 1-4")

    @staticmethod
    def _display_menu() -> None:
        """Displays menu options."""
        print("\n=== TEXT ANALYZER ===")
        print("1. Full text analysis")
        print("2. Validate 6-digit number")
        print("3. Show letter frequency")
        print("4. Exit to main menu")

    def _analyze_text_flow(self) -> None:
        """Handles full analysis workflow."""
        try:
            file_path = input("Input file path [default: data/input.txt]: ").strip() or "Lab4/Task2/data/input.txt"
            self._load_and_analyze(file_path)
            self._save_and_zip()
            self._show_results()
        except Exception as e:
            print(f"Error: {str(e)}")

    def _load_and_analyze(self, path: str) -> None:
        """Loads and processes text file with proper path resolution"""
        if not os.path.isabs(path):
            base_dir = Path(__file__).parent.parent
            path = str(base_dir / "Task2" / "data" / "input.txt")

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found at: {path}")  # Debug path

        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        self.analyzer = TextAnalyzer(text)
        self.results = self.analyzer.analyze()

    def _save_and_zip(self) -> None:
        """Saves results and creates zip archive."""
        if not self.results:
            raise ValueError("No data to save")

        FileOperations.save_results(self.results, "results.json")
        FileOperations.zip_file("results.json", "results.zip")
        print("Results saved and archived")

    def _show_results(self) -> None:
        """Displays analysis summary."""
        if not self.results:
            print("No data available")
            return

        print("\n=== ANALYSIS SUMMARY ===")
        print(f"Words with a-o + digits: {len(self.results['variant11']['words_with_a_o_digits'])}")
        print(f"Quoted words: {self.results['variant11']['quoted_words_count']}")
        print(f"Smileys detected: {self.results['common']['smiles_count']}")

    @staticmethod
    def _validate_number() -> None:
        """Validates 6-digit number input."""
        num = input("Enter 6-digit number: ")
        is_valid = TextAnalyzer("").check_six_digit_number(num)
        print(f"Number is {'valid' if is_valid else 'invalid'}")

    def _show_letter_stats(self) -> None:
        """Displays letter frequency statistics."""
        if not self.analyzer:
            file_path = input("Enter file path: ").strip() or "input.txt"
            self._load_and_analyze(file_path)

        stats = self.analyzer.count_letters()
        print("\nLETTER FREQUENCY:")
        for char, count in sorted(stats.items(), key=lambda x: -x[1])[:10]:
            print(f"{char}: {count}")
