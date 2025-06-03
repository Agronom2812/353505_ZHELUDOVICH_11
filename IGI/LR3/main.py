"""
Main executable program
"""

from task_runner import (
    run_task1,
    run_task2,
    run_task3,
    run_task4,
    run_task5
)

def show_menu():
    """Display program menu"""
    print("\nLAB WORK MENU")
    print("1. Series Expansion")
    print("2. Find Minimum Number")
    print("3. Count Uppercase Vowels")
    print("4. Text Analysis")
    print("5. List Processing")
    print("0. Exit")

def main():
    """Main program loop"""
    while True:
        show_menu()
        choice = input("Select task (0-5): ")
        
        tasks = {
            '1': run_task1,
            '2': run_task2,
            '3': run_task3,
            '4': run_task4,
            '5': run_task5
        }
        
        if choice == '0':
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")
    
    print("\nProgram finished.")

if __name__ == "__main__":
    main()
