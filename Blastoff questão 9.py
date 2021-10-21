#Na primeira linha de código eu transformo o input em um número inteiro ao invés de manter como str
#Variavél vez é o número fixo das opoerações que aumenta gradualmente com o while. Tive que reiniciar o vez toda vez que criava uma tabuada nova
num = int(input("Insira um número para ter as tabuadas de todas as quatro operações básicas: "))
vez = 1
print("Esta é a tabuada da multiplicação:")
while vez <= 10:
    print( num, "x", vez, "=", num*vez)
    vez = vez + 1
vez = 1
print("Esta é a tabuada da soma:")
while vez <= 10:
    print( num, "+", vez, "=", num+vez)
    vez = vez + 1
vez = 1
print("Esta é a tabuada da subtração:")
while vez <= 10:
    print( num, "-", vez, "=", num-vez)
    vez = vez + 1
vez = 1
#Infelizmente não consegui eliminar os números após a vírgula da tabuada de divisão
print("E esta é a tabuada da divisão:")
while vez <= 10:
    print (num, "/", vez, "=", num/vez)
    vez = vez + 1