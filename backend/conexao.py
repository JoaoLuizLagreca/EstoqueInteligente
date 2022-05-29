import mysql.connector

class Conexao ():
    
    def conectaBancoDeDados(self,db_host, db_user, db_pass, db_name):
        conexao = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_pass,
        database = db_name
    )
        return conexao
