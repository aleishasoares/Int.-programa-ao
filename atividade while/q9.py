numero = int(input("Digite um número: "))
primo = True 
divisor = 2

if divisor<2:
    print ("O número não é primo")
else:
    while divisor < numero:
           if numero % divisor == 0:
                primo = False
    divisor = divisor + 1

if primo == True:
    print ("O número é primo")  
else:
     print ("O número não é primo")