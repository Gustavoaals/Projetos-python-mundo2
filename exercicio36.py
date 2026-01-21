# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

largura = 40

print("=-=".center(largura, "="))
print(f"\033[1;31m{'EMPRESTIMO BANCÁRIO'.center(largura)}\033[m")
print("=-=".center(largura, "="))

casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Sálario do comprador: R$"))
tempo = int(input("Quantos anos de financiamento? "))

prestacao = casa / (tempo * 12)
minimo = salario * 30 / 100

print(f"Para pagar uma casa de {casa} de R${casa:.2f} em {tempo} anos")
print(f"a prestação será de R${prestacao:.2f}")

if prestacao <= minimo:
    print("\033[1;32mEmprestimo pode ser CONCEDIDO!\033[m")
else:
    print("\033[0;41mEmprestimo NEGADO!\033[m")
