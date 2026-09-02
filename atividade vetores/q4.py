numeros = [1,4,5,7,8,10]
contador = 0
pares = 0

while contador<6:
    if numeros[contador] % 2 == 0:
        pares += 1
    contador += 1

print ("O número de elementos pares é:", pares)