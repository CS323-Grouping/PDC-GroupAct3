from concurrent.futures import ProcessPoolExecutor
import os

SSS_RATE = 0.045
PHILHEALTH_RATE = 0.025
PAGIBIG_RATE = 0.02
TAX_RATE = 0.10

employees = [
    ("Employee_1", 25000),
    ("Employee_2", 32000),
    ("Employee_3", 28000),
    ("Employee_4", 40000),
    ("Employee_5", 35000)
]

def compute_payroll(employee):
    """
    Computes all deductions, total deduction,
    and net salary for one employee.
    """
    name, salary = employee

    sss = salary * SSS_RATE
    philhealth = salary * PHILHEALTH_RATE
    pagibig = salary * PAGIBIG_RATE
    tax = salary * TAX_RATE

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    # Optional: show process ID to observe parallel execution
    print(f"{name} processed by PID: {os.getpid()}")

    return {
        "name": name,
        "gross_salary": salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

        print("\n=== Payroll Results ===\n")
        for result in results:
            print(f"Employee: {result['name']}")
            print(f"Gross Salary: {result['gross_salary']:.2f}")
            print(f"Total Deduction: {result['total_deduction']:.2f}")
            print(f"Net Salary: {result['net_salary']:.2f}")
            print("-" * 40)
