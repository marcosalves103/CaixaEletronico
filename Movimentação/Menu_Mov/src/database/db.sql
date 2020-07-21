drop database transactions;
CREATE DATABASE transactions;

 

USE transactions;

 

CREATE TABLE users(
id int not null,
saldo float not null,
created_at datetime,
updated_at datetime,
PRIMARY KEY(id)
);

CREATE TABLE extrato(
id_extrato int not null auto_increment,
id_conta int not null,
id_origem int not null,
id_destino int not null,
valor decimal(10,2) not null,
tipo varchar(15) not null,
data_extrato datetime not null,
constraint `fk_usuarioExt`
foreign key(`id_conta`)
references transactions.users(`id`),
primary key(`id_extrato`)
);


insert into users values(1,3000, '2020/03/03', '2020/07/13');
insert into users values(2,1000,  '2020/03/03', '2020/07/13');
select * from users;
select * from extrato;