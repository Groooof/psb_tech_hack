import pydantic as pd
import datetime as dt
import re
import typing as tp
from enum import Enum


def validate_phone(phone):
    regex = '^7[0-9]{10}$'
    if not re.search(regex, phone):
        raise ValueError('Wrong phone format')
    return phone


class CreditPurposes(str, Enum):
    flat = 'flat'
    other = 'other'


class RequestUserData(pd.BaseModel):
    surname: str
    name: str
    patronymic: str
    phone: str
    birthday: dt.date
    document_type: str
    passport_series: str = pd.Field(min_length=4, max_length=4)
    passport_number: str = pd.Field(min_length=6, max_length=6)
    profit: int
    amount: int
    benefits: bool
    purpose: CreditPurposes

    _phone_validator = pd.validator('phone')(validate_phone)

    class Config:
        schema_extra = {
            'example': {
                'surname': 'Иванова',
                'name': 'Алиса',
                'patronymic': 'Леонидовна',
                'phone': '79780000006',
                'birthday': '1995-04-19',
                'document_type': 'паспорт',
                'passport_series': '0006',
                'passport_number': '000006',
                'profit': '45000',
                'amount': '100000',
                'benefits': 'True',
                'purpose': 'other'
            }
        }


class AvailableCreditInfo(pd.BaseModel):
    name: str
    monthly_payment: int
    period: int
    overpayment: int


class ResponseAvailableCreditProducts(pd.BaseModel):
    min_overpayment: tp.List[AvailableCreditInfo] = pd.Field(default_factory=list)
    min_monthly_payment: tp.List[AvailableCreditInfo] = pd.Field(default_factory=list)

