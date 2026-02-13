import json
import time
import os
import multiprocessing
import random
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
import config
import deduction_rates as rates

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
        if r is None: continue
        
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

def compute_payroll(employee: dict) -> dict:
    try:
        pid = os.getpid()
        name = employee.get("name", "Unknown")
        salary = employee.get("salary", 0)
        
        delay = random.uniform(0.5, 1.5)
        log("PROCESS", f"[PID-{pid}] Processing {name}... ({delay:.2f}s)")
        time.sleep(delay) 
        
        sss = rates.compute_sss(salary)
        philhealth = rates.compute_philhealth(salary)
        pagibig = rates.compute_pagibig(salary)
        tax = rates.compute_tax(salary)
        
        total_deduction = sss + philhealth + pagibig + tax
        net_salary = salary - total_deduction
        
        return {
            "name": name, "gross": salary, "sss": sss, "philhealth": philhealth,
            "pagibig": pagibig, "tax": tax, "total_deduction": total_deduction,
            "net_salary": net_salary, "pid": pid
        }
    except Exception as e:
        log("ERROR", f"Failed to process employee: {e}")
        return None

def dp_start():
    if not os.path.exists(config.INPUT_FILE_PATH):
        log("ERROR", "Data file not found. Run generator first.")
        return

    with open(config.INPUT_FILE_PATH, "r") as f:
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
    dp_start()