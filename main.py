import os
import sys

import generate_salary_data
import part_a_task_parallelism
import part_b_data_parallelism

def clear_screen():
    """Clears the console screen for a clean menu view."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print(f"{'LABORATORY 3: CONCURRENCY IN PYTHON':^60}")
    print("=" * 60)

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("\nSelect an activity to run:\n")
        print("  [1] Generate/Reset Salary Data (Start Here)")
        print("  [2] Run Part A: Task Parallelism (Single Employee)")
        print("  [3] Run Part B: Data Parallelism (Batch Processing)")
        print("  [0] Exit")
        print("\n" + "-" * 60)
        
        choice = input("  Enter your choice (0-3): ").strip()

        if choice == '1':
            print("\n  >> Running Data Generator...")
            generate_salary_data.generate_dataset(25)
            input("\n  Press Enter to return to menu...")
            
        elif choice == '2':
            print("\n  >> Running Part A (Task Parallelism)...")
            part_a_task_parallelism.main()
            input("\n  Press Enter to return to menu...")
            
        elif choice == '3':
            print("\n  >> Running Part B (Data Parallelism)...")
            part_b_data_parallelism.main()
            input("\n  Press Enter to return to menu...")
            
        elif choice == '0':
            print("\n  Exiting program. Goodbye!")
            sys.exit()
            
        else:
            input("\n  Invalid choice! Press Enter to try again...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
        sys.exit()