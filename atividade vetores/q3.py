numeros = [1,2,3,4]

maior = numeros[0]
menor = numeros[0]

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]

print("O maior número é:", maior)
print ("O menor número é:", menor)