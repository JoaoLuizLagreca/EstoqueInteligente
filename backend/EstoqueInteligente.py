import mysql.connector
import datetime
import json
import pandas as pd
import socket

#iniciando conexão com o banco de dados mySQL
def connect(db_host, db_user, db_pass, db_name): #criando conexão com o banco de dados (local)
    connection = mysql.connector.connect(
    host = db_host,
    user = db_user,
    password = db_pass,
    database = db_name
)
    return connection

#iniciando CRUD
def create(connection, quantidade, capacidade, estado, produto):
    cursor = connection.cursor() #Criando um cursor
    sql = "INSERT INTO prateleira (quantidade, capacidade, estado, produto) VALUES (%s, %s, %s, %s)"
    data = (
        quantidade,
        capacidade,
        estado,
        produto
    )
    cursor.execute(sql,data)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    connection.close()
    print("Foi cadastrado um novo produto!! O Id é:", id)

def read(connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM prateleira"
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

def update(connection, quantidade, capacidade, estado, produto):
    cursor = connection.cursor()
    sql = "UPDATE prateleira SET quantidade = %s, capacidade = %s, estado = %s, produto = %s WHERE produto_id = %s"
    data = (
        quantidade,
        capacidade,
        estado,
        produto,
        id
    )
    cursor.execute(sql, data)
    connection.commit()
    recordsaffected = cursor.rowcount
    cursor.close()
    connection.close
    print(recordsaffected, "Produtos alterados!")

def delete(connection, id):
    cursor = connection.cursor()
    sql = "DELETE FROM prateleira WHERE id = %s"
    data = (
        id,
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

    if (connection):
        print("Conexão realizada com sucesso!") #Sucesso
    else:
        print("Não foi possível realizar a conexão.") #Falha

application = Flask(__name__)

#state = { "value" : 1}

@application.route('/', methods =['GET'])
def home():
    return "Seja Bem Vindo ao VNCS-13"

@application.route('/GetFox', methods =['GET'])
def GetState():
    return jsonify(state)

@application.route('/AppChangeState', methods =['GET'])
def AppChangeState():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = s.recv(3621)

    # if state['value'] == 1:
    #     state['value'] = 0
    # else:
    #     state['value'] = 1

    # return jsonify(state)

@application.route('/PostFox', methods =['POST'])
def PostFox():
    #data = request.get_json('localhost:3621')

    #state.update(data)

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='localhost', port=80)
    main(1)
