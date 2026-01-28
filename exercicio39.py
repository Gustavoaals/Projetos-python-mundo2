# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f"Quem nasceu em {ano_nasc} tem {idade} anos ")

if idade == 18:
    print(f"Você precisa se alistar imediatamente!")
   
elif idade < 18:
    saldo = 18 - idade
    print("Você ainda não possui idade suficiente para se alistar")
    print(f"ainda faltam {saldo} anos para o alistaemnto")
    ano = ano_atual + saldo
    print(f"Seu alistamento sera em {ano} ")

elif idade > 18:
    saldo = idade - 18
    print(f"Ja passou da hora de se alistar, você deviria ter se alistado há {saldo} anos.")
    ano = ano_atual - saldo
    print(f"Seu alistamento foi em {ano}")