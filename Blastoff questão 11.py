#Intereseção de listas
#As duas listas já dadas pela questão. Foi realizado a criação de uma var que iria abarcar essas duas listas, e foi criado um função de intersecção já presente em python
a = [1,2,3,4]
b = [1,2,5,8]

print("Vamos intereseccionar duas listas. A lista a:",a,"e a lista b:",b,)
c = set(b).intersection(set(a))

print("Está é a intersecção das duas listas presentes no código:\n",c)