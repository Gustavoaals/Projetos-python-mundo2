#Jogo da Adivinhação v2.0

from random import randint
maquina = randint(0,10) 
print('''
Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite ? "))
    palpites += 1
    if jogador == maquina:
        acertou = True
    else:
        if jogador < maquina:
            print("Mais... Tente mais uma vez.")
        elif jogador > maquina:
            print("Menos... Tente mais uma vez")
print(f"Acertou com {palpites} tentativas, Parabéns!")
