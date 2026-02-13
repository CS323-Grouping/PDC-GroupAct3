import json
import time
import threading
import os
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import config
import deduction_rates as rates 

def log(level, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def display_payslip(name: str, salary: float, deductions: dict, total_deduction: float, net_salary: float):
    w_label = 30
    w_amount = 18
    table_width = 1 + w_label + 1 + w_amount

    print("\n" + "=" * table_width)
    print(f"{'P A Y S L I P':^{table_width}}")
    print("=" * table_width)
    print(f" Employee Name : {name}")
    print(f" Gross Salary  : ₱{salary:,.2f}")
    print("-" * table_width)
    print(f" {'DEDUCTION TYPE':<{w_label}} {'AMOUNT':>{w_amount}}")
    print("-" * table_width)
    
    for dtype, amount in deductions.items():
        print(f" {dtype:<{w_label}} ₱{amount:>{w_amount - 1},.2f}")
        
    print("-" * table_width)
    print(f" {'Total Deductions :':<{w_label}} ₱{total_deduction:>{w_amount - 1},.2f}")
    print(f" {'NET SALARY :':<{w_label}} ₱{net_salary:>{w_amount - 1},.2f}")
    print("=" * table_width + "\n")

def run_sss(salary: float) -> float:
    delay = random.uniform(0.5, 1.5)
    thread_name = threading.current_thread().name
    log("THREAD", f"[{thread_name}] Computing SSS... ({delay:.2f}s)")
    time.sleep(delay)
    return rates.compute_sss(salary)

def run_philhealth(salary: float) -> float:
    delay = random.uniform(0.5, 1.5)
    thread_name = threading.current_thread().name
    log("THREAD", f"[{thread_name}] Computing PhilHealth... ({delay:.2f}s)")
    time.sleep(delay)
    return rates.compute_philhealth(salary)

def run_pagibig(salary: float) -> float:
    delay = random.uniform(0.5, 1.5)
    thread_name = threading.current_thread().name
    log("THREAD", f"[{thread_name}] Computing Pag-IBIG... ({delay:.2f}s)")
    time.sleep(delay)
    return rates.compute_pagibig(salary)

def run_tax(salary: float) -> float:
    delay = random.uniform(0.5, 1.5)
    thread_name = threading.current_thread().name
    log("THREAD", f"[{thread_name}] Computing Tax... ({delay:.2f}s)")
    time.sleep(delay)
    return rates.compute_tax(salary)

def task_p():
    if not os.path.exists(config.INPUT_FILE_PATH):
        log("ERROR", "Data file not found. Run generator first.")
        return

    try:
        with open(config.INPUT_FILE_PATH, "r") as f:
            employees = json.load(f)
    except json.JSONDecodeError:
        log("ERROR", "Data file is corrupt.")
        return

    if not employees:
        log("ERROR", "Employee list is empty.")
        return

    # Randomly select one employee
    emp = random.choice(employees)
    salary = emp.get("salary", 0)
    name = emp.get("name", "Unknown")
    
    log("INFO", f"Selected Random Employee: {name}")
    log("INFO", "Starting Task Parallelism...")

    start_time = time.time()
    results = {}
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_sss = executor.submit(run_sss, salary)
        future_ph = executor.submit(run_philhealth, salary)
        future_pi = executor.submit(run_pagibig, salary)
        future_tax = executor.submit(run_tax, salary)

        results["SSS"] = future_sss.result()
        results["PhilHealth"] = future_ph.result()
        results["Pag-IBIG"] = future_pi.result()
        results["Tax"] = future_tax.result()

    end_time = time.time()
    duration = end_time - start_time

    total_deduction = sum(results.values())
    net_salary = salary - total_deduction

    log("SUCCESS", f"Task processing completed in {duration:.2f} seconds.")
    display_payslip(name, salary, results, total_deduction, net_salary)

if __name__ == "__main__":
    task_p()