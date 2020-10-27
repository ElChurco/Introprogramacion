p1 = str(input("Por favor ingrese una palabra: "))
def inversion(pal):
    tam_palabra = len(pal)
    while tam_palabra != 0:
        tam_palabra -= 1
        print(pal[tam_palabra], end="")
inversion(p1)