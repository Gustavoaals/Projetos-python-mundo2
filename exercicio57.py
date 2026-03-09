# enquanto o contador for menor 11 ele vai contando até chegar em 11(10).
'''c = 1
while c < 11: # enquanto o contador for menor 11 ele vai contando até chegar em 11(10).
    print(f"{c}",end=" ")
    c += 1
print('\nFim!')
'''
# For eu ultilizo quando desejo um limite.
'''
for c in range(1,6): 
    n = int (input("Digite um valor: "))
print('FIm!')'''

#Vai ficar lendo varios ate a pessoa digitar N, ai para
'''r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar [S/N] ")).upper()
print('Fim.')'''

#Ao digitar 0 ele para de perguntas os números.
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares!")
