#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep
from random import randint
print('-=-' * 15)
print("JOGO DE ADVINHAÇÃO".center(45))
print('-=-' * 15)

num = int(input("Digite um número entre 0 e 5: "))
maquina = randint(0,5)

print ("PROCESSANDO...")
sleep(3)
if num == maquina:
    print(f"PARABÉNS!!, o seu numero {num} é igual ao da maquina {maquina}")
else:
    print(f"Que pena você perdeu, o numero da maquina foi {maquina}, e o seu {num} a maquina venceu")
