import { Children, cloneElement } from 'react';

import styles from './ActionColor.module.scss';

interface IActionColorProps {
    children: React.ReactElement;
}

/**
 * @name ActionColor
 * @description Wrapped element will be colored with the action color
 * @param children Basicly a common string 
 */

export const ActionColor: React.FC<IActionColorProps> = ({children}) => {
    return (
        <>
            {
                Children.map(children, child => {
                    return (
                        <span className={styles.actionColor}>
                            { cloneElement(child) }
                        </span>
                    );
                })
            }
        </>
    );
};