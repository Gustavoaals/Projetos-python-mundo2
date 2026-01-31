#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento.
print("=-" * 20)
print("SIMULADOR DE LOJA".center(40))
print("=-" * 20)

preco = float(input("Preço das compras R$: "))

print("""
FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque (10% desconto)
[ 2 ] À vista cartão (5% desconto)
[ 3 ] 2x no cartão (sem juros)
[ 4 ] 3x ou mais no cartão (20% juros)
""")

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco * 0.90
    print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")

elif opcao == 2:
    total = preco * 0.95
    print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")

elif opcao == 3:
    parcela = preco / 2
    print(f"Sua compra de R${preco:.2f} ficou 2x de R${parcela:.2f}.")

elif opcao == 4:
    vezes = int(input("Em quantas vezes você vai pagar? "))
    if vezes < 3:
        print("Número de parcelas inválido.")
    else:
        total = preco * 1.20
        parcela = total / vezes
        print(f"Sua compra ficou em R${total:.2f} COM JUROS e parcelada em {vezes}x ficou R${parcela:.2f}.")

else:
    print("Opção inválida.")
