#números primos
#Criei uma var chamada mult para ser uma armazenadora de múltiplos
n = int(input("Por favor insira um número inteiro e positivo para verificarmos se este é um número primo: "))
mult=0

#Condições para ser um número primo: O resto tem que ser diferente de zero e quociente deve ser menor que o divisor
for count in range(2,n):
    if (n % count == 0):
        mult += 1
#Aqui checamos mais uma condição para número primo
if(mult==0):
    print("O número",n,"é primo")
else:
    print("O número",n,"não é primo")