def teste_primo (x):
    primo=0
    for i in range(2,x):
        if x % i == 0:
            primo=primo+1
    return primo
def maior_primo (x):
    armazena = 0
    while x>2:
        if teste_primo(x) == 0:
            if x>armazena:
                armazena = x
        x=x-1
    return armazena

x=int(input())
print(maior_primo(x))              