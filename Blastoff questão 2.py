
print("Este programa vai calcular o consumo médio de gasolina de um automóvel.")

#Mudando o input para abranger números float
distancia = float(input("Insira a distância percorrida pelo veículo: "))
combustivel = float(input("Insira a quantidade de combustível gasto pelo veículo: "))

#Realizando o calculo de gasto médio    
gastoMedio = float(distancia/combustivel)

#Aqui o programa imprimi o resultado do calculo
print("Resultado:", gastoMedio)