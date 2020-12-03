bas = int(input("Ingrese la base de su figura: "))
alt = int(input("Ingrese la altura de su figura: "))
num = 1
lM = 0
lm = 0
if bas > alt:
    lM = bas
    lm = alt
else:
    lM = alt
    lm = bas
no_entran = []
si_entran = []
while num != 0:
    radio = int(input("Ingrese un radio: "))
    num = radio
    if num == 0:
        num = 0
    diametro = 2 * radio
    if diametro <= lm:
        lm = lm - diametro
        lM = lM - diametro
        si_entran.append(radio)
    else:
        lm = lm
        no_entran.append(radio)
print(f"{si_entran} Pueden entrar en la figura")
print(f"{no_entran} No pueden entrar en la fifura")