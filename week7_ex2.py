x=int(input("digite a largura:  "))
y=int(input("digite a altura: "))
aux2=y
while y>0:
    aux=0
    while aux < x:
        if y == aux2 or y==1:
            print("#", end="")
        elif aux != 0 and aux != x-1:
            print(" ", end="")
        else:
            print("#", end="")
        aux=aux+1
    print()
    y=y-1