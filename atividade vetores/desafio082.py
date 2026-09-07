n = int(input("Quantos números você deseja cadastar? "))
lista = [None] * n
pares = []
impares = []

for c in range(n):
    lista[c] = int(input("Digite um número: "))

print("A lista inteira é:", lista)

for c in range(n):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])

print("A lista de números pares é:", pares)
print("A lista de números ímpares é:", impares)