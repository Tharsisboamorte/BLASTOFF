#Criei uma lista com duas posições para ser uma matriz 2x2, depois criei um range para a linha e outro para coluna, coloquei para o usuário digitar um valor e depois imprimi os valores de usa matriz
print("Esse programa vai te ajudar a criar uma matriz 2x2")
matriz = [[0,0],[0,0]]
for l in range(0,2):
    for c in range(0,2):
        matriz[l][c] = int(input("Por favor digite um valor para cada posição da matriz 2x2: "))
print(matriz)