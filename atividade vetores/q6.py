numeros = [2,-4,6,-7,-8,9]

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = numeros[i] * 0

print(numeros)