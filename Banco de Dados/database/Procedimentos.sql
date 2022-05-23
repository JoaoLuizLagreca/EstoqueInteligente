use estoque_inteligente;

delimiter $$
create procedure adicionarProduto(NomeProduto varchar(50), Preco float, Peso_medio float)
begin
    insert into Produto(NomeProduto, Preco, peso_medio) values (
        NomeProduto,
        Preco,
        Peso_medio
    );
end $$

delimiter $$
create procedure compra(produto_id integer, quantidade integer)
begin
    if quantidade > 0 then
        select @estoque_atual := estoque from Produto where id=produto_id;

        if @estoque_atual - quantidade < 0 then
            # Relatar erro
            signal SQLSTATE 'ERROR'
            set MESSAGE_TEXT = 'Estoque seria inferior à 0 com essa quantidade';
        else
            update Produto set estoque = @estoque_atual - quantidade where id=produto_id;
        end if;
    else
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade inválido';
    end if;
end $$

delimiter $$
create procedure reestocar(produto_id integer, quantidade integer)
begin
    if quantidade <= 0 then
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade inválido';
    else
        select @estoque_atual := estoque from Produto where id=produto_id;
        update Produto set estoque = @estoque_atual + quantidade where id=produto_id;
    end if;
end $$

delimiter $$
create procedure criarPrateleira(produto_nome varchar(50), capacidadeP integer)
begin
    insert into Prateleira(capacidade, produto) values(
    capacidadeP,
    (select id from Produto where NomeProduto=produto_nome)
);
end $$
