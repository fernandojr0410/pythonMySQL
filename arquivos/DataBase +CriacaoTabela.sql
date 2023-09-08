create database projetoPython;

use projetoPython;

create table Cliente (
IdCliente int auto_increment not null,
Nome varchar(45) not null,
Idade int not null,
primary key (IdCliente)
);

create table Produto(
idProduto int auto_increment not null
)