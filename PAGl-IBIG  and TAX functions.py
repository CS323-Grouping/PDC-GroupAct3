def calculate_pagibig(salary):
    pagibig_rate = 0.02
    pagibig = salary * pagibig_rate
    return round(pagibig, 2)

def calculate_tax(salary):
    tax_rate = 0.10
    tax = salary * tax_rate
    return round(tax, 2)

salary = 20000

pagibig = calculate_pagibig(salary)
tax = calculate_tax(salary)

print(f"Salary: ₱{salary}")
print(f"Pag-IBIG Contribution: ₱{pagibig}")
print(f"Tax Deduction: ₱{tax}")
