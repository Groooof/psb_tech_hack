import math


def get_credit_monthly_payment(amount: int, annual_interest_rate: float, period: float):
    p = annual_interest_rate/12/100
    return (amount * p) / (1 - (1 + p)**(-period))


def get_credit_period(amount: int, annual_interest_rate: float, monthly_payment: float):
    p = annual_interest_rate/12/100
    return -math.log((1 - ((amount * p) / monthly_payment)), (1 + p))
