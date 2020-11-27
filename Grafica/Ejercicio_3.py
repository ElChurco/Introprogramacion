import random

num = int(input("Ingrese el tamaño de su Lista: "))
contador = 1
vector2 = []
vector3 = []

while contador <= num:
    v1 = random.randint(1,300)
    a = str(v1)
    if a[-1] == str(5):
        vector3.append(v1)
    vector2.append(v1)
    contador = contador + 1


print("")
print(f"La lista aleatoria de {num} es: \n{vector2}")
print("")
print(f"Numeros a lazar terminados en 5: \n{vector3}")