print('=-' * 15)
print("TABUADA".center(30))
print('=-' * 15)

print('''\nQual operação Matematica desejada?\n
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão\n ''')

num = int(input("Digite um número: "))
tabu = int(input("Tabuada: "))

for n in range(0,11):
    if num == 1:
        print(f"{tabu} + {n} = {tabu + n} ") 