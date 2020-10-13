num = int(input(" Por favor ingrese la cantidad de palabras: "))
sum = 0
v1 = 0
v2 = 1000
while sum < num:
    sum += 1
    p1 = input(f"Palabra {sum}: ")
    if len(p1) > v1:
        v1 = len(p1)
        p1_max = p1
    if len(p1) < v2:
        v2 = len(p1)
        p1_min = p1
print(f"{p1_max} es la palabra mas larga")
print(f"{p1_min} es la palabra mas corta")
print("Gracias!")
