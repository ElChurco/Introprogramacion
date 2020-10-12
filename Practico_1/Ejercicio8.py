n1 = int(input("Por favor ingrese un numero: "))
n2 = int(input("Por favor ingrese un segundo numero: "))
def sumar(listanumeros):
    num = 0
    for a in range(n1 + 1, n2):
        num = num + a
    return num
print(sumar([]))
