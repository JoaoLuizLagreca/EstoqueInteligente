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
create procedure compra(id integer, quantidade integer)
begin
    if quantidade > 0 then
        select @estoque_atual := estoque from produto where id_produto=id;

        if @estoque_atual - quantidade < 0 then
            # Relatar erro
            signal SQLSTATE 'ERROR'
            set MESSAGE_TEXT = 'Estoque seria inferior à 0 com essa quantidade';
        else
            update produto set estoque = @estoque_atual - quantidade where id_produto=id;
        end if;
    else
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade inválido';
    end if;
end $$

delimiter $$
create procedure reestocar(id integer, quantidade integer)
begin
    if quantidade <= 0 then
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade inválido';
    else
        select @estoque_atual := estoque from produto where id_produto = id;
        update produto set estoque = @estoque_atual + quantidade where id_produto = id;
    end if;
end $$

delimiter $$
create procedure criarPrateleira(produto_nome varchar(50), capacidadeP integer)
begin
    insert into prateleira(capacidade, produto) values(
    capacidadeP,
    (select id_produto from produto where nome_produto=produto_nome)
);
end $$

delimiter $$
create procedure atualizarQuantidadeNaPrateleira(id integer, qtd integer)
begin

     if qtd < 0 then
        # Relatar erro
        signal SQLSTATE 'ERROR'
        set MESSAGE_TEXT = 'Valor quantidade não pode ser menor que 0';
    else
        update prateleira set quantidade = qtd where id_prateleira=id;
    end if;

    
end$$