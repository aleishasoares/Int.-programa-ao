expressao = input("Digite uma expressão: ")

contador = 0
correta = True

for caractere in expressao:
    if caractere == "(":
        contador += 1
    elif caractere == ")":
        contador -= 1
    
    if contador < 0:
        correta = False
        break

if contador != 0:
    correta = False

if correta:
    print("Parênteses corretos")
else:
    print("Parênteses incorretos")