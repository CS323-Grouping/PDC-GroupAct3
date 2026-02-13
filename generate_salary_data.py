import json
import random
import os
from datetime import datetime

# --- CONFIGURATION ---
NUM_EMPLOYEES = 50
MIN_SALARY = 20000
MAX_SALARY = 90000
OUTPUT_DIR = "data"
OUTPUT_FILE = "salary.json"
FILE_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

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

def generate_dataset(count):
    employees = []
    total_salary = 0

    log("INFO", "Starting employee dataset generation...")
    log("INFO", f"Target record count: {count}")
    log("INFO", f"Salary range: {MIN_SALARY} - {MAX_SALARY}")
    log("INFO", f"Output path: {FILE_PATH}")

    for index in range(1, count + 1):
        f_name = random.choice(FIRST_NAMES)
        l_name = random.choice(LAST_NAMES)
        salary = round(random.uniform(MIN_SALARY, MAX_SALARY), 2)

        employee = {
            "name": f"{f_name} {l_name}",
            "salary": salary
        }

        employees.append(employee)
        total_salary += salary

        log("DEBUG", f"[{index}/{count}] Generated -> {employee['name']} | Salary: {salary}")

    average_salary = round(total_salary / count, 2)

    log("INFO", "Finished generating employee records.")
    log("INFO", f"Total payroll generated: {round(total_salary, 2)}")
    log("INFO", f"Average salary: {average_salary}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    log("INFO", f"Ensured directory '{OUTPUT_DIR}' exists.")

    try:
        with open(FILE_PATH, "w") as f:
            json.dump(employees, f, indent=4)

        file_size = os.path.getsize(FILE_PATH)

        log("SUCCESS", f"Dataset successfully saved to '{FILE_PATH}'")
        log("INFO", f"File size: {file_size} bytes")

    except IOError as e:
        log("ERROR", f"Failed to save file: {e}")

    log("INFO", "Dataset generation process completed.")

if __name__ == "__main__":
    generate_dataset(NUM_EMPLOYEES)