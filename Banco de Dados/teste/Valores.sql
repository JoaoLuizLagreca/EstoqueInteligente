use estoque_inteligente;

call adicionarProduto('Anti-pulgas', 15.45, 0.80);
call criarPrateleira('Anti-pulgas', 30);
call reestocar('Anti-pulgas', 50);

call compra('Anti-pulgas', 4);
call compra('Anti-pulgas', 2);