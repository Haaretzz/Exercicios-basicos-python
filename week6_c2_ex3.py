def encontra_impares(lista):
	#Define a lista que armazenará os valores impares:
	lista_impares = []
	#Verifica se há elementos na lista:
	if len(lista) > 0:
		#Retira o primeiro elemento da lista:
		numero = lista.pop(0)
		#Verifica se o número é impar:
		if numero % 2 != 0:
			#Se sim, insere o número na lista
			lista_impares.append(numero)
		#Faz a união do resultado atual com o retorno para o resto da lista:
		lista_impares += encontra_impares(lista)
	#Retorna a lista final:
	return lista_impares

print(encontra_impares([1,2,3,4,5]))