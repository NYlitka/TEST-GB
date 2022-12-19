-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT(3) NOT NULL,
  adress TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Новиков Иван',42, 'Москва');
INSERT INTO EMPLOYEE VALUES (0002, 'Гусева Марина', 45,'Калининград');
INSERT INTO EMPLOYEE VALUES (0003, 'Петров Алексей', 17,'Омск');
INSERT INTO EMPLOYEE VALUES (0004, 'Дубровская Анастасия', 18,'Sales');
INSERT INTO EMPLOYEE VALUES (0005, 'Бутова Анна', 20,'Москва');
INSERT INTO EMPLOYEE VALUES (0006, 'Кузьмина Полина',34,'Sales');
INSERT INTO EMPLOYEE VALUES (0007, 'Новикова Юлия', 21,'Москва');

-- fetch 
SELECT name FROM EMPLOYEE WHERE age <30 and age >17 and adress = 'Москва' ;
