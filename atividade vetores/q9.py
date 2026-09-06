numeros = [1, 2, 2, 5]

ordenado = True

for i in range(1, len(numeros)):
    if numeros[i] < numeros[i-1]:
        ordenado = False
        break

if ordenado:
    print("SIM")
else:
    print("NAO")