class Alteracao ():

    def alteraPrateleira (conexao, quantidade, capacidade, estado, produto, id_prateleira):
        cursor = conexao.cursor()
        #sql = "CALL nome_procedimento(parâmetros)"
        sql = "UPDATE prateleira SET quantidade = %s, capacidade = %s, estado = %s, produto = %s WHERE id_prateleira = %s"
        data = (
            quantidade,
            capacidade,
            estado,
            produto,
            id_prateleira
        )
        cursor.execute(sql, data)
        conexao.commit()
        recordsaffected = cursor.rowcount
        cursor.close()
        conexao.close
        print(recordsaffected, "Prateleira alterada!")

    def alteraProduto(conexao, nome_produto, preco, peso_medio, estado, estoque, id_produto):
        cursor = conexao.cursor()
        sql = "UPDATE produto SET nome_produto = %s, preco = %s, peso_medio = %s, estoque = %s WHERE id_produto = %s"
        data = (
            nome_produto,
            preco,
            peso_medio,
            estoque,
            id_produto
        )
        cursor.execute(sql, data)
        conexao.commit()
        recordsaffected = cursor.rowcount
        cursor.close()
        conexao.close
        print(recordsaffected, "Produto(s) alterado(s)!")