import json
import random
import os
from datetime import datetime
import config

FIRST_NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", 
    "Ian", "Julia", "Kevin", "Liam", "Monica", "Nathan", "Olivia", "Peter", 
    "Quinn", "Rachel", "Steve", "Tina", "Ursula", "Victor", "Wendy", "Xander", 
    "Yasmine", "Zach"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", 
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", 
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

def log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def generate_dataset():
    employees = []
    
    print(f"\n--- DATA GENERATOR CONFIGURATION ---")
    user_input = input(f"Enter number of employees to generate [Default: {config.GEN_EMPLOYEE_COUNT}]: ").strip()
    
    if user_input:
        try:
            count = int(user_input)
            if count <= 0:
                print(">> Invalid number. Using default.")
                count = config.GEN_EMPLOYEE_COUNT
        except ValueError:
            print(">> Invalid input. Using default.")
            count = config.GEN_EMPLOYEE_COUNT
    else:
        count = config.GEN_EMPLOYEE_COUNT

    log("INFO", f"Starting generation of {count} employee records...")
    log("INFO", f"Output path: {config.INPUT_FILE_PATH}")

    for _ in range(count):
        f_name = random.choice(FIRST_NAMES)
        l_name = random.choice(LAST_NAMES)
        salary = round(random.uniform(config.GEN_MIN_SALARY, config.GEN_MAX_SALARY), 2)

        employees.append({
            "name": f"{f_name} {l_name}",
            "salary": salary
        })

    os.makedirs(config.DATA_DIR, exist_ok=True)

    try:
        with open(config.INPUT_FILE_PATH, "w") as f:
            json.dump(employees, f, indent=4)
        log("SUCCESS", f"Dataset successfully saved to '{config.INPUT_FILE_PATH}'")
        
        print("\n" + "="*40)
        print(f"{'PREVIEW (First 5 Records)':^40}")
        print("="*40)
        print(f" {'NAME':<25} {'SALARY':>12}")
        print("-" * 40)

        for emp in employees[:5]:
            print(f" {emp['name']:<25} ₱{emp['salary']:>11,.2f}")

        print("-" * 40)
        if count > 5:
            print(f" ... and {count - 5} more records.")

    except IOError as e:
        log("ERROR", f"Failed to save file: {e}")

if __name__ == "__main__":
    generate_dataset()