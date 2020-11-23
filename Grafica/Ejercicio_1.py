FACT = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  ### [0]*20

def FACT_NUMERO(n):
    aux = 1
    for i in range(n):
        factorial = (i+1) * aux
        aux = factorial
    return factorial

for i in range(1,21):
    FACT[i-1] = FACT_NUMERO(i)

print(FACT)
