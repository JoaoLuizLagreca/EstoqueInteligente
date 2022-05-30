create database estoque_inteligente;
use estoque_inteligente;

create table produto(
    id_produto Integer primary key auto_increment,
    nome_produto varchar(50) not null unique,
    preco float,
    peso_medio float not null,
    estoque integer default 0
);

create table prateleira(
    id_prateleira integer primary key auto_increment,
    quantidade integer not null default 0,
    capacidade integer not null,
    estado tinyint not null default 0,
    produto integer not null,
    foreign key (produto) references produto(id_produto)
);

create table log_de_estoque(
    data_estocagem datetime not null default sysdate(),
    quantidade integer not null,
    preco float,
    produto integer not null,
    foreign key (produto) references produto(id_produto)
);