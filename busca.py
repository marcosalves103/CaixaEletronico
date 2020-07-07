import os

#Funções
def cadastrar():
    n = input('Digite seu nome: ')
    s = input('Digite seu sobrenome: ')
    t = int(input('Digite seu telefone: '))
    e = input('Digite seu email: ')
    agenda = open('%s_%s.txt' %(n,s),'a')
    agenda.write('%s %s, %d, %s\n'%(n, s, t, e))
    agenda.close()

def buscar():
    n = input('Digite o nome do contato a ser pesquisado: ')
    s = input('Digite o sobrenome do contato a ser pesquisado: ')

    if os.path.isfile('%s_%s.txt'%(n,s)):
          agenda = open('%s_%s.txt'%(n,s),'r')
    
          for x in agenda.readlines():
                print(x)
          agenda.close()

    else:
       print('Contato não encontrado.') 


# Outra maneira
#def buscar():
#    n = input('Digite o nome do contato a ser pesquisado: ')
#    s = input('Digite o sobrenome do contato a ser pesquisado: ')
#
#    try:
#      agenda = open('%s_%s.txt'%(n,s),'r')
#
#      for x in agenda.readlines():
#          print(x)
#
#     agenda.close()
#    except:
#      print('Contato não encontrado.')       

def deletar():
    n = input('Digite o nome que deseja apagar: ')
    s = input('Digite o sobrenome que deseja apagar: ')
    os.remove('%s_%s.txt'%(n,s))

#Função principal

def main():
    print('              MENU')
    print('1. Novo contato\n2. Buscar contato pelo nome')
    print('3. Atualizar contato\n4. Apagar contato\n0. Sair')
    op = 1
    while op!=0:
        op = int(input('\nDigite a opção: '))
        if op==1:            
            cadastrar()            
        elif op==2:
            buscar()
        elif op==4:
            deletar()            
        elif op==0:
            print('Programa finalizado.')
            break
        else:
            print('Opção incorreta, tente novamente. ')
main()