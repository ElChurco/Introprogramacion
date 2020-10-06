m = float(input("Ingrese la cantidad de agua: " ))
mensaje = "Tu deuda a pagar es: "
if m <= 100:
    print(mensaje, m * 1.00, "Bolivianos")
elif 100 < m <= 499:
    print(mensaje, m * 1.20, "Bolivianos")
elif 500 <= m <= 999:
    print(mensaje, m * 1.50, "Bolivianos")
elif m >= 1000:
    print(mensaje, m * 2.00, "Bolivianos")

