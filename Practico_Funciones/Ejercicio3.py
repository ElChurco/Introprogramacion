p1 = input("Ingrese una palabra: ")
def long_palabra(palabra):
    numero = 0
    for a in palabra:
        numero += 1
    print(numero)
long_palabra(p1)