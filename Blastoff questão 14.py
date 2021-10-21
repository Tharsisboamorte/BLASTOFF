palavra = input("Insira uma palavra para descobrir se ela é um palindormo")
# Utilizando da função reversed no python para inverter a sequência de caracteres da palavra e comparar com a palavra original.
if str(palavra) == "".join(reversed(palavra)) :
    print("Palíndromo")
else:
    print("Não é um palíndromo")