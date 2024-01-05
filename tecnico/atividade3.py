#QUESTAO 1
'''
for contador in range(50):
    print ("Boa Tarde!")

#QUESTAO 2

faixa_de_1_a_15 = 0
faixa_de_16_a_30 = 0
faixa_de_31_a_45 = 0
faixa_de_46_a_60 =  0
faixa_maior_60 =0

for contador in range(15):

    try:
        idade = int(input("Informe sua idade: "))
        if 1 <= idade <= 15:
            faixa_de_1_a_15 += 1
        elif 16 <= idade <= 30:
            faixa_de_16_a_30 +=1
        elif 31 <= idade <= 45:
            faixa_de_31_a_45 +=1
        elif 46 <= idade <= 60:
            faixa_de_46_a_60 +=1
        elif idade >60:
            faixa_maior_60 +=1
        else:
            print("Idade inválida. Error.")
    except ValueError:
        print("Idade inválida.")

total_pessoas = faixa_de_1_a_15 + faixa_de_16_a_30 + faixa_de_31_a_45 + faixa_de_46_a_60 +  faixa_maior_60

porcentagem_1_15 = (faixa_de_1_a_15/ total_pessoas) * 100
porcentagem_16_30 = (faixa_de_16_a_30/ total_pessoas) * 100
porcentagem_31_45 = (faixa_de_31_a_45 / total_pessoas) * 100
porcentagem_46_60 = (faixa_de_46_a_60 / total_pessoas) * 100
porcentagem_61_mais = (faixa_maior_60 / total_pessoas) * 100



print("\n> > > Pesquisa de faixa etária: < < < ")
print(f"1 a 15 anos: {faixa_de_1_a_15} pessoas")
print(f"16 a 30 anos: {faixa_de_16_a_30} pessoas")
print(f"31 a 45 anos: {faixa_de_31_a_45} pessoas")
print(f"46 a 60 anos: {faixa_de_46_a_60} pessoas")
print("Maior que 61 anos: {} pessoas".format(faixa_maior_60))

print("\nPorcentagem de cada faixa etária em relação ao total de pessoas:")
print(f"1 a 15 anos: {porcentagem_1_15:.2f}%")
print(f"16 a 30 anos: {porcentagem_16_30:.2f}%")
print(f"31 a 45 anos: {porcentagem_31_45:.2f}%")
print(f"46 a 60 anos: {porcentagem_46_60:.2f}%")
print("Maior que 61 anos: {:.2f}%".format(porcentagem_61_mais))


#QUESTAO 3

maior_valor = 0
menor_valor = 999999999

qte_num = int(input("Digite a quantidade de numeros:"))

for contador in range(qte_num):
    valor = int(input("Digite um valor inteiro positivo: "))

    if valor > maior_valor:
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor

print(f"O maior valor digitado é: {maior_valor}")
print(f"O menor valor digitado é: {menor_valor}")

# QUESTAO 4

try:
    numero = int(input("Digite um número inteiro: "))
    
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                print(f"{numero} não é um número primo.")
                break
        else:
            print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

#QUESTAO 5

qte_primos = 0

for contador in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        
        if numero > 1:
            primo = True

            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                qte_primos+= 1
        else:
            print(f"{numero} não é um número primo.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

print(f"A quantidade de números primos digitados é: {qte_primos}")


#QUESTAO 6

total_votos_1 = 0
total_votos_2 = 0
total_votos_3 = 0
total_votos_4 = 0
votos_nulos = 0
votos_branco = 0

while True:
    try:
        voto = int(input("VOTE:  \n1 - Dr.Pessoa \n2 - Firmino Filho  \n3 - Silvio Mendes \n4 - Élmano Ferrer \n5 - NULO  \n6 - BRANCO  \n0 - ENCERRAR SESSÃO\n"))

        if 0 <= voto <= 6:
            if voto == 0:
                break
            elif voto == 1:
                total_votos_1 += 1
            elif voto == 2:
                total_votos_2 += 1
            elif voto == 3:
                total_votos_3 += 1
            elif voto == 4:
                total_votos_4 += 1
            elif voto == 5:
                votos_nulos += 1
            elif voto == 6:
                votos_branco += 1
        else:
            print("Código inválido. Por favor, digite um código entre 0 e 6.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n> > > APURAÇÃO DOS VOTOS < < <")
print(f"Total de votos para o Dr.Pessoa: {total_votos_1}")
print(f"Total de votos para o Firmino Filho: {total_votos_2}")
print(f"Total de votos para o Silvio Mendes: {total_votos_3}")
print(f"Total de votos para o Élmano Ferrer: {total_votos_4}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_branco}")


#QUESTAO 8

soma_das_idades = 0
qte_individuos = 0

while True:
    try:
        idade = int(input("Digite a idade do indivíduo (ou 0 para encerrar): "))
        
        if idade == 0:
            break

        soma_das_idades += idade
        qte_individuos += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if qte_individuos > 0:
    idade_media = soma_das_idades / qte_individuos
    print(f"A idade média dos indivíduos é: {idade_media:.2f}")
else:
    print("NENHUM DADO ENCONTRADO!")


# QUESTAO 9

maior_altura = float('-inf')
menor_altura = float('inf')
soma_altura_mulheres = 0
qte_mulheres = 0
qte_homens = 0

for contador in range(15):
    try:
        altura = float(input("Digite a altura da pessoa (em metros): "))
        sexo = input("Digite o sexo da pessoa (M ou F): ").upper()

        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura


        if sexo == 'F':
            soma_altura_mulheres += altura
            qte_mulheres += 1
        elif sexo == 'M':
            qte_homens += 1
        else:
            print("Sexo inválido. Por favor, digite M ou F.")

    except ValueError:
        print("Entrada inválida. Por favor, digite uma altura válida.")

if qte_mulheres > 0:
    media_altura_mulheres = soma_altura_mulheres / qte_mulheres
    print(f"\nMaior altura do grupo: {maior_altura:.2f} metros")
    print(f"Menor altura do grupo: {menor_altura:.2f} metros")
    print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} metros")
    print(f"Número de homens: {qte_homens}")
else:
    print("\nNão foram fornecidos dados de mulheres para calcular a média de altura.")



# QUESTAO 10

print("╔════════════════════════════════════════╗")
print("║ Tabela de Conversão F° para C°         ║")
print("╠════════════════════════════════════════╣")
print("║       Fahrenheit   |   Celsius         ║")
print("╟────────────────────────────────────────╢")

# Loop de 50 a 65 com incremento de 1
for fahrenheit in range(50, 66):
    # Fórmula de conversão de Fahrenheit para Celsius
    celsius = (fahrenheit - 32) * 5 / 9

    # Imprime os resultados formatados com caracteres especiais
    print(f"║   {fahrenheit}°F       |     {celsius:.2f}°C     ║")

print("╚════════════════════════════════════════╝")


#QUESTAO 11
soma_positivos = 0
soma_negativos = 0

while True:
    try:
        numero = float(input("Digite um número (ou 0 para encerrar): "))
        if numero == 0:
            break
        if numero > 0:
            soma_positivos += numero
        elif numero < 0:
            soma_negativos += numero

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

soma_total = soma_positivos + soma_negativos

print(f"\nSoma dos números positivos: {soma_positivos}")
print(f"Soma dos números negativos: {soma_negativos}")
print(f"Soma total: {soma_total}")


#QUESTAO 12

total_mulheres = 0
total_homens = 0
soma_idade_homens_exp = 0
cont_homens_exp = 0
cont_homens_acima_45 = 0
cont_mulheres_exp_abaixo_35 = 0

while True:
    try:
        idade = int(input("Digite a idade do candidato (ou 0 para encerrar): "))
        
        if idade == 0:
            break

        sexo = input("Digite o sexo do candidato (M ou F): ").upper()
        experiencia = input("O candidato possui experiência no serviço? (S ou N): ").upper()

        if sexo == 'M':
            total_homens += 1
            if experiencia == 'S':
                soma_idade_homens_exp += idade
                cont_homens_exp += 1
            if idade > 45:
                cont_homens_acima_45 += 1
        elif sexo == 'F':
            total_mulheres += 1
            if idade < 35 and experiencia == 'S':
                cont_mulheres_exp_abaixo_35 += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

idade_media_homens_exp = soma_idade_homens_exp / cont_homens_exp if cont_homens_exp > 0 else 0

porcentagem_homens_acima_45 = (cont_homens_acima_45 / total_homens) * 100 if total_homens > 0 else 0

print("\nLEVANTAMENTO DOS DADOS DA EMPRESA:")
print(f"Número de candidatas do sexo feminino: {total_mulheres}")
print(f"Número de candidatos do sexo masculino: {total_homens}")
print(f"Idade média dos homens com experiência: {idade_media_homens_exp:.2f}")
print(f"Porcentagem de homens com mais de 45 anos: {porcentagem_homens_acima_45:.2f}%")
print(f"Número de mulheres com idade inferior a 35 anos e com experiência: {cont_mulheres_exp_abaixo_35}")




#QUESTÃO 13

soma_peso_faixa_1_10 = 0
soma_peso_faixa_11_20 = 0
soma_peso_faixa_21_30 = 0
soma_peso_maior_30 = 0
cont_faixa_1_10 = 0
cont_faixa_11_20 = 0
cont_faixa_21_30 = 0
cont_maior_30 = 0

for i in range(15):
    try:
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        peso = float(input(f"Digite o peso da pessoa {i+1} (em kg): "))

        if 1 <= idade <= 10:
            soma_peso_faixa_1_10 += peso
            cont_faixa_1_10 += 1
        elif 11 <= idade <= 20:
            soma_peso_faixa_11_20 += peso
            cont_faixa_11_20 += 1
        elif 21 <= idade <= 30:
            soma_peso_faixa_21_30 += peso
            cont_faixa_21_30 += 1
        elif idade > 30:
            soma_peso_maior_30 += peso
            cont_maior_30 += 1
        else:
            print("Idade inválida. Error.")

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")

media_peso_faixa_1_10 = soma_peso_faixa_1_10 / cont_faixa_1_10 if cont_faixa_1_10 > 0 else 0
media_peso_faixa_11_20 = soma_peso_faixa_11_20 / cont_faixa_11_20 if cont_faixa_11_20 > 0 else 0
media_peso_faixa_21_30 = soma_peso_faixa_21_30 / cont_faixa_21_30 if cont_faixa_21_30 > 0 else 0
media_peso_maior_30 = soma_peso_maior_30 / cont_maior_30 if cont_maior_30 > 0 else 0

print("\nMédias dos pesos por faixa etária:")
print(f"1 a 10 anos: {media_peso_faixa_1_10:.2f} kg")
print(f"11 a 20 anos: {media_peso_faixa_11_20:.2f} kg")
print(f"21 a 30 anos: {media_peso_faixa_21_30:.2f} kg")
print("Maiores de 30 anos: {:.2f} kg".format(media_peso_maior_30))


#QUESTAO 14

total_aprovados = 0
total_reprovados = 0
soma_medias_alunos = 0

for i in range(6):
    try:
        nota1 = float(input(f"Digite a primeira nota do aluno {i+1}: "))
        nota2 = float(input(f"Digite a segunda nota do aluno {i+1}: "))
        media = (nota1 + nota2) / 2

        soma_medias_alunos += media

        print(f"Média do aluno {i+1}: {media:.2f}")

        if 0 <= media <= 5.0:
            print("Situação: Reprovado")
            total_reprovados += 1
        elif 5.1 <= media <= 6.9:
            print("Situação: Recuperação")
        elif 7.0 <= media <= 10:
            print("Situação: Aprovado")
            total_aprovados += 1
        else:
            print("Nota inválida. Error.")

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")

media_geral = soma_medias_alunos / 6

print(f"Total de alunos aprovados: {total_aprovados}")
print(f"Total de alunos reprovados: {total_reprovados}")
print(f"Média geral do programa: {media_geral:.2f}")

#QUESTAO 15

soma_alturas = 0
cont_pessoas_50 = 0

while True:
    try:
        idade = int(input("Digite a idade do usuário (ou idade <= 0 para encerrar): "))
        
        if idade <= 0:
            break

        altura = float(input("Digite a altura da pessoa (em metros): "))

        if idade > 50:
            soma_alturas += altura
            cont_pessoas_50 += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")

media_alturas_50 = soma_alturas / cont_pessoas_50 if cont_pessoas_50 > 0 else 0

print(f"Média das alturas das pessoas com mais de 50 anos: {media_alturas_50:.2f} metros")


#QUESTAO 16

soma_idades_otimo = 0
cont_otimo = 0
cont_regular = 0
cont_bom = 0

for i in range(15):
    try:
        idade = int(input(f"Digite a idade do espectador {i+1}: "))
        opiniao = int(input("Qual a sua opinião sobre o filme: \n1 - Regular  \n2 - Bom \n3 - Ótimo "))

        if opiniao == 3:
            soma_idades_otimo += idade
            cont_otimo += 1
        elif opiniao == 1:
            cont_regular += 1
        elif opiniao == 2:
            cont_bom += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")

media_idades_otimo = soma_idades_otimo / cont_otimo if cont_otimo > 0 else 0

porcentagem_bom = (cont_bom / 15) * 100

print(f"Média das idades das pessoas que responderam ótimo: {media_idades_otimo:.2f} anos")
print(f"Quantidade de pessoas que responderam regular: {cont_regular}")
print(f"Porcentagem de pessoas que responderam bom: {porcentagem_bom:.2f}%")

#QUESTAO 17

total_sim = 0
total_nao = 0
mulheres_sim = 0
total_homens = 0
homens_nao = 0

for i in range(10):
    try:
        sexo = input(f"Digite o sexo do entrevistado {i+1} (M ou F): ").upper()
        resposta = input("Digite a resposta do entrevistado (sim ou não): ").lower()

        if resposta == 'sim':
            total_sim += 1
        elif resposta == 'não':
            total_nao += 1

        if sexo == 'F' and resposta == 'sim':
            mulheres_sim += 1

        if sexo == 'M':
            total_homens += 1
            if resposta == 'não':
                homens_nao += 1

    except ValueError:
        print("Entrada inválida. Por favor, digite valores válidos.")

porcentagem_homens_nao = (homens_nao / total_homens) * 100 if total_homens > 0 else 0

print(f"Total de pessoas que responderam sim: {total_sim}")
print(f"Total de pessoas que responderam não: {total_nao}")
print(f"Total de mulheres que responderam sim: {mulheres_sim}")
print(f"Porcentagem de homens que responderam não: {porcentagem_homens_nao:.2f}%")

#QUESTAO 18

soma_pares = 0
soma_impares = 0

for i in range(10):
    try:
        numero = int(input(f"Digite o {i+1}º número: "))

        if numero % 2 == 0:
            soma_pares += numero
        else:
            soma_impares += numero

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")


#QUESTAO 19

total_pessoas_assistindo = 0
audiencia_canais = {'4': 0, '5': 0, '7': 0, '12': 0}

while True:
    try:
        canal = input("Digite o número do canal (4, 5, 7, 12), ou 0 para encerrar: ")

        if canal == '0':
            break
        if canal not in audiencia_canais:
            print("Canal inválido. Por favor, digite um número válido.")
            continue

        pessoas_assistindo = int(input(f"Digite o número de pessoas assistindo ao canal {canal}: "))

        audiencia_canais[canal] += pessoas_assistindo
        total_pessoas_assistindo += pessoas_assistindo

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")

for canal, audiencia in audiencia_canais.items():
    porcentagem = (audiencia / total_pessoas_assistindo) * 100 if total_pessoas_assistindo > 0 else 0
    print(f"Canal {canal}: {porcentagem:.2f}% de audiência")

'''