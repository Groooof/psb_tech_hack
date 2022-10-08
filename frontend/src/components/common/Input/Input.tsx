import { InputHTMLAttributes } from 'react';
import { Path, UseFormRegister } from 'react-hook-form';
import classNames from 'classnames/bind';

import { IFormValues, EFormPlaceholders } from 'types';

import styles from './Input.module.scss';

const cx = classNames.bind(styles);

interface IInputProps extends InputHTMLAttributes<HTMLInputElement> {
    label: Path<IFormValues>;
    register: UseFormRegister<IFormValues>;
    required: boolean;
    placeholder?: EFormPlaceholders;
    
}

export const Input: React.FC<IInputProps> = ({ label, required, register,  ...other }) => {
    return (
        <div className={cx('input')}>
            <label className={cx('input__label')}>{ label } {required && '*'}</label>
            <input className={cx('input__field')} { ...register(label, { required }) } { ...other }/>
        </div>
    );
};