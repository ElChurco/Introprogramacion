num = int(input("Por favor ingrese un numero: "))
suma = 2
res = 0
f = "*"
if num == 0:
    print(0)
else:
    print(1, end=" ")
    while suma <= num:
        res = suma
        var_1 = suma - suma + 1
        print(var_1 * f)
        print(suma, end=" ")
        while res != 1:
            if res % 2 == 0:
                res = int(res / 2)
                var = res - res + 1
                print(var * f, end=" ")
            else:
                res = int((res * 3) + 1)
                var = res - res + 1
                print(var * f, end=" ")
        suma = suma + 1
    print("*")