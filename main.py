import task_parallelism

def compute_sss(salary):
    return salary * 0.045
def compute_philhealth(salary):
    return salary * 0.025


funcs = [compute_sss, compute_philhealth]

if __name__ == "__main__":
    task_parallelism.task_p(funcs, 5000)