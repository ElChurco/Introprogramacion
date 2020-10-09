n1 = int(input("Por favor ingrese un numero: "))
n2 = int(input("Por favor ingrese un segundo numero: "))
n3 = int(input("Por favor ingrese un ultimo numero: "))
min = min(n1, n2, n3)
max = max(n1, n2, n3)
mid = (n1 + n2 + n3) - min - max
print(min, mid, max)

