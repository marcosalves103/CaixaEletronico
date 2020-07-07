import os
import time

def carregar_cliente():
    lista = []

    try:
        arquivo = open("clientes.txt", "r")

        for linha in arquivo.readlines(): #armazena em linha a o valor da linha
            coluna = linha.strip().split("#") #coluna recebe agora um vetor
            cliente = {
                "email": coluna[1],
                "nome": coluna[0],
                "tel": coluna[2]
            }
            lista.append(cliente)

        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não existe - Criar....")
        pass

    return lista

def salvar_cliente(lista):

    arquivo = open("clientes.txt", "w")#se não existir arquivo cria um novo

    for cliente in lista:
        arquivo.write('{}#{}#{}\n'.format(cliente['nome'], cliente['email'], cliente['tel']))

    arquivo.close()

def existe_cliente(lista, email):
    if len(lista) > 0:
        for cliente in lista:
            if cliente['email'] == email:
                 return True
    return False

def adicionar(lista):
    while True:
        email = input("Digite o e-mail do cliente: ")

        if not existe_cliente(lista, email):
            break
        else:
            print("Esse e-mail já foi utilizado.")
            print("Por favor, digite um novo e-mail.")
            time.sleep(2)
            os.system("cls")
        #nesse passo, o e-mail recebido será único
        #chamamos de dicionario
    cliente = {
        "email": email,
        "nome": input("Digite o nome: "),
        "tel": input("Digite o telefone: ")
    }
    lista.append(cliente) #adiciona no final da lista

    print("O cliente {} foi cadastrado com sucesso!\n".format(cliente['nome']))
    time.sleep(2)
    os.system("cls")

def alterar():
    pass

def excluir():
    pass

def buscar():
    pass

def listar(lista):
    print("==Lista de Clientes==")
    if len(lista) > 0:
        for i, cliente in enumerate(lista):
            print("Contato {}".format(i+1))
            print("\tNome: {}".format(cliente['nome']))
            print("\tEmail: {}".format(cliente['email']))
            print("\tTelefone: {}".format(cliente['tel']))
            print("===============================================")
        print("Quantidade de Clientes: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")

def principal():
    lista = carregar_cliente() # inicializa a lista de clientes
    while True:
        time.sleep(2)
        os.system("cls")
        print("===Banco Digital===")
        print("1 - Adicionar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Excluir Cliente")
        print("4 - Buscar Cliente")
        print("5 - Listar Cliente")
        print("6 - Sair do sistema Banco")
        opcao = int(input("Digite o opção desejada:"))

        if opcao == 1:
            adicionar(lista) # unica construída
            salvar_cliente(lista)

        elif opcao == 2:
            alterar()
            salvar_cliente(lista)

        elif opcao == 3:
            excluir()
            salvar_cliente(lista)

        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print("Saindo do programa...")
            print("Inté...")
            time.sleep(2)
            os.system("cls")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")
            time.sleep(2)
            os.system("cls")

principal()