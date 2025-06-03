"""
Main program for Lab Work
Provides menu to select between different tasks
"""


def show_main_menu():
    """Display the main menu options"""
    print("\n=== MAIN MENU ===")
    print("1. Task 1 - Synonym Dictionary")
    print("2. Task 2 - Text Analysis")
    print("3. Task 3 - Series Analysis")
    print("4. Task 4 - Geometric Shapes")
    print("5. Task 5 - NumPy Operations")
    print("0. Exit")
    return input("Select task (0-5): ").strip()


def run_task(task_number: str):
    """Run selected task"""
    if task_number == '1':
        from Lab4.Task1.ui import Task1UI
        Task1UI().run()
    elif task_number == '2':
        from Lab4.Task2.ui import Task2UI
        Task2UI().run()
    elif task_number == '3':
        from Lab4.Task3.ui import Task3UI
        Task3UI().run()
    elif task_number == '4':
        from Lab4.Task4.ui import Task4UI
        Task4UI().run()
    elif task_number == '5':
        from Lab4.Task5.ui import Task5UI
        Task5UI().run()
    else:
        print("Invalid selection")


def main():
    """Main program loop"""
    print("=== LAB WORK PROGRAM ===")
    print("Select task to execute:")

    while True:
        choice = show_main_menu()

        if choice == '0':
            print("Exiting program...")
            break
        elif choice in ('1', '2', '3', '4', '5'):
            run_task(choice)
        else:
            print("Please enter a number between 0-5")


if __name__ == "__main__":
    main()
