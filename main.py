import os
import sys
import generate_salary_data
import task_parallelism
import data_parallelism

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print(f"{'LABORATORY 3' :^60}")
    print("=" * 60)

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("\nSelect an activity to run:\n")
        print(f"  [1] Generate Salary Data (Customize Size)")
        print("  [2] Run Part A: Task Parallelism")
        print("  [3] Run Part B: Data Parallelism")
        print("  [0] Exit")
        print("\n" + "-" * 60)
        
        choice = input("\n>> Enter your choice (0-3): ").strip()

        if choice == '1':
            generate_salary_data.generate_dataset() 
            input("\nPress Enter to return to menu...")
            
        elif choice == '2':
            print("\n>> Running Part A (Task Parallelism)...\n")
            task_parallelism.task_p()
            input("\nPress Enter to return to menu...")
            
        elif choice == '3':
            print("\n>> Running Part B (Data Parallelism)...\n")
            data_parallelism.dp_start()
            input("\nPress Enter to return to menu...")
            
        elif choice == '0':
            sys.exit()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()