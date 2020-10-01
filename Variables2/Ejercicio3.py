import math
radio = int(input("Ingrese el numero del radio de un circulo: "))
area = math.pi * radio**2
perimetro= 2* math.pi * radio
mensaje = f"El area del circulo es {area}. El perimetro del circulo es: {perimetro}"
print(mensaje)