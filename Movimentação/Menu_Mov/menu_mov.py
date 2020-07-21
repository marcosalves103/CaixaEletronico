import os
import time
from src.Transactions import Transactions


transf = Transactions(1)


def saldo():
    transf.query()

    print("\nPara imprimir digite 1")
    print("Para finalizar a consulta digite 2")
    escolha = input("Digite o número: ")
    print()

    while(escolha != "1" and escolha != "2"):
        print("Digite corretamente...")
        escolha = input("Digite o número: ")
        print()

    if(escolha == "1"):
        print("Imprimindo...\n")
        time.sleep(2)


def trans():
    transf.transference()

    t = input("\nConfirmar a transação (Digite 1 para SIM ou 2 para NÃO)\n")
    while(t != "1" and t != "2"):
        t = input("\nConfirmar transação (Digite 1 para SIM ou 2 para NÃO)\n")

    if(t == "1"):
        print("Transferência Concluída")
        time.sleep(2)
    else:
        print("Voltando para o menu...")
        time.sleep(2)


def extrato():
    print("\n Histórico das operações\n")
    transf.statement()

    input("\nPressione enter para voltar para o menu")


def principal():
    while True:
        time.sleep(2)
        os.system("cls")
        print("===Banco Digital===")
        print("1 - Consulte seu saldo")
        print("2 - Realize uma transferência")
        print("3 - Consulte seu extrato")
        print("4 - Sair do sistema Banco")
        opcao = int(input("Digite o opção desejada:"))


        if opcao == 1:
            saldo()
        elif opcao == 2:
            trans()
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")


principal()
