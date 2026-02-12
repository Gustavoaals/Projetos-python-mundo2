#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços. Exemplos de palíndromos:

frase = input("Digite uma frase: ").lower()
frase = frase.replace(" ", "")

inverso = frase[::-1]

print(f"O inverso de {frase} é {inverso}")

if frase == inverso:
    print("Temos um palíndromo")
else:
    print("A frase digitada não é um palíndromo")