num = int(input("Por favor ingrese un numero: "))
for i in range(1, num + 1):
    res = num % i
    if res == 0:
        print(i)




