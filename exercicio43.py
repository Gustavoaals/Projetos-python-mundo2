#Calculadora de IMC

print('-=' * 20)
print("CALCULADORA DE IMC".center(40))
print('-=' * 20)

peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? (m) "))
imc = peso / (altura * altura)

print(f"O IMC desta pessoa é de {imc:.2f}")

if imc < 18.5:
    print("Você está ABAIXO do peso.")
elif imc >= 18.5 and imc < 25:# ou poderia ser elif imc < 25:
    print("Muito bem, você está faixa do PESO NORMAL!!")
elif imc >=25 and imc <30:
    print("Você está SOBREPESO.")
elif imc >= 30 and imc < 40:
    print("Você está com OBESIDADE.")
else:
    print("Você está com Obesidade Mórbida.")
