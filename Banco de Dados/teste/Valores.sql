use estoque_inteligente;

call adicionarProduto('Anti-pulgas', 15.45, 0.80);
call criarPrateleira(1, 30);
call reestocar(1, 50);

call compra(1, 4);
call compra(1, 2);