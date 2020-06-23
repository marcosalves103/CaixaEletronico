import os
import time
def existe_cliente(lista, email):
    if len(lista) > 0:
        for cliente in lista:
            if cliente['email'] == email:
                 return True
    return False

def adicionar(lista):
    while True:
        email = input("Digite o e-mail do cliente:")

        if not existe_cliente(lista, email):
            break
        else:
            print("Esse e-mail já foi utilizado.")
            print("Por favor, digite um novo e-mail.")

        #nesse passo, o e-mail recebido será único
        #chamamos de dicionario
    cliente = {
        "email": email,
        "nome": input("Digite o nome:"),
        "tel": input("Digite o telefone:")
    }
    lista.append(cliente) #adiciona no final da lista

    print("O cliente {} foi cadastrado com sucesso!\n".format(cliente['nome']))
def alterar():
    pass

def excluir():
    pass

def buscar():
    pass

def listar():
    pass

def principal():
    lista = [] # inicializa a lista vazia
    while True:
        time.sleep(2)
        os.system("cls");
        print("===Banco Digital===")
        print("1 - Adicionar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Buscar Cliente")
        print("5 - Listar Cliente")
        print("6 - Sair do sistema Banco")
        opcao = int(input("Digite o opção desejada:"))

        if opcao == 1:
            adicionar(lista)
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            print("Saindo do programa...")
            print("Inté...")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")

principal()