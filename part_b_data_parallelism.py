import json
import time
import os
import multiprocessing
import random
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor

INPUT_FILE = "data/salary.json"

def log(level, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def fmt_money(amount):
    return f"₱{amount:,.2f}"

def display_payroll_summary(results):
    w_name = 20
    w_gross = 13
    w_ded = 11
    w_net = 13
    w_pid = 6
    
    table_width = w_name + w_gross + (w_ded * 5) + w_net + w_pid + 24 

    print("\n" + "=" * table_width)
    print(f"{'BATCH PAYROLL SUMMARY REPORT':^{table_width}}")
    print("=" * table_width)
    
    header = (
        f" {'EMPLOYEE NAME':<{w_name}} | {'GROSS':>{w_gross}} | "
        f"{'SSS':>{w_ded}} | {'P-HEALTH':>{w_ded}} | {'PAG-IBIG':>{w_ded}} | {'TAX':>{w_ded}} | "
        f"{'TOTAL DED':>{w_ded}} | {'NET PAY':>{w_net}} | {'PID':^{w_pid}}"
    )
    print(header)
    print("-" * table_width)

    total_payout = 0
    
    for r in results:
        f_gross = fmt_money(r['gross'])
        f_sss = fmt_money(r['sss'])
        f_ph = fmt_money(r['philhealth'])
        f_pi = fmt_money(r['pagibig'])
        f_tax = fmt_money(r['tax'])
        f_total_ded = fmt_money(r['total_deduction'])
        f_net = fmt_money(r['net_salary'])

        row = (
            f" {r['name']:<{w_name}} | {f_gross:>{w_gross}} | "
            f"{f_sss:>{w_ded}} | {f_ph:>{w_ded}} | {f_pi:>{w_ded}} | {f_tax:>{w_ded}} | "
            f"{f_total_ded:>{w_ded}} | {f_net:>{w_net}} | {r['pid']:^{w_pid}}"
        )
        print(row)
        total_payout += r['net_salary']

    print("-" * table_width)
    print(f" TOTAL PAYOUT: {fmt_money(total_payout):>{table_width - 16}}")
    print("=" * table_width + "\n")

def compute_payroll(employee):
    pid = os.getpid()
    name = employee["name"]
    salary = employee["salary"]
    
    # Random delay between 0.5s and 1.5s per employee
    delay = random.uniform(0.5, 1.5)
    
    log("PROCESS", f"[PID-{pid}] Processing {name}... ({delay:.2f}s)")
    
    time.sleep(delay) 
    
    sss = salary * 0.045
    philhealth = salary * 0.025
    pagibig = salary * 0.020
    tax = salary * 0.10
    
    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction
    
    log("PROCESS", f"[PID-{pid}] Finished {name}")
    
    return {
        "name": name,
        "gross": salary,
        "sss": sss,
        "philhealth": philhealth,
        "pagibig": pagibig,
        "tax": tax,
        "total_deduction": total_deduction,
        "net_salary": net_salary,
        "pid": pid
    }

def main():
    if not os.path.exists(INPUT_FILE):
        log("ERROR", "Data file not found. Run generator first.")
        return

    with open(INPUT_FILE, "r") as f:
        employees = json.load(f)

    log("INFO", f"Starting Data Parallelism for {len(employees)} employees...")

    start_time = time.time()
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_payroll, employees))

    duration = time.time() - start_time
    log("SUCCESS", f"Batch processing completed in {duration:.2f} seconds.")

    display_payroll_summary(results)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()