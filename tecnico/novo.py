def converter(duracao): # criar a função

    horas =  duracao// 3600
    minutos = (duracao % 3600) // 60
    segundos = duracao % 60

    # Retorna o tempo formatado
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# Solicita ao usuário que insira o tempo em segundos
segundos = int(input("Digite o tempo em segundos: "))

# Chama a função e exibe o tempo formatado
tempo_formatado = converter(segundos)
print("Tempo formatado:", tempo_formatado)
