n = int(input("quantos números você deseja cadastar? "))
lista = [None] * n

for i in range(n):
    lista[i] = int(input("Digite um número: "))

print("A lista inteira é:", lista)
print("Você digitou", len(lista), "elementos.")
print("A lista em ordem crescente é:", sorted(lista))

if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")