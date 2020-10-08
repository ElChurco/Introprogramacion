v1 = int(input("Ingrese un numero: "))
v2 = int(input("Ingrese un segundo numero: "))
cos = v1 // v2
res = 1 % 2
if res == 0:
    print("La division es exacta: ")
else:
    print("La division No es exacta: ")
print(f"Cociente: {cos}")
print(f"Resto: {res}")