class Cliente:

  def __init__(self, listaClientes):
    self.listaClientes = listaClientes
    pass

  def buscarPeloEmail(self, email):

    #Percorre a lista de clientes
    for cliente_id in self.listaClientes:
      cliente = self.listaClientes[cliente_id]

      #Verifica se o email do cliente corresponde ao recebido
      if cliente.get('email') == email:
        return cliente
      pass

    #cliente não foi encontrado
    return False
    pass

  def adicionar(self, cliente):

    #Gera o id do usuário
    cliente_id = len(self.listaClientes) + 1
    print(cliente_id)
    #Insere o cliente
    self.listaClientes[cliente_id] = cliente
    pass

  def alterar(self, iD, cliente):

    for cliente_id in self.listaClientes:

      #Procura pelo cliente com o mesmo ID
      if cliente_id == iD:
        #Atualiza todos os dados do usuário
        self.listaClientes[cliente_id] = cliente

        return True
      pass

    #O cliente não foi encontrado
    return False
    pass
  def excluir(self, cliente_id):

    #Exclui o usuário
    #Caso o cliente não seja encontrado, retorna False
    return self.listaClientes.pop(cliente_id, False)

    pass

  def buscarPeloId(self, iD):

    for cliente_id in self.listaClientes:

      #Procura pleo cliente com o mesmo ID
      if cliente_id == iD:
        return self.listaClientes[cliente_id]
      pass

    #cliente não foi encontrado
    return False
    pass


  def listarTodos(self):

    #Retorna todos os clientes da lista
    return self.listaClientes
    pass

  pass