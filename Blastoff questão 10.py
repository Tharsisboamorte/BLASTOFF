#Criando uma var chamada fatorial para guardar o valor da operação dentro da condicional while
valor = int(input("Entre com um número para saber o fatorial dele: "))  
fatorial = 1
#O fatorial vai acumulando os resultados e a var valor vai diminuindo até chegar perto do 1
while (valor > 1):  
  fatorial = fatorial * valor  
  valor = valor - 1  
print("O fatorial é",fatorial)