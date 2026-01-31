#A Confederação Nacional de Natação precisa de um programa que leia
#o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:

from datetime import date

ano_nasc = int(input("Ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print (f"Você nasceu em {ano_nasc} e tem {idade} anos ")

if 0 > idade >= 9:
    print("Você está na categoria de: MIRIM.")
elif idade < 14:
    print("Você está na categoria: INFANTIL.")
elif 14 > idade < 19: # ERRADO 22 
    print("Você está na categoria JÚNIOR")
elif 19 > idade <= 25:
    print("Você está na categoria SÊNIOR")
else :
    print("Você está na cateforia de MASTER")
#7 > media >= 5 