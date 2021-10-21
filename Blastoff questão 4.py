#Conversão de Celsius para farenheit
c = float(input("Quantos graus em Celsius (°C) você gostaria de converter?\n"))
f = float( c*1.8+32)
#Aqui consegui arredondar o número para apenas duas casas decimais
print ("Farenheit =",round(f,2),"°F")