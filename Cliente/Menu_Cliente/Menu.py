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


        if opcao == 4:
            print("\n Saindo do Programa...")
            break

principal()