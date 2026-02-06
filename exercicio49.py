#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
#só que agora utilizando um laço for

num = int(input("Digite um número: "))

for tabu in range(1,11):
    print(f"{num} x {tabu} = {num * tabu}")