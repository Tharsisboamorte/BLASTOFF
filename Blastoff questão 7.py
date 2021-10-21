print("Temos uma lista pronta com números pares e impares, todos randomizados, e este programa vai te informar de todos os números pares")
#importando números randômicos e criando uma lista de dez posições com eles
import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,1000)
    randomlist.append(n)
print("Esta é a lista em sua totalidade: ", randomlist)
pares = []
#Criando uma condição para saber quais números são pares e depois os adicionando a lista pares
for i in randomlist:
    if i % 2 == 0:
        pares.append(i)
print("Estes sãos números pares da lista: ", pares)


