num_ter = int(input("n: "))
suma = 0
for i in range(1, num_ter + 1):
    if i % 2 == 0:
        signo = -1
    else:
        signo = 1
    valor_termino_actual = signo / (1 + 2 *(i - 1))
    suma += valor_termino_actual
pi = 4 * suma
print(pi)
