import os
import time

from menu_poo.Cliente import Cliente
from menu_poo.db.clientes import clientes

class Main:

  def init(self):
    self.cliente = Cliente(clientes)

    while True:
      time.sleep(2)
      os.system("cls")

      print("===Banco Digital===")
      print("1 - Adicionar Cliente")
      print("2 - Alterar Cliente")
      print("3 - Excluir Cliente")
      print("4 - Buscar Cliente Pelo E-mail")
      print("5 - Buscar Cliente Pelo Identificador")
      print("6 - Listar Todos os Clientes")
      print("7 - Sair do Sistema de Banco")

      opcaoSelecionada = int(input("Digite o opção desejada: "))

      if opcaoSelecionada == 1:
        self.adicionarCliente()

      elif opcaoSelecionada == 2:
        self.alterarCliente()

      elif opcaoSelecionada == 3:
        self.excluirCliente()

      elif opcaoSelecionada == 4:
        self.buscarClientePeloEmail()

      elif opcaoSelecionada == 5:
        self.buscarClientePeloId()

      elif opcaoSelecionada == 6:
        self.listarTodosClientes()

      elif opcaoSelecionada == 7:
          print("Saindo do programa...")
          print("Inté...")
      else:
          print("Opcão incorreta, por favor digite novamente...")
      pass

  pass

  def adicionarCliente(self):
    cliente = {
      'email' : input("Digite o e-mail do usuário: "),
      'nome' : input("Digite o nome do usuário: "),
      'telefone' : input("Digite o telefone do usuário: ")
    }

    if self.cliente.buscarPeloEmail(cliente.get('email')):
      print("O e-mail do cliente já existe.")
      return
      pass

    self.cliente.adicionar(cliente)

    pass

  def alterarCliente(self):
    cliente = {
      'email' : input("Digite o e-mail do cliente: "),
      'nome' : input("Digite o nome do cliente: "),
      'telefone' : input("Digite o telefone do cliente: ")
    }

    cliente_id = int(input("Digite o identificador do usuário: "))
    if self.cliente.alterar(cliente_id, cliente):
      print("Dados do cliente atualizados com sucesso.")
      return
      pass

    print("O Cliente não existe.")
    pass

  def excluirCliente(self):
    cliente_id = int(input("Digite o identificador do cliente: "))

    if self.cliente.excluir(cliente_id):
      print("Cliente excluído.")
      return
      pass

    print("O Cliente não existe.")
    pass

  def buscarClientePeloEmail(self):
    email = input("Digite o e-mail do Cliente: ")

    cliente = self.cliente.buscarPeloEmail(email)
    if cliente:
      print(cliente)
      input("Pressione Enter para continuar...")
      return
      pass

    print("O Cliente não existe.")
    pass

  def buscarClientePeloId(self):
    cliente_id = int(input("Digite o identificador do Cliente: "))

    cliente = self.cliente.buscarPeloId(cliente_id)
    if cliente:
      print(cliente)
      input("Pressione qualquer tecla para continuar...")
      return
      pass

    print("O Cliente não existe.")
    pass

  def listarTodosClientes(self):
    clientes = self.cliente.listarTodos()
    print(clientes)
    input("Pressione qualquer tecla para continuar...")
    pass


