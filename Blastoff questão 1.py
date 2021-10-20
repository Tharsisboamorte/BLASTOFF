#Inicio do código pedindo ao usuário para inserir a idade de cada var.
print ("Olá, esse programa é feito para calcular a média da idade de cinco pessoas. Por favor informe as idades de acordo com cada letra")

#Cada variavél vai ser um inteiro
i = int(input("Qual a idade da pessoa i: "))
j = int(input("Qual a idade da pessoa j: "))
k = int(input("Qual a idade da pessoa k: "))
x = int(input("Qual a idade da pessoa x: "))
y = int(input("Qual a idade da pessoa y: "))

#Aqui eu faço o calculo da média e converto o valor para um decimal.
media = float((i+j+k+x+y)/5)

#Apresentando o valor da média.
print("A média das idades é: ", media)