import { EFormPlaceLabels } from '../enums/Form';

interface IFormValues {
    [EFormPlaceLabels.name]: string;
    [EFormPlaceLabels.surname]: string;
    [EFormPlaceLabels.patronimic]: string;
    [EFormPlaceLabels.passport]: string;
    [EFormPlaceLabels.birthDate]: string;
    [EFormPlaceLabels.phone]: string;
};



export type {
    IFormValues
};