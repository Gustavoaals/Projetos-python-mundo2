codigo = "int@var ==10"
if codigo[4] == '@':
    codigo = codigo[:4] + codigo[5:]
print(codigo)