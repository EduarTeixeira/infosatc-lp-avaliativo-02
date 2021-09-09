#Exercício a
n1Filmes = input("Digite o nome de um filme que você gosta: ")
n2Filmes = input("Digite o nome de outro filme que você gosta: ")
n1Jogos = input("Digite o nome de um jogo que você gosta: ")
n2Jogos = input("Digite o nome de outro jogo que você gosta: ")
n1Livros = input("Digite o nome de um livro que você gosta: ")
n2Livros = input("Digite o nome de outro livro que você gosta: ")
n1Esportes = input("Digite o nome de um esporte que você gosta: ")
n2Esportes = input("Digite o nome de outro esporte que você gosta: ")
lista_filmes = [n1Filmes, n2Filmes]
lista_jogos = [n1Jogos, n2Jogos]
lista_livros = [n1Livros, n2Livros]
lista_esportes = [n1Esportes, n2Esportes]
print("Lista de Filmes: {}".format(lista_filmes))
print("Lista de Jogos: {}".format(lista_jogos))
print("Lista de Livros: {}".format(lista_livros))
print("Lista de Esportes: {}".format(lista_esportes))

#Exercício b
lista_geral = [lista_filmes, lista_jogos, lista_livros, lista_esportes]
print("Lista geral com todas as outras listas: {}".format(lista_geral))

#Exercício c
print("Segundo item da lista livros: {}".format(lista_livros[1]))

#Exercício d
del lista_esportes[0]
print("Lista esportes sem o item da primeira posição: {}".format(lista_esportes))

#Exercício e
lista_geral.append(disciplinas[])