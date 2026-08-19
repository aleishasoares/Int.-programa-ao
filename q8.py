continuar = "S"

while continuar == "S":
    n1 = float(input("Digite a primeira nota:"))

    while n1 < 0 or n1 > 10:
        print ("Nota invalida, digite um número entre 0 e 10")
        n1 = float(input("Digite a primeira nota: "))
    n2 = float(input(" Digite a segunda nota: "))

    while n2 < 0 or n2 > 10:
        print ("Nota invalida, digite um número entre 0 e 10")
        n2 = float(input("Digite a segunda nota: "))

    media = (n1+n2)/2
    print ("A média aritmética das notas é:", media)

    continuar = input("Deseja calcular a média de outro aluno? (S/N)").upper()
    while continuar!= "S" and continuar != "N":
        print (" Opçao invalida, digite S ou N!")
        continuar = input("NOVO CALCULO S/N: ")