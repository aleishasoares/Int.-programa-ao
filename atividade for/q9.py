n = int(input("Digite um número inteiro: "))

primo = True
if n < 2:
    primo = False
else:
    i = 2
    while i < n:
        if n % i == 0:
            primo = False
        i += 1

if primo:
    print(f"{n} é primo")
else:
    print(f"{n} não é primo")