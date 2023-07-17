import random

def criar_matriz():
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

def preencher_matriz(matriz, vetor):
    for i in range(3):
        for j in range(3):
            choice = random.choice(vetor)
            matriz[i][j] = choice
            vetor.remove(choice)

def quadrado_magico(matriz):
    linha1 = matriz[0][0] + matriz[0][1] + matriz[0][2]
    linha2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
    linha3 = matriz[2][0] + matriz[2][1] + matriz[2][2]
    coluna1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
    coluna2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
    coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
    diagonal1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diagonal2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
    return (linha1 == linha2 == linha3 == coluna1 == coluna2 == coluna3 == diagonal1 == diagonal2)

boolean = False

while not boolean:
    matriz = criar_matriz()
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    preencher_matriz(matriz, vetor)
    boolean = quadrado_magico(matriz)
    print("\n", matriz[0], "\n", matriz[1], "\n", matriz[2])
