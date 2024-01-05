while True:
    try:
        nota = float(input().strip())

        if 0 <= nota <= 10:
            break
        else:
            print("Nota inválida.")
    except ValueError:
        print("Entrada inválida.")

if nota >= 8.5:
    conceito = 'A'
elif nota >= 7.0:
    conceito = 'B'
elif nota >= 5.0:
    conceito = 'C'
elif nota >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

print(f"{conceito}")
