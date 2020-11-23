vector1 = [0]*5
vector2 = [0]*5
vector3 = [0]*5
for i in range(10):
    if i < 5:
        print("Ingrese el valor del vector 1: ")

        vector1[i] = int(input())

    else:
        print("Ingrese el valor del vector 2: ")
        vector2[i-5] = int(input())

    for j in range(0,5):
        vector3[j] = vector1[j] + vector2[j]

print(vector3)
