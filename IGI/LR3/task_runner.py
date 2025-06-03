"""
Module to run individual tasks with proper imports
"""

from calculations.series import calculate_series, exact_value
from calculations.min_finder import find_min_number
from calculations.text_analyzer import count_uppercase_vowels, analyze_text
from calculations.list_processor import process_list
from utils.input_utils import get_float_input, get_int_input
from utils.output_utils import (
    print_series_results,
    print_min_number_result,
    print_vowel_count,
    print_text_analysis,
    print_list_analysis
)

def run_task1():
    print("\n=== Task 1: Series Expansion ===")
    x = get_float_input("Enter x (>1): ", min_val=1)
    eps = get_float_input("Enter precision: ", min_val=0)
    
    result, terms, history = calculate_series(x, eps)
    exact = exact_value(x)
    print_series_results(history, result, exact)

def run_task2():
    print("\n=== Task 2: Find Minimum Number ===")
    min_num = find_min_number()
    print_min_number_result(min_num)

def run_task3():
    print("\n=== Task 3: Count Uppercase Vowels ===")
    text = input("Enter text: ")
    count = count_uppercase_vowels(text)
    print_vowel_count(text, count)

def run_task4():
    print("\n=== Task 4: Text Analysis ===")
    text = """So she was considering..."""  # Full text here
    analysis = analyze_text(text)
    print_text_analysis(analysis)

def run_task5():
    print("\n=== Task 5: List Processing ===")
    n = get_int_input("Enter list size: ", min_val=1)
    numbers = [get_float_input(f"Element {i+1}: ") for i in range(n)]
    
    a = get_float_input("Enter A: ")
    b = get_float_input("Enter B: ")
    
    in_range, sum_after = process_list(numbers, a, b)
    print_list_analysis(numbers, in_range, sum_after)

if __name__ == "__main__":
    run_task1()
