import styles from './ActionColor.module.scss';

interface IActionColorProps {
    children: string | number;
}

/**
 * @name ActionColor
 * @description Wrapped element will be colored with the action color
 * @param children Basicly a common string 
 */

export const ActionColor: React.FC<IActionColorProps> = ({children}) => {
    return (
        <span className={styles.actionColor}>{children}</span>
    );
};