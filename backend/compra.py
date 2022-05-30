class Compra ():

    def compraProduto(conexao, id_produto, quantidade):
        cursor = conexao.cursor()
        sql = "CALL compra(%s,%s)"
        #sql = "INSERT INTO produto (nome_produto, preco, peso_medio, estoque) VALUES (%s, %s, %s, %s)"
        data = (
            id_produto,
            quantidade
        )
        cursor.execute(sql,data)
        conexao.commit()
        id_produto = cursor.lastrowid
        cursor.close()
        conexao.close()
        print("Uma compra foi efetuada!")
