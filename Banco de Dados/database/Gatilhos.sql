use estoque_inteligente;

delimiter $$
create trigger estoque_mudanca after update on produto for each row
begin
    insert into log_de_estoque(quantidade, preco, produto) values(
        new.estoque - old.estoque,
        old.preco,
        new.id_produto
    );
end $$