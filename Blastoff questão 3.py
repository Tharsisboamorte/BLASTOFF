a = float(input("Insira um valor para A: "))
b = float(input("Insira um valor para B: "))
c = float(input("Insira um valor para C: "))

if a<b<c:
    print("A é o menor número")
elif b<a<c:
    print("B é o menor número")
else:
    print("C é o menor número")