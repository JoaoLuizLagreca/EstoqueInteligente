create database estoque_inteligente;
use estoque_inteligente;

create table Produto(
    id Integer primary key auto_increment,
    NomeProduto varchar(50) not null unique,
    Preco float,
    peso_medio float not null,
    estoque integer default 0
);

/*
estados:
0: INITIALIZING
1: STANDBY
2: OK
3: REQUESTING_STOCK
4: EMPTY
5: MISSPLACED_PRODUCT
*/
create table Prateleira(
    id integer primary key auto_increment,
    quantidade integer not null default 0,
    capacidade integer not null,
    estado tinyint not null default 0,
    produto integer not null,
    foreign key (produto) references Produto(id)
);

create table Log_de_estoque(
    data_estocagem datetime not null default sysdate(),
    quantidade integer not null,
    preco float,
    produto integer not null,
    foreign key (produto) references Produto(id)
);