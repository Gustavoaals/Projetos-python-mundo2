largura = 40

print("=-=".center(largura, "="))
print(f"\033[1;31m{'EMPRESTIMO BANCÁRIO'.center(largura)}\033[m")
print("=-=".center(largura, "="))

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Sálario do comprador: R$"))
tempo = int(input("Quantos anos de financiamento? "))