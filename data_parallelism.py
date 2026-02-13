from concurrent.futures import ProcessPoolExecutor

# Payroll computation function (runs in separate process)
def compute_payroll(employee):
    name = employee["name"]
    gross_salary = employee["gross_salary"]

    # Example deductions
    tax = gross_salary * 0.10
    sss = gross_salary * 0.05
    philhealth = gross_salary * 0.03
    pagibig = 500

    total_deduction = tax + sss + philhealth + pagibig
    net_salary = gross_salary - total_deduction

    return {
        "name": name,
        "gross_salary": gross_salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }


if __name__ == "__main__":

    # Five employees
    employees = [
        {"name": "Employee 1", "gross_salary": 30000},
        {"name": "Employee 2", "gross_salary": 35000},
        {"name": "Employee 3", "gross_salary": 28000},
        {"name": "Employee 4", "gross_salary": 40000},
        {"name": "Employee 5", "gross_salary": 32000},
    ]

    # Process-based parallel execution
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_payroll, employees))

    # Display results
    print("\nPayroll Results (Data Parallelism)\n")

    for result in results:
        print(f"Name: {result['name']}")
        print(f"Gross Salary: {result['gross_salary']:.2f}")
        print(f"Total Deduction: {result['total_deduction']:.2f}")
        print(f"Net Salary: {result['net_salary']:.2f}")
        print("-" * 40)