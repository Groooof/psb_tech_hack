import { InputHTMLAttributes } from 'react';
import { Path, UseFormRegister, ValidationRule } from 'react-hook-form';
import classNames from 'classnames/bind';

import { IFormValues, EFormPlaceholders, EFormLabels } from 'types';

import styles from './Input.module.scss';

const cx = classNames.bind(styles);

interface IInputProps extends InputHTMLAttributes<HTMLInputElement> {
    label: Path<IFormValues>;
    fieldName: EFormLabels;
    register: UseFormRegister<IFormValues>;
    validator?: ValidationRule<RegExp>;
    required: boolean;
    placeholder?: EFormPlaceholders;
    
}

export const Input: React.FC<IInputProps> = ({ label, fieldName, required, validator, register, ...other }) => {
    return (
        <div className={cx('input')}>
            <label className={cx('input__label')}>{ fieldName } {required && '*'}</label>
            <input className={cx('input__field')} { ...register(label, { required, pattern: validator }) } { ...other }/>
        </div>
    );
};