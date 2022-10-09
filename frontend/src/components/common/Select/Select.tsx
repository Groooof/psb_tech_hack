import SelectLibrary, { StylesConfig, SingleValue, ActionMeta } from 'react-select';

import { ISelectOptions } from 'types';
import { Colors } from 'const/variables';

import './Select.scss';

const styling: StylesConfig<ISelectOptions, false> = {
    control: () => ({
        display: 'flex',
        width: '100%',
        maxHeight: 40,
        paddingTop: 3,
        paddingLeft: 12,
        backgroundColor: Colors.InputBorderColor,
        border: '1px solid transparent',
        borderRadius: 8,
    }),
    option: (provided) => ({
        ...provided,
        backgroundColor: 'white',
        '&:hover': {
            backgroundColor: Colors.InputBorderColor
        }
    })
};

interface ISelectProps {
    onChange: (newValue: SingleValue<ISelectOptions>, actionMeta: ActionMeta<ISelectOptions>) => void;
}


const options: ISelectOptions[] = [
    {value: 'flat', label: 'Квартира'},
    {value: 'business', label: 'Бизнес'},
    {value: 'другое', label: 'Другие цели'},
];

export const Select: React.FC<ISelectProps> = ({onChange}) => {
    return (
        <SelectLibrary styles={styling} onChange={onChange} className='select' options={options} placeholder="Цель кредита"/>
    );
};