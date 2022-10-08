CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    patronymic TEXT,
    phone CHAR(11) NOT NULL,
    email TEXT,
    is_client BOOLEAN DEFAULT FALSE,
    birthday DATE NOT NULL,
    passport_series CHAR(4) NOT NULL,
    passport_number CHAR(6) NOT NULL,
    personal_data_consent BOOLEAN DEFAULT FALSE,
    registration_address TEXT,
    residential_address TEXT
);

CREATE TABLE consumer_credits (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    max_period SMALLINT NOT NULL,
    min_interest_rate DECIMAL(3, 1) NOT NULL,
    max_amount INT NOT NULL,
    benefits BOOLEAN DEFAULT FALSE
);

CREATE TABLE credit_cards (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    interest_free_period SMALLINT NOT NULL,
    max_amount INT NOT NULL,
    benefits BOOLEAN DEFAULT FALSE
);

CREATE TABLE mortgages (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    max_period SMALLINT NOT NULL,
    min_interest_rate DECIMAL(4, 2) NOT NULL,
    max_amount INT NOT NULL,
    benefits BOOLEAN DEFAULT FALSE
);

CREATE TABLE fns (
    id SERIAL PRIMARY KEY,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    patronymic TEXT,
    inn CHAR(12) NOT NULL,
    birthday DATE NOT NULL,
    document_type TEXT NOT NULL,
    passport_series CHAR(4) NOT NULL,
    passport_number CHAR(6) NOT NULL,
    profit INT NOT NULL
);

CREATE TABLE fms (
    id SERIAL PRIMARY KEY,
    passport_series CHAR(4) NOT NULL,
    passport_number CHAR(6) NOT NULL,
    validity DATE NOT NULL
);

CREATE TABLE bki (
    id SERIAL PRIMARY KEY,
    passport_series CHAR(4) NOT NULL,
    passport_number CHAR(6) NOT NULL,
    monthly_load INT NOT NULL,
    overdue BOOLEAN NOT NULL
);

INSERT INTO fns (surname, name, patronymic, inn, birthday, document_type, passport_series, passport_number, profit)
VALUES
    ('Бобров', 'Андрей', 'Андреевич', '000000000001', '2000-05-03', 'паспорт', '0001', '000001', 0),
    ('Харитонов', 'Марк', 'Петрович', '000000000002', '1995-11-14', 'паспорт', '0002', '000002', 105500),
    ('Гаврилов', 'Алекандр', 'Алексеевич', '000000000003', '2002-06-23', 'паспорт', '0003', '000003', 30000),
    ('Левин', 'Егор', 'Юрьевич', '000000000004', '1994-05-01', 'паспорт', '0004', '000004', 60000),
    ('Виноградов', 'Александр', 'Алексеевич', '000000000005', '1999-04-16', 'паспорт', '0005', '000005', 0),

    ('Иванова', 'Алиса', 'Леонидовна', '000000000006', '1995-04-19', 'паспорт', '0006', '000006', 45000),
    ('Николаева', 'Алисия', 'Александровна', '000000000007', '2001-10-23', 'паспорт', '0007', '000007', 30000),
    ('Данилов', 'Максим', 'Даниилович', '000000000008', '1990-02-10', 'паспорт', '0008', '000008', 56000),
    ('Ермаков', 'Максим', 'Владимирович', '000000000009', '1998-06-30', 'паспорт', '0009', '000009', 85000),
    ('Ковалева', 'Евгения', 'Елисеевна', '000000000010', '1996-05-05', 'паспорт', '0010', '000010', 140000);

INSERT INTO fms (passport_series, passport_number, validity)
VALUES
    ('0001', '000001', '2021-04-14'),
    ('0002', '000002', '2020-06-11'),
    ('0003', '000003', '2034-11-04'),
    ('0004', '000004', '2029-01-04'),
    ('0005', '000005', '2031-12-02'),
    ('0006', '000006', '2030-01-01'),
    ('0007', '000007', '2032-01-09'),
    ('0008', '000008', '2035-05-13'),
    ('0009', '000009', '2030-09-25'),
    ('0010', '000010', '2033-11-01');

INSERT INTO bki (passport_series, passport_number, monthly_load, overdue)
VALUES
    ('0001', '000001', 300000, False),
    ('0002', '000002', 0, False),
    ('0003', '000003', 250000, False),
    ('0004', '000004', 400000, True),
    ('0005', '000005', 240000, False),
    ('0006', '000006', 0, False),
    ('0007', '000007', 450000, False),
    ('0008', '000008', 2000000, True),
    ('0009', '000009', 0, False),
    ('0010', '000010', 5500000, True);

