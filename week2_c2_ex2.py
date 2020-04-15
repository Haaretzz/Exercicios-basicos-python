def menor_nome(nomes):
	stripped_nomes = list(map(str.strip, nomes))
	aux = " "
	aux = stripped_nomes[0]
	for i in range(len(stripped_nomes)):
		if len(stripped_nomes[i]) < len(aux):
			aux = stripped_nomes[i]
	return aux.capitalize()