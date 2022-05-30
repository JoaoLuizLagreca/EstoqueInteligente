from conexao import Conexao
from cadastro import Cadastro
from exclusao import Exclusao
from calculos import Calculos
from alteracao import Alteracao
from exibicao import Exibicao
from compra import Compra
from restoque import Restoque


def main():
        host_database = "localhost"
        user_database = "root"
        pass_database = ""
        name_database =  "estoque_inteligente"

        nome_produto = "Bolacha laercio"
        preco = 2
        peso_medio = 100
        estoque = 2
        peso = 90
        capacidade = 10
        quantidade = 1
        estado = 4
        produto = 20
        id_prateleira = 1
        id_produto = 1

        conexao = Conexao.conectaBancoDeDados(host_database, user_database, pass_database, name_database)

        print(conexao)

        if (conexao):
            print("Conexão realizada com sucesso!") #Sucesso
        else:
            print("Não foi possível realizar a conexão.") #Falha

        #Cadastro.cadastroProduto(conexao, nome_produto, preco, peso_medio, estoque)
        #Exclusao.deletaProduto(conexao, id_produto)
        #Calculos.calculaEstado(peso, peso_medio)
        #Alteracao.alteraPrateleira(conexao, quantidade, capacidade, estado, produto, id_prateleira)
        #Alteracao.alteraProduto(conexao, nome_produto, preco, peso_medio, estado, estoque, id_produto)
        Exibicao.exibeDadosDashboard(conexao)
        #Exibicao.exibeEstadoBalanca(conexao, peso, peso_medio)
        #Compra.compraProduto(conexao, id_produto, quantidade)
        #Restoque.restoqueProduto(conexao, id_produto, quantidade)




main()
