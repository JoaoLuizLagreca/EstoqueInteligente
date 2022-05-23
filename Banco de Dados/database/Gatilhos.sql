use estoque_inteligente;

delimiter $$
create trigger estoque_mudanca after update on Produto for each row
begin
    insert into Log_de_estoque(quantidade, preco, produto) values(
        new.estoque - old.estoque,
        old.Preco,
        new.id
    );
end $$