INSERT INTO users (
    surname, name, patronymic, phone, email, is_client, birthday, passport_series,
    passport_number, personal_data_consent, registration_address, residential_address)
VALUES
    ('Бобров', 'Андрей', 'Андреевич', '79780000001', 'client_1@mail.ru', True, '2000-05-03', '0001', '000001', True, '', ''),
    ('Харитонов', 'Марк', 'Петрович', '79780000002', 'client_2@mail.ru', True, '1995-11-14', '0002', '000002', True, '', ''),
    ('Гаврилов', 'Алекандр', 'Алексеевич', '79780000003', 'client_3@mail.ru', True, '2002-06-23', '0003', '000003', True, '', ''),
    ('Левин', 'Егор', 'Юрьевич', '79780000004', 'client_4@mail.ru', True, '1994-05-01', '0004', '000004', True, '', ''),
    ('Виноградов', 'Александр', 'Алексеевич', '79780000005', 'client_5@mail.ru', True, '1999-04-16', '0005', '000005', True, '', ''),

    ('Иванова', 'Алиса', 'Леонидовна', '79780000006', 'client_6@mail.ru', False, '1995-04-19', '0006', '000006', True, '', ''),
    ('Николаева', 'Алисия', 'Александровна', '79780000007', 'client_7@mail.ru', False, '2001-10-23', '0007', '000007', True, '', ''),
    ('Данилов', 'Максим', 'Даниилович', '79780000008', 'client_8@mail.ru', False, '1990-02-10', '0008', '000008', True, '', ''),
    ('Ермаков', 'Максим', 'Владимирович', '79780000009', 'client_9@mail.ru', False, '1998-06-30', '0009', '000009', True, '', ''),
    ('Ковалева', 'Евгения', 'Елисеевна', '79780000010', 'client_10@mail.ru', False, '1996-05-05', '0010', '000010', True, '', '');

INSERT INTO consumer_credits (name, max_period, min_interest_rate, max_amount, benefits)
VALUES
    ('Кредит особого назначения', 84, 5.5, 5000000, True),
    ('Кредит для работников предприятий ОПК и военнослужащих', 84, 5.5, 5000000, True),
    ('Кредит для госслужащих и бюджетников', 84, 7.5, 5000000, True),
    ('Кредит для держателей зарплатных карт', 84, 6.5, 5000000, False),
    ('Кредит для клиентов с кредитной историей ПСБ', 84, 9.5, 5000000, False),
    ('Кредит для вкладчиков ПСБ', 84, 9.5, 5000000, False),
    ('Рефинансирование кредитов', 84, 5.5, 5000000, False),
    ('Кредит «Открытый рынок»', 60, 14.5, 3000000, False);

INSERT INTO credit_cards (name, interest_free_period, max_amount, benefits)
VALUES
    ('Кредитная карта 100+', 101, 1000000, False),
    ('Кредитная карта «Двойной кешбэк»', 55, 1000000, False);

INSERT INTO mortgages (name, max_period, min_interest_rate, max_amount, benefits)
VALUES
    ('Семейная военная ипотека', 300, 4.3, 4770000, True),
    ('Военная ипотека 5,5%. Госпрограмма', 300, 5.5, 4230000, True),
    ('Военная ипотека (рефинансирование)', 300, 8.0, 3355000, True),
    ('Военная ипотека (покупка)', 300, 5.5, 4230000, True),
    ('Госпрограмма 2020', 360, 6.35, 30000000, False),
    ('Ипотека для ИТ-специалистов', 360, 5.0, 18000000, True),
    ('Новостройка (квартира)', 360, 9.5, 30000000, False),
    ('Новостройка (апартаменты)', 360, 9.5, 30000000, False),
    ('Новостройка (земельный участок)', 360, 10.10, 15000000, False),
    ('Вторичное жилье (квартира)', 360, 9.7, 30000000, False),
    ('Вторичное жилье (апартаменты)', 360, 9.9, 30000000, False),
    ('Вторичное жилье (земельный участок)', 360, 10.10, 15000000, False),
    ('Семейная ипотека', 360, 5.0, 12000000, False),
    ('Рефинансирование ипотеки', 360, 9.5, 20000000, False),
    ('Рефинансирование. Семейная ипотека', 360, 5.0, 12000000, False),
    ('Кредит под залог квартиры (на любые цели)', 240, 11.1, 10000000, False),
    ('Кредит под залог квартиры (на покупку другого жилья)', 360, 9.9, 30000000, False),
    ('Дальневосточная ипотека', 242, 1.5, 6000000, False);

