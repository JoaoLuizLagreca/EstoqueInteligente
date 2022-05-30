import datetime
import json
import pandas as pd
import socket
from flask import Flask, jsonify, request
from exibicao import Exibicao
from alteracao import Alteracao
from cadastro import Cadastro

class Rotas (object):

    app = Flask(__name__)

    app.run(host='localhost', port=3307)

    @app.route('/estadoBalanca', methods = ['GET'])
    def estadoBalanca(conexao, peso, peso_medio):
        Exibicao.exibeEstadoBalanca(conexao, peso, peso_medio)

    @app.route('/dashboard', methods = ['GET'])
    def dashboard(conexao):
        Exibicao.exibeDadosDashboard(conexao)

    @app.route('/produtos', methods = ['POST'])
    def produtos(conexao):
        request.get_json

    @app.route('/atualizaPrateleira',  methods = ['GET'])
    def atualizaPrateleira(conexao, quantidade, capacidade, estado, produto, produto_id):


    @app.route('/cadastroProduto',  methods = ['POST'])
    def formulario(conexao, nome_produto, peso_medio, preco, quantidade_estoque):

    @app.route('/recebeDados',  methods = ['POST'])
    def recebeDados(conexao, quantidade, capacidade, estado, produto, produto_id):