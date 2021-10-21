#Nas 13 primeiras linhas eu utilizo da conversão de horas para segundos e de minutos para segundos para fazer o calulor da diferença posteriormente na linha 16
print("Esse programa vai calcular quanto tempo durou a partida de futebol que você participou/assistiu")
print("Digite as horas inicias:")
h1 = int(input())
horaseg1 = h1*3600
print("Digite os minutos inicias:")
m1 = int(input())
minseg1 = m1*60
print("Digite as horas finais:")
h2 = int(input())
horaseg2 = h2*3600
print("Digite os minutos finais:")
m2 = int(input())
minseg2 = m2*60

segundos = (horaseg2+minseg2)-(horaseg1+minseg1)

#Nessas últimas linhas eu utilizo do resultado da diferença dos dois horários e converto cada um para seu estado original de medida
h = int(segundos / 3600)
resto = segundos % 3600
m = int(resto / 60)

print("Foram",h,"horas e", m,"minutos de partida de futebol")