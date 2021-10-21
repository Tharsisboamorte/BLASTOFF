print("Este programa pretente te ajudar a decobrir se dois números apresentados por você são múltiplos ou não")
x = float(input("Insira aqui o valor do primeiro número: "))
y = float(input("Insira aqui o valor do segundo número: "))

# A variavél resto serve para calcular o resto da divisão entre os dois números
resto = int((x%y))

#Por via de regra se o resto da divisão entre dois números não é igual a zero eles não são múltiplos um do outro
if resto == 0:
    print("Os números são múltiplos")
else:
    print("Não são múltiplos")