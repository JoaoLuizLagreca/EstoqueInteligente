import datetime
import json
import pandas as pd
from conexao import Conexao
from calculos import Calculos

class Exibicao ():

    def exibeDadosDashboard(conexao):
        cursor = conexao.cursor()
        sql = "SELECT MONTHNAME(data_estocagem), SUM(quantidade) FROM log_de_estoque GROUP BY MONTHNAME(data_estocagem)"
        cursor.execute(sql)
        consulta = cursor.fetchall()
        cursor.close()
        conexao.close()
        json_dados_dashboard = ""
        for linha in consulta:
            print(linha)
            df_dados_dashboard = pd.DataFrame(consulta)
            consulta = df_dados_dashboard.to_json(orient="records")
            parsed = json.loads(consulta)
            json_dados_dashboard = json.dumps(parsed, indent=4)
            print(json_dados_dashboard)

        return json_dados_dashboard

    def exibeProdutos(conexao):
        cursor = conexao.cursor()
        sql = "SELECT DISTINCT(nome_produto), id_produto FROM produto"
        cursor.execute(sql)
        consulta = cursor.fetchall()
        cursor.close()
        conexao.close()
        json_dados_dashboard = ""
        for linha in consulta:
            print(linha)
            json_dados_produto = pd.DataFrame(consulta)
            consulta = json_dados_produto.to_json(orient="records")
            parsed = json.loads(consulta)
            json_dados_dashboard = json.dumps(parsed, indent=4)
            print(json_dados_produto)

        return json_dados_dashboard

    def exibeEstadoBalanca(conexao, peso, peso_medio):
        cursor = conexao.cursor()
        sql = "SELECT * FROM prateleira"
        cursor.execute(sql)
        consulta = cursor.fetchall()
        cursor.close()
        conexao.close()
        json_estado_balanca = ""
        for linha in consulta:
            print(linha)
            Calculos.calculaEstado(peso, peso_medio)
            df_estado_balanca = pd.DataFrame(consulta)
            consulta = df_estado_balanca.to_json(orient="records")
            parsed = json.loads(consulta)
            json_estado_balanca = json.dumps(parsed, indent=4)
            print(json_estado_balanca)

        return json_estado_balanca
