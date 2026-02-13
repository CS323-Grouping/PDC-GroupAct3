import config

def compute_sss(salary: float) -> float:
    return round(salary * config.RATE_SSS, 2)

def compute_philhealth(salary: float) -> float:
    return round(salary * config.RATE_PHILHEALTH, 2)

def compute_pagibig(salary: float) -> float:
    return round(salary * config.RATE_PAGIBIG, 2)

def compute_tax(salary: float) -> float:
    return round(salary * config.RATE_TAX, 2)