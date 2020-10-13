from datetime import date
dia = int(input("Por favor ingrese la fecha de su nacimiento: "))
mes = int(input("Por favor ingrese el mes: "))
anno = int(input("Por favor ingrese el año: "))
fecha_de_nacimiento = date(anno, mes, dia)
hoy = date.today()
op = (hoy.year - fecha_de_nacimiento.year)
op1 = (hoy.day - fecha_de_nacimiento.day)
op2 = (hoy.month - fecha_de_nacimiento.month)
if op2 <= 0:
    if op1 >= 0:
        print(f"Usted tiene {op} annos ")
    else:
        print(f"Usted tiene {op - 1} annos")
else:
    print(f"Usted tiene {op} años")

