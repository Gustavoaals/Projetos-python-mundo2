#A Confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:

from datetime import date

ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print (f"Você nasceu em {ano_nasc} e tem {idade} anos ")

if idade < 9: # entre 1 ano a 9 anos 
    print("Você está na categoria de: MIRIM.")
elif idade < 14: # entre 9 anos e 14 anos
    print("Você está na categoria: INFANTIL.")
elif idade < 19: # entre 14 anos e 19 anos
    print("Você está na categoria JÚNIOR")
elif idade < 25: # entre 14 anos e 25 anos
    print("Você está na categoria SÊNIOR")
else: # Acima de 25 anos
    print("Você está na categoria de MASTER")
