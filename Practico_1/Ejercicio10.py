t1 = int(input("Ingrese el tiempo del primer tramo: "))
t2 = int(input("Ingrese el timpo del segundo tramo: "))
res = t1 + t2
sum = 0
while res > 0:
    sum = res + sum
    t1 = t1 + 1
    res = int(input("Duracion del ultimo tramo: "))
op = sum // 60
op1 = sum % 60
if op1 < 10:
    print(f"{op}:{op1} Horas ")
else:
    print(f"{op}:{op1} Horas ")