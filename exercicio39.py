# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f"Quem nasceu em {ano_nasc} tem {idade} anos ")