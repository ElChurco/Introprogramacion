p1 = str(input("Por favor ingrese un caracter: "))
def letra(vocal):
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print(True)
        print("Es una vocal")
    else:
        print(False)
        print("No es una vocal")
letra(p1)