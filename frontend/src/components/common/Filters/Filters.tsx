import { useState } from 'react';
import classNames from 'classnames';

import styles from './Filters.module.scss';

interface IFilterTexts {
    [key: string]: string;
}


/**
 * @name Filters
 * @description Filters component, changes tabs and filter value acc on click
 * @returns Basic React component
 */

export const Filters: React.FC = () => {
    const [filter, setFilter] = useState<string>('overPay');

    const filterTexts: IFilterTexts = {
        overPay: 'По итогу переплаты',
        minimal: 'По минимальному платежу'
    };

    function handleFilter(e: React.MouseEvent<HTMLDivElement>) {
        const target = e.target;
        if (target instanceof Element) {
            const closest = target.closest('#overPay, #minimal');
            if (closest) {
                setFilter(closest.id);
            }
        }
    }

    const overPay = classNames(styles.filters__item, filter === 'overPay' && styles.active);
    const minimal = classNames(styles.filters__item, filter === 'minimal' && styles.active);
    return (
        <div onClick={handleFilter} className={styles.filters}>
            <div className={overPay} id="overPay">
                <span>{filterTexts.overPay}</span>
            </div>
            <div className={minimal} id="minimal">
                <span>{filterTexts.minimal}</span>
            </div>
        </div>
    );
};