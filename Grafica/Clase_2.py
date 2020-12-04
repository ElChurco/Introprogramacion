Ax = int(input("Ingrese un numero para Ax: "))
Ay = int(input("Ingrese un numero para Ay: "))
Bx = int(input("Ingrese un numero para Bx: "))
By = int(input("Ingrese un numero para By: "))
Cx = int(input("Ingrese un numero para Cx: "))
Cy = int(input("Ingrese un numero para Cy: "))

base = Cx - Ax
altura = By - Ay
import math
hipo = math.sqrt((altura*altura)+(base*base))

perimetro = base + altura + hipo
area = base * altura / 2
print (f"El perimetro es {perimetro}")
print (f"El area es {area}")
