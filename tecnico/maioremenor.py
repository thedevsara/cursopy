maior = None
menor = None

while True:
    entrada = input().strip()

    try:
        numero = int(entrada)

        if numero == 0:
            break

        if numero > 0:
            if maior is None or numero > maior:
                maior = numero
            if menor is None or numero < menor:
                menor = numero
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

if maior is not None:
    print(f"{maior}")
else:
    print("Nenhum número válido foi lido.")

if menor is not None:
    print(f"{menor}")
else:
    print("Nenhum número válido foi lido.")
