class Alteracao ():

    def alteraPrateleira(self, conexao, quantidade, capacidade, estado, produto, prateleira_id):
        cursor = conexao.cursor()
        sql = "UPDATE prateleira SET quantidade = %s, capacidade = %s, estado = %s, produto = %s WHERE prateleira_id = %s"
        data = (
            quantidade,
            capacidade,
            estado,
            produto,
            prateleira_id
        )
        cursor.execute(sql, data)
        conexao.commit()
        recordsaffected = cursor.rowcount
        cursor.close()
        conexao.close
        print(recordsaffected, "Prateleira alterada!")

    def alteraProduto(self, conexao, nome_produto, preco, peso_medio, estado, estoque, produto_id):
        cursor = conexao.cursor()
        sql = "UPDATE produto SET nome_produto = %s, preco = %s, peso_medio = %s, estoque = %s WHERE produto_id = %s"
        data = (
            nome_produto,
            preco,
            peso_medio,
            estoque,
            produto_id
        )
        cursor.execute(sql, data)
        conexao.commit()
        recordsaffected = cursor.rowcount
        cursor.close()
        conexao.close
        print(recordsaffected, "Produto(s) alterado(s)!")