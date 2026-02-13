import json
import time
import threading
import os
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

INPUT_FILE = "data/salary.json"

def log(level, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def display_payslip(name, salary, deductions, total_deduction, net_salary):
    # --- DYNAMIC WIDTH CALCULATION ---
    w_label = 30
    w_amount = 18
    # Structure: " " + label + " " + amount
    # Total = 1 (leading space) + 30 + 1 (middle space) + 18
    table_width = 1 + w_label + 1 + w_amount

    print("\n" + "=" * table_width)
    print(f"{'P A Y S L I P':^{table_width}}")
    print("=" * table_width)
    
    # We use the width variables inside the f-string formatting
    print(f" Employee Name : {name}")
    print(f" Gross Salary  : ₱{salary:,.2f}")
    print("-" * table_width)
    
    # Header
    print(f" {'DEDUCTION TYPE':<{w_label}} {'AMOUNT':>{w_amount}}")
    print("-" * table_width)
    
    # Rows
    for dtype, amount in deductions.items():
        formatted_amount = f"₱{amount:,.2f}"
        print(f" {dtype:<{w_label}} {formatted_amount:>{w_amount}}")
        
    print("-" * table_width)
    
    # Totals
    f_total = f"₱{total_deduction:,.2f}"
    f_net = f"₱{net_salary:,.2f}"
    
    print(f" {'Total Deductions :':<{w_label}} {f_total:>{w_amount}}")
    print(f" {'NET SALARY :':<{w_label}} {f_net:>{w_amount}}")
    print("=" * table_width + "\n")

# --- REALISTIC DEDUCTION TASKS ---
def compute_sss(salary):
    thread_name = threading.current_thread().name
    delay = random.uniform(0.5, 1.5)
    log("THREAD", f"[{thread_name}] Calculating SSS... ({delay:.2f}s)")
    time.sleep(delay) 
    return salary * 0.045

def compute_philhealth(salary):
    thread_name = threading.current_thread().name
    delay = random.uniform(0.5, 1.5)
    log("THREAD", f"[{thread_name}] Calculating PhilHealth... ({delay:.2f}s)")
    time.sleep(delay)
    return salary * 0.025

def compute_pagibig(salary):
    thread_name = threading.current_thread().name
    delay = random.uniform(0.5, 1.5)
    log("THREAD", f"[{thread_name}] Calculating Pag-IBIG... ({delay:.2f}s)")
    time.sleep(delay)
    return salary * 0.020

def compute_tax(salary):
    thread_name = threading.current_thread().name
    delay = random.uniform(0.5, 1.5)
    log("THREAD", f"[{thread_name}] Calculating Tax... ({delay:.2f}s)")
    time.sleep(delay)
    return salary * 0.10

def main():
    if not os.path.exists(INPUT_FILE):
        log("ERROR", "Data file not found. Please run generator first.")
        return

    with open(INPUT_FILE, "r") as f:
        employees = json.load(f)

    if not employees:
        log("ERROR", "Employee file is empty.")
        return

    emp = random.choice(employees)
    salary = emp["salary"]
    
    log("INFO", f"Selected Random Employee: {emp['name']}")
    log("INFO", f"Starting Task Parallelism...")

    start_time = time.time()

    results = {}
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_ph = executor.submit(compute_philhealth, salary)
        future_pi = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        results["SSS"] = future_sss.result()
        results["PhilHealth"] = future_ph.result()
        results["Pag-IBIG"] = future_pi.result()
        results["Tax"] = future_tax.result()

    end_time = time.time()
    duration = end_time - start_time

    total_deduction = sum(results.values())
    net_salary = salary - total_deduction

    log("SUCCESS", f"Task processing completed in {duration:.2f} seconds.")

    display_payslip(emp['name'], salary, results, total_deduction, net_salary)

if __name__ == "__main__":
    main()