CREATE DATABASE transactions if not exists;

 

USE transactions;

 

CREATE TABLE users(
id int not null,
saldo float not null,
extrato text not null,
created_at datetime,
updated_at datetime,
PRIMARY KEY(id)
);