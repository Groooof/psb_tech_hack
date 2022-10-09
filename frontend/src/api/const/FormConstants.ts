import { IInitialState } from 'api/types';

const initialState: IInitialState = {
    min_monthly_payment: [],
    min_overpayment: [],
    loading: 'idle',
    userData: {
        name: '',
        surname: '',
        patronimic: '',
        passport: '',
        birthDate: '',
        phone: '',
        income: '',
        creditSum: '',
        select: ''
    }
};

export { initialState };