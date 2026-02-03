numeros =  [ 5, 6 , 8, 5, 8, 9, 1, 2, 4] #lista de numero
for num in numeros:
    if num % 2 != 0: # checando se o numero é impar
        continue # se for impar ele vai continuar para outra linha e so vai exibir numero par
    print(f"O número {num} é PAR")

contador = 0 
while contador <= 8: # enquanto estiver menor que 8 ele vai reliazar o loop
    print(f"O contador esta no valor {contador} ")
    contador += 1