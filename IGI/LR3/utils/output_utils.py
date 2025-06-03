"""
Output utilities module
"""

def print_table(headers: list, data: list, column_width: int = 20):
    """
    Print data in formatted table
    
    Args:
        headers: List of column headers
        data: List of lists with row data
        column_width: Width of each column
    """
    # Print header
    header_row = " | ".join(header.ljust(column_width) for header in headers)
    print("\n" + "-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))
    
    # Print data rows
    for row in data:
        row_str = " | ".join(str(item).ljust(column_width) for item in row)
        print(row_str)
    
    print("-" * len(header_row) + "\n")

def print_series_results(history: list, final_result: float, exact_value: float):
    """
    Print series calculation results
    
    Args:
        history: List of tuples (iteration, current_sum, term_value)
        final_result: Final computed result
        exact_value: Exact math value
    """
    headers = ["Iteration", "Term Value", "Current Sum", "Error"]
    data = []
    
    for n, current_sum, term in history:
        error = abs(current_sum - exact_value)
        data.append([
            n,
            f"{term:.6e}",
            f"{current_sum:.6f}",
            f"{error:.6e}"
        ])
    
    print_table(headers, data)
    
    print(f"{'Final result:':<15} {final_result:.10f}")
    print(f"{'Exact value:':<15} {exact_value:.10f}")
    print(f"{'Difference:':<15} {abs(final_result - exact_value):.10f}\n")

def print_list_analysis(numbers: list, in_range: int, sum_after_max: float):
    """
    Print list analysis results
    
    Args:
        numbers: Processed list
        in_range: Count of numbers in range
        sum_after_max: Sum after max element
    """
    print("\nList analysis results:")
    print(f"List: {numbers}")
    print(f"Elements in range: {in_range}")
    print(f"Sum after max element: {sum_after_max}\n")

def print_min_number_result(min_num: int):
    """
    Print minimum number result
    
    Args:
        min_num: Found minimum number
    """
    if min_num is not None:
        print(f"\nThe minimum number is: {min_num}")
    else:
        print("\nNo numbers were entered")

def print_vowel_count(text: str, count: int):
    """
    Print vowel count results
    
    Args:
        text: Analyzed text
        count: Vowel count
    """
    print(f"\nText: {text}")
    print(f"Uppercase vowel count: {count}")

def print_text_analysis(results: dict):
    """
    Print comprehensive text analysis results
    
    Args:
        results: Dictionary with analysis results
    """
    print("\nText analysis results:")
    print(f"a) Word count: {results['word_count']}")
    print(f"b) Longest word: '{results['longest_word']}' (position: {results['longest_pos']})")
    print("c) Odd-positioned words:")
    for i, word in enumerate(results['odd_words'], 1):
        print(f"{i}. {word}")
