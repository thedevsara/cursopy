def avaliar_a_sara():
    while True:
        try:
            avaliacao = int(input("Digite sua avaliação (1, 2, 3, 4 ou 5 estrelas): "))
            if 1 <= avaliacao <= 5:
                return avaliacao
            else:
                print("Por favor, escolha uma avaliação entre 1 e 5 estrelas.")
        except ValueError:
            print("Por favor, insira um número válido (1, 2, 3, 4 ou 5).")

avaliacao = avaliar_a_sara()
print("Você avaliou a Sara com", avaliacao, "estrelas.")
print("A Sara agradece sua avaliação.")
