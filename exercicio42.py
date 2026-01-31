#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
#mostrar que tipo de triângulo será formado:

import time 
print('-=' * 20)
print("ANALISADOR DE TRINÂNGULO".center(40))
print('-=' * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

time.sleep(2)
print("ANALISANDO...")
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")

    if r1 == r2 == r3:
        print("Triângulo EQUILÁTERO: todos os lados iguais.")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("Triângulo ISÓSCELES: dois lados iguais, um diferente.")
    else:
        print("Triângulo ESCALENO: todos os lados diferentes.")
else:
    print("Os segmentos NÃO podem formar um triângulo.")
