numero = str(input("Ingrese un numero: "))
tam = len(numero)
mitad = tam // 2
cont = 0
cont1 = -1
cont2 = 0

while cont < mitad:
    if numero[cont] == numero[cont1]:
        cont += 1
        cont1 -= 1
        cont2 += 1
    else:
        cont += 1
        cont1 -= 1

if cont2 == mitad:
    print(f"{numero} es Capicua")
else:
    print(f"{numero} no es Capicua")