def maiusculas(frase):
	strAUX = "" 
	for i in frase:
		if ord(i) >= 65 and ord(i) <= 90:
			strAUX += i
	return strAUX