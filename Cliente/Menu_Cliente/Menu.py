import os
import time


def principal():
    lista = [] # inicializa a lista vazia
    while True:
        time.sleep(2)
        os.system("cls");
        print(" === MÓDULO CLIENTE === ")
        print("1 - Cadastrar Banco ou Fintech")
        print("2 - Editar Cadastro")
        print("3 - Listar Banco ou Fintech")
        print("4 - Sair do Sistema do Banco")
        opcao = int(input("Digite o Opção Desejada:"))

        if opcao == 1:
            print("\n Digite o Nome da Empresa:")
            print("\n Digite o CNPJ da Empresa:")
            print("\n Digite Localização da Empresa:")
            print("\n Digite a Inscrição Estadual da Empresa:")
            print("\n Escolher Funcionalidades: S ou N")
        # print("\n  - Saque:")
        # print("\n  - Depósito:")
        # print("\n  ...")

        if opcao == 2:
            print("\n Digite o CNPJ da Empresa:")
            print("\n Digite um Novo Nome:")
            print("\n Digite uma Nova Localização:")
            print("\n Digite uma Nova Inscrição Estadual:")
            print("\n Escolha Novas Funcionalidades:")
        # print("\n  - Saque:")
        # print("\n  - Depósito:")
        # print("\n  ...")
            print("\n Escolha o Estado do Banco:")
        # print("\n  Ativo: S ou N")

        if opcao == 3:
            #print("\n DECIDIR POR PEGAR INDIVIDUAL PELO NOME DO ARQUIVO OU COLETIVO DE TODAS EMPRESAS PELA PASTA COM TODOS ARQUIVOS ARMAZENADOS")

            #INDIVIDUAL
            print("\n Digite o CNPJ da Empresa:")

            #GERAL
            #LISTAR DIRETO
            #opção de parar de listar

        if opcao == 4:
            print("\n Saindo do Programa...")
            break

principal()
