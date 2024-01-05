numero = int(input().strip())

if 0 <= numero < 100000:
    soma = 0
    if numero == 0:
        print("0")
    else:
        while numero > 0:
            digito = numero % 10
            soma += digito
            numero = numero // 10
        print(soma)
else:
    print("-1")