import { Colors } from 'const/variables';
import { ICardEntity } from 'api/types';

import { ActionColor } from '../ActionColor/ActionColor';
import { Button } from '../Button/Button';

import styles from './Card.module.scss';



export const Card: React.FC<ICardEntity> = ({
    name = 'Кредит', 
    type = 'payment',
    interest_rate = 5.5, 
    monthly_payment = 12000, 
    period = 3, 
    overpayment = 20000
}) => {
    const coloredPayment = (
        <ActionColor>
            {monthly_payment}
        </ActionColor>
    );
    const coloredOverpayment = (
        <ActionColor>
            {monthly_payment}
        </ActionColor>
    );
    return (
        <div className={styles.card}>
            <h3 className={styles.card__title}>{name}</h3>
            <div className={styles.card__info}>
                <div className={styles.card__interest}>
                    <span className={styles.card__infoTitle}>{interest_rate}%</span>
                    <span className={styles.card__infoSubtitle}>% ставка</span>
                </div>
                <div className={styles.card__overpayment}>
                    <span className={styles.card__infoTitle}>
                        {
                            type === 'payment' ? coloredPayment : monthly_payment
                        }
                    </span>
                    <span className={styles.card__infoSubtitle}>Платеж</span>
                </div>
                <div className={styles.card__period}>
                    <span className={styles.card__infoTitle}>{period} Года</span>
                    <span className={styles.card__infoSubtitle}>Срок</span>
                </div>
                <div className={styles.card__monthly}>
                    <span className={styles.card__infoTitle}>
                        {
                            type === 'overpayment' ? coloredOverpayment : overpayment
                        }
                    </span>
                    <span className={styles.card__infoSubtitle}>Переплата</span>
                </div>
            </div>
            <Button color={Colors.actionColor}>Оформить</Button>
        </div>
    );
};