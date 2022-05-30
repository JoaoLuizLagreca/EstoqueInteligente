class Cadastro ():

    def cadastroProduto(conexao, nome_produto, preco, peso_medio, estoque):
        cursor = conexao.cursor()
        sql = "INSERT INTO produto (nome_produto, preco, peso_medio, estoque) VALUES (%s, %s, %s, %s)"
        data = (
            nome_produto,
            preco,
            peso_medio,
            estoque
        )
        cursor.execute(sql,data)
        conexao.commit()
        id_produto = cursor.lastrowid
        cursor.close()
        conexao.close()
        print("Foi cadastrado um novo produto! O Id é:", id_produto)


