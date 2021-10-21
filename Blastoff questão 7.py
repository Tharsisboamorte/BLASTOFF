# numero = input("Insira os números que desejar separados pela barra de espaço: "
# )
# numeros = numero.split()
# pares = []
# for i in range(len(numeros)):
#     numeros[i] = int(numeros[i])

# if (numeros[i] % 2 == 0):
#     pares.append()
# for par in pares:
#     print("Estes sãos números pares da lista: ", pares)

lista1 = []
lista2 = []
for i in range(len(lista1)):
    lista1[i] = int(lista1[i])
for valor in lista1:
    if valor % 2 == 0:
        lista2.append(valor)

print(lista2)