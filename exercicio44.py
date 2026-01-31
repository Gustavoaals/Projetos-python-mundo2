#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento.

compras = float(input("Preços das compras R$: "))

print('''
FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input("Qual é a opção? "))
avista10 = (compras * 10) / 100
avista5 = (compras * 5) / 100
parcelado = (compras * 20) / 100 
compras = parcelado + compras

if opcao == 1:
    print(f"Sua compra de R${compras:.2f} vai custar R${compras - avista10:.2f} no final.")
elif opcao == 2:
    print(f"Sua compra de R${compras:.2f} vai custar R${compras - avista5:.2f} no final.")
elif opcao == 3:
    print(f"Sua compra de R${compras} ficou parcelado 2x em {compras / 2}")
elif opcao == 4:
    vezes = int(input("Em quantas vezes você vai pagar?: "))
    if vezes == 2:
        print(opcao)
    print(f"Sua compra de R${compras:.2f} parcelada em {vezes}x ficou em R${compras / vezes}")