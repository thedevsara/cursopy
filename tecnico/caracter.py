caractere = input().strip()

if len(caractere) == 1:
    codigo = ord(caractere)
    print(codigo)
else:
    if caractere == "":
        print("32")
    else:
        print(caractere)
