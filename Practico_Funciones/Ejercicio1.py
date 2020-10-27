num1 = int(input("Por favor ingrese un numero: "))
num2 = int(input("Por favor ingrese un segundo numero: "))
def numayor(num_1, num_2):
    if num_1 > num_2:
        print(f"El numero mayor es: {num_1}")
    else:
        print(f"El numero mayor es: {num_2}")

numayor(num1, num2)