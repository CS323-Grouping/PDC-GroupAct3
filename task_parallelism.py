from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from datetime import datetime


def task_p(funcs, salary):
    with ThreadPoolExecutor() as exe:
        res = {}
        for function in funcs:
            print(f"{function.__name__:18} Started at: {time.time():.4f}")
            temp = exe.submit(function, salary)
            res[temp] = function.__name__

        total_deduction = 0

        for i in as_completed(res):
            task_name = res[i]
            res_value = i.result()
            print(f"{task_name:18} Ended at: {time.time():.4f} | Result: {res_value}")
            total_deduction += res_value

        print(f"Total Deduction: {total_deduction}")

