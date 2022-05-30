use estoque_inteligente;

delimiter $$
create procedure adicionarProduto(nome_produto varchar(50), preco float, peso_medio float)
begin
    insert into produto(nome_produto, preco, peso_medio) values (
        nome_produto,
        preco,
        peso_medio
    );
end $$

delimiter $$
create procedure compra(id_produto integer, quantidade integer)
begin
    if quantidade > 0 then
        select @estoque_atual := estoque from Produto where produto_id=id_produto;

        if @estoque_atual - quantidade < 0 then
            # Relatar erro
            signal SQLSTATE 'ERROR'
            set MESSAGE_TEXT = 'Estoque seria inferior à 0 com essa quantidade';
        else
            update produto set estoque = @estoque_atual - quantidade where produto_id=id_produto;
        end if;
    else
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade inválido';
    end if;
end $$

delimiter $$
create procedure reestocar(id_produto integer, quantidade integer)
begin
    if quantidade <= 0 then
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade inválido';
    else
        select @estoque_atual := estoque from produto where produto_id = id_produto;
        update produto set estoque = @estoque_atual + quantidade where produto_id= id_produto;
    end if;
end $$

delimiter $$
create procedure criarPrateleira(produto_nome varchar(50), capacidadeP integer)
begin
    insert into prateleira(capacidade, produto) values(
    capacidadeP,
    (select produto_id from produto where nome_produto=produto_nome)
);
end $$