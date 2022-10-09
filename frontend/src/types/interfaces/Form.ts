import { EFormEngLabels } from '../enums/Form';

interface IFormValues {
    [EFormEngLabels.name]: string;
    [EFormEngLabels.surname]: string;
    [EFormEngLabels.patronimic]: string;
    [EFormEngLabels.passport]: string;
    [EFormEngLabels.birthDate]: string;
    [EFormEngLabels.phone]: string;
    [EFormEngLabels.income]: string;
    [EFormEngLabels.creditSum]: string;
    [EFormEngLabels.select]: string;
};

interface ISelectOptions {
    readonly value: string;
    readonly label: string;
}



export type {
    IFormValues,
    ISelectOptions
};