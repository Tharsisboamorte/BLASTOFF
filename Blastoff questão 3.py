#aqui abri variavéis e coloque a possibilidade de ser um float para abranger números decimais também
a = float(input("Insira um valor para A: "))
b = float(input("Insira um valor para B: "))
c = float(input("Insira um valor para C: "))
#Da sexta linha pra baixo eu fiz uma condicional que compara se a é menor que os outros dois e dps se b é menor que os outros dois, caso nenhum dos casos seja concretizado, c vai ser o menor dentre todos.
if a<b<c:
    print("A é o menor número")
elif b<a<c:
    print("B é o menor número")
else:
    print("C é o menor número")