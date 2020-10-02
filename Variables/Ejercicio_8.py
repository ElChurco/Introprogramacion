monto_invertir = float(input("Ingrese el monto a invertir: "))
interes = float(input("Ingrese el interes anual: "))
años = float(input("Ingrese el numero de años a invertir: "))
o1 = monto_invertir + int(1)
o2 = float(o1) ** años
o3 = float(o2) * monto_invertir
print(f"El interes compuesto es {round(o3, 2)}")

