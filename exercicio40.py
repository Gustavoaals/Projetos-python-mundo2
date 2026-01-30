#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media =  (nota1 + nota2) /2

print(f"Tirando {nota1:.2f} e {nota2:.2f}, a media foi {media:.2f} ")

if 7 > media >= 5:
    print("O aluno está de RECUPERAÇÃO")
elif media < 5:
    print("O aluno está REPROVADO.")
elif media >= 7:
    print("O aluno está APROVADO!!")