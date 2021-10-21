print("Digite uma quantidade de hora: ")
h1 = int(input())
horaseg1 = h1*3600
m1 = int(input())
minseg1 = m1*60
h2 = int(input())
horaseg2 = h2*3600
m2 = int(input())
minseg2 = m2*60

segundos = (horaseg2+minseg2)-(horaseg1+minseg1)


h = int(segundos / 3600)
resto = segundos % 3600
m = int(resto / 60)

print(h, m)