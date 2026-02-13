import deduction_rates as rates
import task_parallelism
import data_parallelism
import json


funcs = [rates.compute_sss, rates.compute_philhealth, rates.calculate_pagibig, rates.calculate_tax]


try:
    with open("data/salary.json", "r") as file:
        temp = json.load(file)
        employees = {emp["name"]: emp["salary"] for emp in temp}

except:
    print("Error, maybe try running generate salary.py")


if __name__ == "__main__":
    task_parallelism.task_p(funcs, 5000) # gi hardcode nako ang salary for Task Parallelism
    print("----Data Parallelism----")
    data_parallelism.dp_start(employees)