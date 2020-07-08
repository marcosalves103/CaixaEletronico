import os


print("Bem-vindo!")

class Proj:

  def init(req):
    while True:

      os.system("cls")

      print("1 - Realizar saque")
      
      print("2 - Realiazar depósito")
      
      print("3 - Efeturar pagamento")

      print (" ")

      selecionado = int(input("Digite o opção desejada: "))

      if selecionado == 1:
        req.saqueCliente()

      elif selecionado == 2:
        req.depositoCliente()

      elif selecionado == 3:
        req.pagamentoCliente()
  pass

  def saqueCliente(req):
    dinheiro = {
      input("Informe o quanto gostaria de sacar: ")
    }
    pass

  def depositoCliente(req):
    quantidade = {
      input("Informe o quanto gostaria de depositar: "),
      input("Informe a conta para onde o depóstio irá: "),
    }
    pass

  def pagamentoCliente(req):
    pag = {
      input("Informe o quanto será pago: "),
      input("Informe a conta para onde o pagamento irá: "),
    }
    pass
    

  


