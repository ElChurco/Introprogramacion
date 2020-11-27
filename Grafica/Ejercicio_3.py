import random
def crearVectorRandom(tam):
    vector=[]
    for i in range(1,tam+1):
        vector.append(random.randint(1,300))
    return vector

tam=int(input("Ingrese el tamaño del vector: "))
vectorNumerosAleatorios=crearVectorRandom(tam)
vectorNumerosEncontrados=[]
print(vectorNumerosAleatorios)
digito=int(input("Ingrese el último dígito a verificar: "))
for pos in range(0,tam):
    valor=vectorNumerosAleatorios[pos]
    residuo=valor%10
    if(residuo==digito):
        vectorNumerosEncontrados.append(valor)
print(vectorNumerosEncontrados)