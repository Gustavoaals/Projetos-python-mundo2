# GAME: Pedra Papel e Tesoura
import time
from random import randint

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA     
''')

jogador = int(input("Qual a sua jogada?: "))

print("Pedra..")
time.sleep(1)
print("Papel..")
time.sleep(1)
print("Tesouraa!")
time.sleep(1)

itens = ["Pedra", "Papel", "Tesoura"]
computador = randint(0, 2)

print("-=" * 11)

# validação para evitar erro
if jogador < 0 or jogador > 2:
    print("JOGADA INVÁLIDA!")
else:
    print(f'''
O computador jogou {itens[computador]}
Jogador jogou {itens[jogador]}
''')
    print("-=" * 11)

    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("JOGADOR VENCE!")
        elif jogador == 2:
            print("COMPUTADOR VENCE")

    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print("COMPUTADOR VENCE")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("JOGADOR VENCE!")

    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print("JOGADOR VENCE!")
        elif jogador == 1:
            print("COMPUTADOR VENCE")
        elif jogador == 2:
            print("EMPATE")
