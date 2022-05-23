use estoque_inteligente;

insert into Produto(NomeProduto, Preco, peso_medio) values (
    'Anti-pulgas',
    15.45,
    0.80
);

insert into Prateleira(capacidade, produto) values(
    30,
    (select id from Produto where NomeProduto='Anti-pulgas')
);