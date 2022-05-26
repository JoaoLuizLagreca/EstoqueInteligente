import mysql.connector
import datetime
import json
import pandas as pd
#iniciando conexão com o banco de dados mySQL
def connect(db_host, db_user, db_pass, db_name): #criando conexão com o banco de dados (local)
    connection = mysql.connector.connect(
    host = db_host, #host do banco
    user = db_user, #usuário
    password = db_pass, #senha
    database = db_name #nome do banco de dados
)
    return connection

#iniciando CRUD
def create(connection, nome_produto, preco, peso_medio):
    cursor = connection.cursor() #Criando um cursor
    sql = "INSERT INTO produtos (nome_produto, preco, peso_medio, hora_cadastro) VALUES (%s, %s, %s, %s)" #String da query que o sistema vai rodar no banco
    data = (
        nome_produto, #Nome do produto que será inserido na tabela produtos
        preco, #Preço do produto que será inserido na tabela produtos
        peso_medio,#Preço médio do produto que será inserido na tabela produtos
        str(datetime.datetime.today()) #Horário em que o produto está sendo cadastrado no banco
    )
    cursor.execute(sql,data) #Executando o cursor que foi declarado acima da linha 11 até a linha 17
    connection.commit() #Executando o commit no banco para que não fique nenhuma transação (mesmo sendo um insert)
    produto_id = cursor.lastrowid #Pegando o id da última linha inserida na tabela, ocorreu da linha 11 à linha 17
    cursor.close() #Fechando cursor que foi aberto na linha 11
    connection.close() #Fechando conexão que foi aberta na linha 4
    print("Foi cadastrado um novo produto!! O Id é:", produto_id) #Exibindo o id da última linha cadastrada que pegamos na linha 22

def read(connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM produtos" #Exibição de todos os itens da tabela produtos
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    for result in results:
        print(result)

    df = pd.DataFrame(results)
    consulta = df.to_json(orient="records")
    parsed = json.loads(consulta)
    json.dumps(parsed, indent=4)

    print(consulta)

def update(connection, novo_nome_produto, novo_preco, novo_peso_medio, produto_id):
    cursor = connection.cursor()
    sql = "UPDATE produtos SET nome_produto = %s, preco = %s, peso_medio = %s WHERE produto_id = %s"
    data = (
        novo_nome_produto,
        novo_preco,
        novo_peso_medio,
        produto_id
    )
    cursor.execute(sql, data)#Executando o cursor que foi declarado acima
    connection.commit() #Executando o commit no banco para que não fique nenhuma transação
    recordsaffected = cursor.rowcount #Pegando o número de registros alterados no banco
    cursor.close() #Fechando cursor
    connection.close #Fechando conexão do banco
    print(recordsaffected, "Produtos alterados!") #Mostrando a quantidade de produtos afetados

def delete(connection, id_produto):
    cursor = connection.cursor()
    sql = "DELETE FROM produtos WHERE id_produto = %s"
    data = (
        id_produto,
    )
    cursor.execute(sql,data)
    connection.commit
    recordsaffected = cursor.rowcount
    connection.close()
    cursor.close()
    print (recordsaffected, "Produtos excluídos")

def main(connection):
    host_database = input("Insira o host do banco de dados")
    user_database = input("Insira o nome do banco de dados")
    pass_database = input("Insira a senha do banco de dados")
    name_database = input("Insira o nome do banco de dados")

    connect(host_database, user_database, pass_database, name_database)

    if (connection): #Verifica se foi possível realizar a conexão com o banco
        print("Conexão realizada com sucesso!") #Sucesso
    else:
        print("Não foi possível realizar a conexão.") #Falha


if __name__ == "__main__":
    main(1)
