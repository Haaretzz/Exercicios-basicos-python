n=int(input("Digite um número inteiro: "))
cont=0
while n > 0:
    cont=cont+n%10
    n=n//10
print(cont)    