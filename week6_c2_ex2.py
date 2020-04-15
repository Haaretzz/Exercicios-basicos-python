def soma_lista(lista):
	#Define a variável que irá armazenar a soma:
	resultado = 0
	#Base da recursão:
	if len(lista) > 0:	
		#Retira o primeiro elemento da lista e soma:
		resultado += lista.pop(0)
		#Soma o resultado atual com o retorno para o resto da lista:
		resultado += soma_lista(lista)
	#Retorna o resultado final:
	return resultado

print(soma_lista([1,2,3]))