num1 = int(input("Por favor ingrese un numero: "))
num2 = int(input("Por favor ingrese un segundo numero: "))
num3 = int(input("Por favor ingrese un ultimo numero: "))
def tres_max(num_1, num_2, num_3):
    num_mayor = 0
    if num_1 > num_mayor:
        num_mayor = num_1
    if num_2 > num_mayor:
        num_mayor = num_2
    if num_3 > num_mayor:
        num_mayor = num_3
    print(f"El mayor es: {num_mayor}")

tres_max(num1, num2, num3)