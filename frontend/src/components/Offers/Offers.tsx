import { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { IInitialState, ICardEntity } from 'api/types';

import { Title, ActionColor, Filters, Card } from 'components/common';

import styles from './Offers.module.scss';

interface IDiapason {
    [dayPart: string]: [number, number];
}

interface IDayPart {
    [dayPart: string]: string;
}

interface IOffersProps {
    name?: string;
}

/**
 * @name Offers
 * @description Component which includes part with filters and cards
 * @param name User's name which is got from the Redux store after form completion
 * @returns Basic React Component
 */

export const Offers: React.FC<IOffersProps> = ({name = 'Анна'}) => {
    const min_monthly_payment: ICardEntity[] = useSelector((state: IInitialState) => state.min_monthly_payment);
    const min_overpayment: ICardEntity[] = useSelector((state: IInitialState) => state.min_overpayment);
    const [dayPartKey, setDayPartKey] = useState<string>('');
    const dayPart: IDayPart | undefined = {
        morning: 'Доброе утро',
        afternoon: 'Добрый день',
        evening: 'Добрый вечер',
        night: 'Доброй ночи'
    };

    useEffect(() => {
        getCurrentTimePart();
    }, []);
    function getCurrentTimePart() {
        const date = new Date();
        const hour = date.getHours();
        const diapason: IDiapason = {
            morning: [4, 11],
            afternoon: [12, 16],
            evening: [17, 23],
            night: [24, 3]
        };
        for (const key in diapason) {
            diapason[key].forEach((dayPart, index, arr): void => {
                if (dayPart <= hour && hour <= arr[1]) {
                    setDayPartKey(key);
                }
            });
        }
    }
    const welcomeText = `${dayPart[dayPartKey]}, ${name}, персонализировали`;

    // const paymentElems = min_monthly_payment.map((item, index) => {
    //     const {
    //         name,
    //         monthly_payment,
    //         period, 
    //         overpayment,
    //         interest_rate
    //     } = item;
    //     return (
    //         <Card key={`item-card-${index}`} type="payment" overpayment={overpayment} interest_rate={interest_rate} name={name} monthly_payment={monthly_payment} period={period}/>
    //     );
    // });
    // const overElems = min_overpayment.map((item, index) => {
    //     const {
    //         name,
    //         monthly_payment,
    //         period, 
    //         overpayment,
    //         interest_rate
    //     } = item;
    //     return (
    //         <Card key={`item-card-${index}`} type="overpayment" overpayment={overpayment} interest_rate={interest_rate} name={name} monthly_payment={monthly_payment} period={period}/>
    //     );
    // });
    
    return (
        <div className={styles.offers}>
            <Title className={styles.offers__title} variant='subheader'>
                { welcomeText } <ActionColor>предложения для Вас</ActionColor>
            </Title>
            <Filters/>
            <Card name='Потребительский кредит' type="overpayment" interest_rate={5.5} monthly_payment={16000} period={3} overpayment={5.5}/>
        </div>
    );
};

