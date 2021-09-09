lista_computador = ["RTX 2080Ti", "Gabinete Cooler Master", "i5 7400", "Memória RAM 8gb", "Fonte 500W"]
print("Lista de itens para montar o computador: {}".format(lista_computador))
lista_computador.remove("RTX 2080Ti")
lista_computador.remove("Gabinete Cooler Master")
print("Como a RTX 2080Ti e o Gabinete Cooler Master estavam caros removi-os da lista e ficou assim: {}".format(lista_computador))
lista_computador.insert(0, "RTX 2060")
lista_computador.insert(1, "Gabinete genérico")
print("A lista com itens atualizados e mais baratos ficou assim: {}".format(lista_computador))