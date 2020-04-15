x=int(input("digite a largura:  "))
y=int(input("digite a altura: "))

while y>0:
    aux=0
    while aux < x:
        print("#", end="")
        aux=aux+1
    print()
    y=y-1