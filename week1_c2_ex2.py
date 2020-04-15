def soma_matrizes(m1,m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False
    else:
        matriz = []   
        for i in range(len(m1)):
            linhas = []
            for j in range(len(m1[0])):
                linhas.append(m1[i][j] + m2[i][j])
            matriz.append(linhas)
        return matriz   