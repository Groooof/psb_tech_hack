import classNames from 'classnames';

import styles from './Title.module.scss';

interface ITitleProps {
    variant: 'header' | 'subheader';
    className?: string;
    children: React.ReactNode | string;
}



export const Title: React.FC<ITitleProps> = ({variant = 'subheader', className, children}) => {
    
    const cx = classNames(styles[`title-${variant}`], className);

    if (variant === 'header') {
        return <h1 className={cx}>{ children }</h1>;
    }

    return (
        <h2 className={cx}>{ children }</h2>
    );
};

