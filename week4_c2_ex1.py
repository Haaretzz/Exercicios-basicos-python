def ordenada(lista):
	lista2 = lista[0:]
	for i in range (len(lista2)-1):
		menor = i
		for j in range(i+1, len(lista2)-1):
			if lista2[j] < lista2[menor]:
				menor = lista2[j]
		lista2[i], lista2[menor] = lista2[menor], lista2[i]
	if lista2 == lista:
		return True
	else:
		return False	
		
