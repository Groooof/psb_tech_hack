import math


def get_credit_monthly_payment(amount: int, annual_interest_rate: float, period: float) -> float:
    """
    Расчет ежемесячного платежа по кредиту.
    :param amount: запрашиваемая сумма кредита;
    :param annual_interest_rate: годовая процентная ставка;
    :param period: срок, на который оформляется кредит (в месяцах);
    :return: рассчитанный ежемесячный платеж.
    """
    p = annual_interest_rate/12/100
    return math.ceil((amount * p) / (1 - (1 + p)**(-period)))


def get_credit_period(amount: int, annual_interest_rate: float, monthly_payment: float) -> float:
    """
    Расчет срока кредита.
    :param amount: запрашиваемая сумма кредита;
    :param annual_interest_rate: годовая процентная ставка;
    :param monthly_payment: ежемесячный платеж;
    :return: рассчитанный срок (в месяцах).
    """
    p = annual_interest_rate/12/100
    return -math.log((1 - ((amount * p) / monthly_payment)), (1 + p))


def get_credit_overpayment(period, monthly_payment, amount):
    """
    Расчет переплаты по кредиту.
    :param period: срок кредита;
    :param monthly_payment: ежемесячный платеж;
    :param amount: запрашиваемая сумма кредита;
    :return: рассчитанная сумма переплаты.
    """
    return (period * monthly_payment) - amount


def get_available_funds(profit, monthly_load) -> float:
    """
    Расчет доступных для получения кредита средств
    :param profit: доход
    :param monthly_load: ежемесячная нагрузка (сумма всех ежемесячных кредитный обязательств)
    :return:
    """
    return round(((profit / 6) - monthly_load) / 2)


