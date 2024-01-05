nome = input("Informe o seu nome: ")
nota_prova = int(input("Informe a nota da prova:"))
nota_qualitativa = int(input("Informe a nota qualitativa:")) 

peso_prova = 2 * nota_prova
peso_qualitativa = 1 * nota_qualitativa

media = (peso_prova + peso_qualitativa)/3

print(f"A média de {nome} na disciplina de Algoritmos é: {media:.2f}")

