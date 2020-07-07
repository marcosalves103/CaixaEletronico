
#Interar sobre um arquivo
arquivo = open('arquivo.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()


#Ler todas as linhas em uma única string
arquivo = open('arquivo.txt', 'r')
unica_sting = arquivo.read()
print(unica_sting)
arquivo.close()

#Ler todas as linhas em uma lista
arquivo = open('arquivo.txt', 'r')
lista = arquivo.readlines() #readlines
print(lista)
arquivo.close()

#Ler linha a linha do arquivo
arquivo = open("arquivo.txt", 'r')
primeira_linha = arquivo.readline()
segunda_linha = arquivo.readline()
terceira_linha = arquivo.readline()
print(segunda_linha)
arquivo.close()

#Criando um arquivo vazio
arquivo = open('novo-arquivo.txt', 'w')
arquivo.close()

#Apagar o conteúdo de um arquivo
arquivo = open('novo-arquivo.txt', 'w')
arquivo.close()

#Escrever em um arquivo
arquivo = open('novo-arquivo.txt', 'w') # Vai sobrescrever o arquivo anterior
arquivo.write('nova linha')
arquivo.close()

#Inserir conteúdo ao já existente
arquivo = open('novo-arquivo.txt', 'r') # Abra o arquivo (Leitura)
conteudo = arquivo.readlines()
conteudo.append('Nova linha') #insira seu conteúdo
arquivo = open('novo-arquivo.txt', 'w') # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)
arquivo.close()
