"""
Module for text analysis tasks
"""

def count_uppercase_vowels(text: str) -> int:
    """Count uppercase English vowels"""
    return sum(1 for char in text if char in {'A', 'E', 'I', 'O', 'U'})

def analyze_text(text: str) -> dict:
    """Perform comprehensive text analysis"""
    words = [word.strip(".,") for word in text.split()]
    
    # Task 4a: Word count
    word_count = len(words)
    
    # Task 4b: Longest word
    longest = max(words, key=len)
    longest_pos = words.index(longest) + 1
    
    # Task 4c: Odd words
    odd_words = [word for i, word in enumerate(words, 1) if i % 2 != 0]
    
    return {
        'word_count': word_count,
        'longest_word': longest,
        'longest_pos': longest_pos,
        'odd_words': odd_words
    }
