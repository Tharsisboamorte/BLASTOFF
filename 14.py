palavra = input("Insira uma palavra para descobrir se ela é um palindormo")
if str(palavra) == "".join(reversed(palavra)) :
    print("Palíndromo")
else:
    print("Não é um palíndromo")