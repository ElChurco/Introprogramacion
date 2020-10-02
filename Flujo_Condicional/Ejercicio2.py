v1 = int(input("Ingrese un numero: "))
v2 = int(input("Ingrese un segundo numero: "))
if v1 < v2:
    print(f"{v1} es menor que: ")
elif v1 == v2:
    print(f"{v1} es igual {v2}")
else:
    print(f"{v1} es mayor que {v2}")