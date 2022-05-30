class Exclusao ():

    def deletaProduto(conexao, id_produto):
        cursor = conexao.cursor()
        sql = "DELETE FROM produto WHERE id_produto = %s"
        data = (
            id_produto,
        )
        cursor.execute(sql,data)
        conexao.commit
        recordsaffected = cursor.rowcount
        conexao.close()
        cursor.close()
        print (recordsaffected, "Produtos excluídos")