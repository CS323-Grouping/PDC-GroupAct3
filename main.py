import deduction_rates as rates
import task_parallelism
import json


funcs = [rates.compute_sss, rates.compute_philhealth, rates.calculate_pagibig, rates.calculate_tax]

salaries = []

try:
    with open("data/salary.json", "r") as file:
        employees = json.load(file)
        salaries = [emp["salary"] for emp in employees]
except:
    print("Error, maybe try running generate salary.py")



if __name__ == "__main__":
    task_parallelism.task_p(funcs, 5000)