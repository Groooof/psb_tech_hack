import { CSSProperties } from 'react';
import classNames from 'classnames';

import styles from './Container.module.scss';

interface IContainer extends CSSProperties {
    children: React.ReactNode;
    type?: 'column' | 'row';
}

export const Container: React.FC<IContainer> = ({children, type = 'row'}) => {
    const classes = classNames(styles.container, {[styles.column]: type});

    return (
        <div className={classes}>{ children }</div>
    );
};