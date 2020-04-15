def remove_repetidos(lista):
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return sorted(lista2)
lista=[2,4,2,2,3,3,1]
print(remove_repetidos(lista))