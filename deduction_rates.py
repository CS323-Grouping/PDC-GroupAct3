import time
def calculate_pagibig(salary):
    pagibig_rate = 0.02
    pagibig = salary * pagibig_rate
    return round(pagibig, 2)

def calculate_tax(salary):
    tax_rate = 0.10
    tax = salary * tax_rate
    return round(tax, 2)

def compute_sss(salary):
    return salary * 0.045
def compute_philhealth(salary):
    return salary * 0.025



