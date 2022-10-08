import classNames from 'classnames/bind';

import styles from './Title.module.scss';

interface ITitleProps {
    variant: 'header' | 'subheader';
    children: React.ReactNode;
}

const cx = classNames.bind(styles);

export const Title: React.FC<ITitleProps> = ({variant = 'subheader', children}) => {
    if (variant === 'header') {
        return <h1 className={cx('title-header')}>{ children }</h1>;
    }

    return (
        <h2>{ children }</h2>
    );
};

