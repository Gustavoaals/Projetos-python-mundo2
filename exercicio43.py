print('-=' * 20)
print("CALCULADORA DE IMC".center(40))
print('-=' * 20)

peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? (m) "))
idade = int(input("Qual sua idade? "))
sexo = input("Você é homem ou mulher? ").strip().lower()

imc = peso / (altura * altura)

print(f"\nSeu IMC é: {imc:.2f}")

# Classificação
if imc < 18.5:
    print("Você está ABAIXO do peso.")
elif imc < 25:
    print("Você está na faixa do PESO NORMAL.")
elif imc < 30:
    print("Você está com SOBREPESO.")
elif imc < 40:
    print("Você está com OBESIDADE.")
else:
    print("Você está com OBESIDADE MÓRBIDA.")

# Média de IMC (simulação de banco)
media_imc = {
    "homem": 26,
    "mulher": 24
}

if sexo in media_imc:
    print(f"\nMédia de IMC para {sexo}: {media_imc[sexo]}")
else:
    print("\nSexo informado inválido.")

# Cálculo do peso ideal
peso_minimo = 18.5 * (altura ** 2)
peso_maximo = 24.9 * (altura ** 2)

print("\n=== FAIXA DE PESO IDEAL ===")
print(f"Peso mínimo saudável: {peso_minimo:.2f} Kg")
print(f"Peso máximo saudável: {peso_maximo:.2f} Kg")

# Comparação com peso atual
if peso < peso_minimo:
    print("Você precisa GANHAR peso para entrar na faixa ideal.")
elif peso > peso_maximo:
    print("Você precisa REDUZIR peso para entrar na faixa ideal.")
else:
    print("Você está dentro da faixa de peso ideal! 🎯")