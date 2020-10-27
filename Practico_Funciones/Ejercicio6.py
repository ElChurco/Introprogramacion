pal = str(input("Ingrese una palabra: "))

def palindromo(pal):
    division = len(pal) // 2
    resta = len(pal) - 1
    contador = 0
    contador_1 = 1
    while contador != division:
        if str(pal[contador]) == str(pal[resta]):
            contador_1 = contador + 1
        contador += 1
        resta -= 1
    if contador_1 * 2 == len(pal) or (contador * 2) + 1 == len(pal):
        print(True)
        print("Es un Palindromo")
    else:
        print(False)
        print("No es un Palindromo")
palindromo(pal)