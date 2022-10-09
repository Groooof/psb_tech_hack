import classNames from 'classnames';

import styles from './Button.module.scss';

interface IButtonProps {
    children: string;
    className?: string;
    onClick?: () => void;
}

type TReactButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement>;


export const Button: React.FC<IButtonProps & TReactButtonProps> = ({className, children, ...props}) => {
    const classes = classNames(styles.button, className);
    return (
        <button className={classes} {...props} >{ children }</button>
    );
};
