# Escreva um programa que leia dois números inteiros e compare-os.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print("O primeiro valor é MAIOR")
elif b > a:
    print("O segundo valor é MAIOR")
else:
    print("Não existe número maior, os dois são iguais")