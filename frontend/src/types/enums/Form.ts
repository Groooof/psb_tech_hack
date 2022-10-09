enum EFormPlaceholders {
    name = 'Иван',
    surname = 'Иванов',
    patronimic = 'Иванович',
    passport = '____ ____',
    birthDate = '__ __ ____',
    phone = '+7 (___) ___-__-__'
};

enum EFormEngLabels {
    name = 'name',
    surname = 'surname',
    patronimic = 'patronimic',
    passport = 'passport',
    birthDate = 'birthDate',
    phone = 'phone',
    income = 'income',
    creditSum = 'creditSum',
    select = 'select'
}

enum EFormLabels {
    name = 'Имя',
    surname = 'Фамилия',
    patronimic = 'Отчество',
    passport = 'Серия и номер паспорта',
    birthDate = 'Дата рождения',
    phone = 'Телефон',
    income = 'Ежемесячный доход',
    creditSum = 'Требуемая сумма'
}

export {
    EFormPlaceholders,
    EFormEngLabels,
    EFormLabels
};