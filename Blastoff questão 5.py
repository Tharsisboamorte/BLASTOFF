x = float(input("número 1: "))
y = float(input("número 2: "))

resto = int((x%y))

if resto == 0:
    print("Os números são multiplos")
else:
    print("Não são multiplos")