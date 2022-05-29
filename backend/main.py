from conexao import Conexao
from cadastro import Cadastro
from exclusao import Exclusao
from calculos import Calculos
from alteracao import Alteracao
from exibicao import Exibicao

class Main ():

    def main():
        host_database = "localhost"
        user_database = ""
        pass_database = ""
        name_database =  "estoque_inteligente"

        nome_produto = "Biscoito Suzana"
        preco = 3
        peso_medio = 100
        estoque = 2
        id_produto = 1
        peso = 90
        capacidade = 10
        quantidade = 1
        estado = 4
        produto = 20
        prateleira_id = 1
        produto_id = 1

        conexao = Conexao.conectaBancoDeDados(host_database, user_database, pass_database, name_database)

        print(conexao)

        if (conexao):
            print("Conexão realizada com sucesso!") #Sucesso
        else:
            print("Não foi possível realizar a conexão.") #Falha

        Cadastro.cadastroProduto(conexao, nome_produto, preco, peso_medio, estoque)
        #Exclusao.deletaProduto(conexao, id_produto)
        #Calculos.calculaEstado(peso, peso_medio)
        #Alteracao.alteraPrateleira(conexao, quantidade, capacidade, estado, produto, prateleira_id)
        #Alteracao.alteraProduto(conexao, nome_produto, preco, peso_medio, estado, estoque, produto_id)
        #Exibicao.exibeDadosDashboard(conexao)
        #Exibicao.exibeEstadoBalanca(conexao, peso, peso_medio)
