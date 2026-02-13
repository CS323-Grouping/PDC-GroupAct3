from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime


def task_p(funcs, salary):
    res = []
    with ThreadPoolExecutor() as exe:
        for function in funcs:
            print(f"Submitting {function.__name__} at {round(time.time(), 2)}")
            res.append(exe.submit(function, salary))

    print(res)


    return res

