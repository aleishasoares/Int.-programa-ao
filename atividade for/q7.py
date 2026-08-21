n =  int(input("Digite quantos números você quer imprimir: "))
soma = 0

for i in range (n):
    num = int(input("Digite um número: "))
    soma = soma + num

print ("A soma dos números é:", soma)