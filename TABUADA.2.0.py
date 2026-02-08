print('=-' * 15)
print("TABUADA".center(30))
print('=-' * 15)

tabu = int(input("TABUADA: "))

print("""
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
""")

num = int(input("NÚMERO: "))

if num < 1 or num > 4:
    print("Número inválido.")
else:
    for n in range(1, 11):
        if num == 1:
            print(f"{tabu} + {n} = {tabu + n}")
        elif num == 2:
            print(f"{tabu} - {n} = {tabu - n}")
        elif num == 3:
            print(f"{tabu} x {n} = {tabu * n}")
        elif num == 4:
            print(f"{tabu * n} ÷ {tabu} = {(tabu * n) / tabu}")
