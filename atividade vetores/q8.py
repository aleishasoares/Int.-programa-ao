N = int(input("Quantos nomes você deseja cadastrar? "))
nome = [None] * N
for i in range(N):
    nomes = input("Digite o nome:")
    nome[i] = nomes

print (nome)

for i in range (len(nome)):
    print(nome[i], ":", i)