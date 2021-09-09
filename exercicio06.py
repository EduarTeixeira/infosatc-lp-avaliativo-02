n1 = input("Digite o nome de uma placa de vídeo: ")
n2 = input("Digite o nome de mais uma placa de vídeo: ")
n3 = input("Digite o nome de outra placa de vídeo: ")
lista = [n1, n2, n3]
print(lista)
if "RTX 3080" in lista:
    print("A RTX 3080 está na posição {} na lista".format(lista.index("RTX 3080")))
else:
    print("A placa de vídeo necessária para executar o programa (RTX 3080) não foi digitada")