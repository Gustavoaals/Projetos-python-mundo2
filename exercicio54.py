#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

totmenor = 0
totmaior = 0
ano_atual = date.today().year

for pessoa in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {pessoa}ª pessoa nasceu? "))
    idade = ano_atual - ano_nascimento

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f"Ao todo tivemos {totmaior} pessoas maiores de idade")
print(f"E também tivemos {totmenor} pessoas menores de idade")
