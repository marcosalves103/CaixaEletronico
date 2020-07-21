import os
import time

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
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'dinheiroNaMaquina.txt')


    arquivo = open(filename, 'r')
    quantidadeNoCaixa = arquivo.read()
    print("Quantidade disponível no caixa: "+quantidadeNoCaixa)
    arquivo.close()

    int(float(quantidadeNoCaixa))

    dinheiro = int(input("Informe o quanto gostaria de sacar: "))

    if dinheiro<=int(float(quantidadeNoCaixa)):
      arquivoEscrita = open(filename, 'w')
      #arquivoEscrita.seek(0)
      quantidade = int(float(quantidadeNoCaixa))-dinheiro
      arquivoEscrita.write(str(quantidade))
      #arquivoEscrita.truncate()
      arquivoEscrita.close()
      print("Operação concluida com sucesso. Você sacou: "+"R$"+str(dinheiro))
    else:
      print("Quantidade não disponível. Por favor, insira manualmente mais dinheiro, ou tente novamente mais tarde")


    

    time.sleep(2)
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
    

  


