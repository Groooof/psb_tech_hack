import { useState, useEffect } from 'react';
import { useForm, SubmitHandler } from 'react-hook-form';
import { SingleValue } from 'react-select';

import { updateField } from 'api/slices/FormSlice';
import { useAppDispatch } from 'app/hooks';

import { Title, Input, Range, Select, ActionColor, Button } from 'components/common/';

import { 
	IFormValues, 
	EFormEngLabels, 
	EFormLabels, 
	EFormPlaceholders, 
	ISelectOptions
} from 'types';

import styles from  './Form.module.scss';

interface IRangeValueObject {
	creditSum: number;
	income: number;
}

type TRangeType = 'creditSum' | 'income';


/**
 * @name Form
 * @description Main Form component. Includes all needed fields for verification.
 * Uses React-hook-Form inside, React-Select and React-MaskedInput
 * @returns A common React component
 */

const Form: React.FC = () => {
	const [rangeValue, setRange] = useState<IRangeValueObject>({creditSum: 30000, income: 30000});
	const { register, handleSubmit, setValue } = useForm<IFormValues>();
	const dispatch  = useAppDispatch();

	useEffect(() => {
		setValue(EFormEngLabels.creditSum, `${rangeValue.creditSum}`);
		setValue(EFormEngLabels.income, `${rangeValue.income}`);
	}, [rangeValue, setValue]);

	function handleRange(type: TRangeType, value: number) {
		setRange(prevState => {
			return {
				...prevState,
				[type]: value
			};
		});
	}

	function handleSelect(option: SingleValue<ISelectOptions>) {
		setValue(EFormEngLabels.select, option!.value);
	}
	
	const onSubmit: SubmitHandler<IFormValues> = data => {
		const tempObject = {
			...data,
			passport_series: data.passport.substring(0, 4),
			passport_number: data.passport.substring(4)
		};
		dispatch(updateField(tempObject));
	};

	

	return (
		<>
			<Title className={styles.title} variant="subheader">
				Заполните форму и <wbr/> получите <ActionColor>индивидуальное предложение</ActionColor>
			</Title>
			<form onSubmit={handleSubmit(onSubmit)}>
				
				<Input type="text" fieldName={EFormLabels.name} label={EFormEngLabels.name} placeholder={EFormPlaceholders.name} register={register}  required/>
				<Input type="text" fieldName={EFormLabels.surname} label={EFormEngLabels.surname} placeholder={EFormPlaceholders.surname} register={register}  required />
				<Input type="text" fieldName={EFormLabels.patronimic} label={EFormEngLabels.patronimic} placeholder={EFormPlaceholders.patronimic} register={register} required />
				<Input type="number" fieldName={EFormLabels.passport} label={EFormEngLabels.passport} placeholder={EFormPlaceholders.passport} register={register} required />
				<Input type="date" fieldName={EFormLabels.birthDate} label={EFormEngLabels.birthDate} placeholder={EFormPlaceholders.birthDate} register={register} required />
				<Input type="tel" fieldName={EFormLabels.phone} label={EFormEngLabels.phone} placeholder={EFormPlaceholders.phone} register={register} required />
				<div className={styles.ranges}>
					<Range type="income" label={EFormLabels.income} onChange={handleRange} value={rangeValue.income} />
					<Range type="creditSum" label={EFormLabels.creditSum} onChange={handleRange} value={rangeValue.creditSum} />
				</div>
				<Select onChange={handleSelect}/>
                <div className={styles.button__container}>
                    <p className={styles['button__capture-text']}>
                        Заполняя форму, я принимаю условия на <a className={styles.button__link} href="https://www.ecredit.one/consent_personal_data_online">обработку персональных данных</a>
                    </p>
				    <Button type="submit">Поиск</Button>
                </div>
			</form>
		</>
	);
};

export { Form };
