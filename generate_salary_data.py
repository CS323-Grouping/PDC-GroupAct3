import json
import random
import os

# --- CONFIGURATION ---
NUM_EMPLOYEES = 20
MIN_SALARY = 20000
MAX_SALARY = 90000
OUTPUT_DIR = "data"
OUTPUT_FILE = "salary.json"
FILE_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

# --- DATA POOLS ---
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

def generate_dataset(count):
    """Generates random employee data and saves it to a JSON file."""
    employees = []
    
    print(f"Generating {count} employee records...")

    for _ in range(count):
        f_name = random.choice(FIRST_NAMES)
        l_name = random.choice(LAST_NAMES)
        
        # Round salary to 2 decimal places for realism
        salary = round(random.uniform(MIN_SALARY, MAX_SALARY), 2)
        
        employees.append({
            "name": f"{f_name} {l_name}",
            "salary": salary
        })

    # Ensure the 'data' directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Write to JSON
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(employees, f, indent=4)
        print(f"✅ Successfully saved to '{FILE_PATH}'")
    except IOError as e:
        print(f"❌ Error saving file: {e}")

if __name__ == "__main__":
    generate_dataset(NUM_EMPLOYEES)