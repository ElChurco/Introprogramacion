estat = float( input ("Ingrese su estatura: "))
pes = float( input ("Ingrese su peso: "))
edad = float( input ("Ingrese su edad: "))
IMC = float( pes  /  estat  **  2 )
if  edad < 45:
    if IMC < 22.0:
        print("Riesgo de enfermedad coronaria baja")
    elif IMC >= 22.0:
        print("Riesgo de  enfermedad coronaria media")
elif  edad >= 45:
    if IMC < 22.0:
        print("Riesgo de enfermedad coronaria media")
    elif  IMC >= 22.0:
        print("Riesgo de enfermedad coronaria alta")
