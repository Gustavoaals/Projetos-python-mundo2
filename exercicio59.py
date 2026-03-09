from time import sleep
menu = 0
while menu != 5:
    num = int(input("Primeiro valor: "))
    num2 = int(input("Segundo valor: "))
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    menu = int(input("Digite a operção desejada: "))
    if menu == 1:
        print(f"A soma entre os números {num} e {num2} é {num+num2} ")
    elif menu == 2:
        print(f"A multiplicação entre {num} e {num2} é de {num*num2}")
    elif menu == 3:
        if num > num2:
            maior = num
            print(f"Entre {num} e {num2} o maior valor é {maior}")
        elif num2 > num2:
            maior = num2
            print(f"Entre {num} e {num2} o maior valor é {maior}")
        else:
            print("Ambos números iguais")
    elif menu == 4:
        print("Informe os números novamente.")
        num = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif menu == 5:
        print("Finalizando...")
    else:
        print("Opção inválida, tente novamente.")
    print('=-=' * 10)
    sleep(1.5)
print("Fim")