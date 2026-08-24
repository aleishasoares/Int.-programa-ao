import random
numero = random.randint(1, 10)
acertou = False
while not acertou:
    chute = int(input("Chute um número de 1 a 10: "))
    if chute == numero:
        print("Acertou!")
        acertou = True
    else:
        print("Errou, tente de novo")