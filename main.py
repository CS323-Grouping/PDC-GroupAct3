import deduction_rates as rates
import task_parallelism



funcs = [rates.compute_sss, rates.compute_philhealth. rates.calculate_pagibig, rates.calculate_tax]

if __name__ == "__main__":
    task_parallelism.task_p(funcs, 5000)