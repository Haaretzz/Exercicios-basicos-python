def incomodam(n):
	if n <= 0:
		return ''
	else:
		return incomodam(n-1) + 'incomodam ' 

def elefantes(n):
	if n <= 0:
		return '' 
	elif n == 1:
		return "Um elefante incomoda muita gente\n"
	else:
		return elefantes(n-1) + str(n) + ' Elefantes ' + incomodam(n) + 'muito mais\n' + str(n) + ' Elefantes incomodam muita gente\n'

print(elefantes(3))