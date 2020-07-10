import os
import time

def menu():
    lista = [] # lista vazia
    while True:
        time.sleep(2)
        os.system("cls")
        print("======== MENU CLIENTE =======")
        print("1 - Cadastrar Banco ou Fintech")
        print("2 - Alterar Banco ou Fintech")
        print("3 - Listar Bancos e Fintechs")
        print("4 - Excluir Banco ou Fintech")
        print("5 - Sair do Sistema de Cliente")
        print("==============================")
        try:
            opcao = int(input("Digite o opção desejada: "))
            if 1 <= opcao <= 5:
                if opcao == 1:
                    print("Não programado ainda.")
                elif opcao == 2:
                    print("Não programado ainda.")
                elif opcao == 3:
                    print("Não programado ainda.")
                elif opcao == 4:
                    print("Não programado ainda.")
                else:
                    print("Saindo do Programa...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("Êxito em sair do programa.")
                    break
            else:
                print("A entrada não pertence a uma das opções.")
        except:
            print("A entrada não é válida.")


menu()