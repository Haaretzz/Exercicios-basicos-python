n=int(input("Digite o valor de n: "))
cont=1
if n == 0:
    n=1
    print(n)
while n > 0:
    cont=cont*n
    n=n-1
print(cont)
