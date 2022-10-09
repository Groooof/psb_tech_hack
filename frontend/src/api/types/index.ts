import { IFormValues } from 'types';

export interface IPostDataEntity {
    surname: string,
    name: string,
    patronymic: string,
    phone: string,
    birthday: string,
    document_type: string,
    passport_series: string,
    passport_number: string,
    profit: number,
    amount: number,
    benefits: boolean,
    purpose: string,
}

export interface IResponseEntity {
    min_overpayment: ICardEntity[];
    min_monthly_payment: ICardEntity[];
}

export interface ICardEntity {
    name: string;
    type: 'overpayment' | 'payment';
    monthly_payment: number;
    period: number;
    overpayment: number;
    interest_rate: number;
}

export interface IInitialState {
    min_overpayment: ICardEntity[];
    min_monthly_payment: ICardEntity[];
    loading: 'idle' | 'pending' | 'succeeded' | 'failed';
    userData: IFormValues;
}