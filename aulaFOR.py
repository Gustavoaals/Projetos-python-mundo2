#n = int(input("Digite um num: "))
#for c in range(0, n+1):
 #   print(c)
#print("FIM!")

s = 0 
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s += n 
    s = s /4

print(f"O somatório de todos os valores foi {s}")
print(f"Dividido por 4 é igual a {s}")