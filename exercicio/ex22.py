#questao 1 
'''
number1= float(input("Digite o primeiro numero: "))
number2= float(input("Digite o segundo numero: "))

if(number1 > number2):
    print(number1)
elif number2 > number1:
    print(number2)
elif(number1 == number2):
    print("Os números são iguais.")
else:
    print("Número inválido.")
    

'''

#questao 2
'''
valor = float(input("Digite um valor:"))

if(valor <0):
    print("Valor negativo.")
elif(valor > 0):
    print("Valor positivo.")
elif(valor == 0):
    print("Valor é 0.")
else:
    ("Número inválido.")
'''
#questao 3
'''
letra = input("Informe seu sexo (F ou M):")

if(letra == "F" or letra == "f"):
    print("Seu sexo é FEMININO.")
elif(letra == "M" or letra == "m"):
    print("Seu sexo é MASCULINO.")  
else:
    print("Sexo inválido.")
'''

#questao 4 
'''
ano = int(input("Informe um ano(4 digitos): "))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

'''

#questao 5
'''
while True:
    letra = input("Digite uma letra:")

    if len(letra) ==1 and 'a' <= letra <= 'z':

        if(letra.lower() == 'aeiou'):
            print(f"A letra {letra} é uma vogal.")
        else:
            print(f"A letra {letra} é uma consoante.")
    else:
        print(f"Entrada inválida, digite uma única letra.")

'''

#questao 6

'''
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 >= number2 >= number3:
    print(f"{number1},{number2},{number3}")
elif number1 >= number3 >= number2:
    print(f"{number1},{number3},{number2}")
elif number2 >= number1 >= number3:
    print(f"{number2},{number1},{number3}")
elif number2 >= number3 >= number1:
    print(f"{number2},{number3},{number1}")
elif number3 >= number1 >= number2:
    print(f"{number3},{number1},{number2}")
else:
    print(f"{number3},{number2},{number1}")

'''

#questao 7
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = nota1 + nota2/2

if(media < 7):
    print("Aluno reprovado.")
elif(media>=7 or media<10):
    print("Aluno aprovado.")
elif(media == 10):
    print("Aluno aprovado com DISTINÇÃO.")
else:
    print("Entrada inválida.")
'''

#questao 8 e 9
'''
number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))
number3 = float(input("Digite o terceiro número: "))

maiorNumero = number1
menorNumero = number1

if(number2 > maiorNumero):
    maiorNumero = number2
elif(number2 < menorNumero):
    menorNumero = number2

if(number3 > maiorNumero):
    maiorNumero = number3
elif(number3 < menorNumero):
    menorNumero = number3

print(f"O maior número é: {maiorNumero}")
print(f"O menor número: {menorNumero}")
'''

#questao 10
'''
preco1 = float(input("Digite o preço do primeiro produto:"))
preco2 = float(input("Digite o preço do segundo produto:"))
preco3 = float(input("Digite o preço do terceiro produto:"))

mais_barato = preco1

if(preco2 < mais_barato):
    mais_barato = preco2

if(preco3 < mais_barato):
    mais_barato = preco3

if mais_barato == preco1:
    print("Você deve comprar o produto 1.")
elif mais_barato == preco2:
    print("Você deve comprar o produto 2.")
elif mais_barato == preco3:
    print("Você deve comprar o produto 3.")
else:
    print("Entrada inválida!")

'''

# questao 11

'''

turno = input("Informe em qual turno você estuda: \nM - MATUTINO  \nV - VESPERTINO \nN - NOTURNO")

if turno == 'M' or turno == 'm':
    print("BOM DIA.")
elif turno == 'V' or turno == 'v':
    print("BOA TARDE.")
elif turno == 'N' or turno == 'n':
    print("BOA NOITE.")
else:
    print("Entrada inválida.")

'''

#questao 12
'''
salario = float(input("Informe seu salario para calcular reajuste: "))

if salario >0.0 and salario <= 280.00:
    valor_do_aumento = salario * 0.2
    total_com_reajuste = salario + valor_do_aumento
    percentual_aumento = 20
elif salario >= 280.00 and salario <700.00:
    valor_do_aumento = salario * 0.15
    total_com_reajuste = salario + valor_do_aumento
    percentual_aumento = 15
elif salario >= 700.00 and salario < 1500.00:
    valor_do_aumento = salario * 0.10
    total_com_reajuste = salario + valor_do_aumento
    percentual_aumento = 10
elif salario >= 1500.00:
    valor_do_aumento = salario * 0.05
    total_com_reajuste = salario + valor_do_aumento
    percentual_aumento = 5
else:
    print("Entrada inválida.")


print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R$ {valor_do_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {total_com_reajuste:.2f}")

'''

#questao 13
'''
valor_hora = float(input("Informe o valor da sua hora de trabalho:"))

horas_trabalhadadas_mes = int(input("Infome a quantidade de horas trabalhadas no mês:"))

salario_bruto = valor_hora * horas_trabalhadadas_mes

#imposto de renda

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <=1500:
    desconto_ir =  salario_bruto * 0.05
elif salario_bruto <=2500:
    desconto_ir = salario_bruto * 0.1
else: 
    desconto_ir = salario_bruto * 0.2

#outros descontos:

desconto_inss = salario_bruto * 0.1
desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.01

#total dos descontos:

total_descontos = desconto_ir + desconto_inss + desconto_sindicato

#salario liquido:

salario_liquido = salario_bruto - total_descontos


print(f"Salario Bruto: {valor_hora} * {horas_trabalhadadas_mes} : R${salario_bruto:.2f}")
print(f"(-) IR ({desconto_ir*100/salario_bruto}%): R${desconto_ir:.2f}")
print(f"(-) INSS (10%): R${desconto_inss:.2f}")
print(f"(-) Sindicato (3%): R${desconto_sindicato:.2f}")
print(f"FGTS (1%): R${fgts:.2f}")
print(f"Total de descontos: R${total_descontos:.2f}")
print(f"Salario Liquido: R${salario_liquido:.2f}")

'''

#questao 14
'''
numero = int(input("Digite um número que corresponde a um dia da semana: \n1 - Domingo \n2 - Segunda \n3 - Terça \n4 - Quarta \n5 - Quinta \n6 - Sexta \n7 - Sábado \n"))


if numero == 1:
    print("Hoje é Domingo.")

elif numero == 2:
    print("Hoje é Segunda-feira.")

elif numero == 3:
    print("Hoje é Terça-feira.")

elif numero == 4:
    print("Hoje é Quarta-feira.")

elif numero == 5:
    print("Hoje é Quinta-feira.")

elif numero == 6:
    print("Hoje é Sexta-feira")

elif numero == 7:
    print("Hoje é Sábado.")
else:
    print("Valor Inválido.")

'''

#questao 15
'''
preco_custo = float(input("Informe o preço de custo do produto: "))

codigo_origem = int(input("Informe o codigo de produto: \n1 - Sul \n2 - Norte \n3 - Leste \n4 - Oeste \n5 ou 6 - Nordeste \n7 ou 8 - Centro-oeste."))

if codigo_origem == 1:
    print(f"Produto procedente da região Sul. Preço: R$ {preco_custo:.2f}")
elif codigo_origem == 2:
    print(f"Produto procedente da região Norte. Preço: R$ {preco_custo:.2f}")
elif codigo_origem == 3:
    print(f"Produto procedente da região Leste. Preço: R$ {preco_custo:.2f}")
elif codigo_origem == 4:
    print(f"Produto procedente da região Oeste. Preço: R$ {preco_custo:.2f}")
elif codigo_origem == 5 or codigo_origem == 6:
    print(f"Produto procedente da região Nordeste. Preço: R$ {preco_custo:.2f}")
elif codigo_origem == 7 or codigo_origem == 8:
    print(f"Produto procedente da região Centro-oeste. Preço: R$ {preco_custo:.2f}")
else:
    print("Produto classificado como importado.")

'''

#questao 16

'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >=0 or media <=3:
    print("Aluno reprovado.")
if media >3 or media <= 6.9:
    print("Aluno em exame final.")
elif media>=7 or media<=10:
    print("Aluno aprovado.")
else:
    print("Entrada inválida.")


'''

# questao 17 
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

if conceito == "A" or conceito == "B" or conceito == "C":
    print("APROVADO")
else:
    print("REPROVADO")

'''

#questao 18
'''
lado1 = float(input("Informe o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Informe o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Informe o comprimento do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Não é possível formar um triângulo com esses lados.")

'''

#questão 19

'''
a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + (delta ** 0.5)) / (2*a)
        raiz2 = (-b - (delta ** 0.5)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")

'''

#questao 20

'''
ano = int(input("Informe um ano(4 digitos): "))

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

'''

#questao 21

'''
data_str = input("Digite a data no formato d/m/a: ")

# Divide a string da data nos componentes dia, mês e ano
dia, mes, ano = map(int, data_str.split('/'))

# Verifica se a data é válida
if 1 <= mes <= 12:
    if mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            if 1 <= dia <= 29:
                print("A data é válida.")
            else:
                print("A data é inválida.")
        else:
            if 1 <= dia <= 28:
                print("A data é válida.")
            else:
                print("A data é inválida.")
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            print("A data é válida.")
        else:
            print("A data é inválida.")
    else:
        if 1 <= dia <= 30:
            print("A data é válida.")
        else:
            print("A data é inválida.")
else:
    print("A data é inválida.")

'''

#questao 22


'''
numero = int(input("Informe um número inteiro menor que 1000: "))

if 0 < numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    print(f"Centenas: {centenas}\nDezenas: {dezenas}\nUnidades: {unidades}")
else:
    print("Número inválido. Por favor, insira um número inteiro menor que 1000.")

'''

#questao 23 

'''
numero = int(input("Digite um número inteiro menor que 1000: "))

if 0 < numero < 1000:

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    resultado = ""

    if centenas > 0:
        resultado += f"{centenas} {'centena' if centenas == 1 else 'centenas'}"
    if dezenas > 0:
        if centenas > 0:
            resultado += ", "
        resultado += f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}"
    if unidades > 0:
        if centenas > 0 or dezenas > 0:
            resultado += " e "
        resultado += f"{unidades} {'unidade' if unidades == 1 else 'unidades'}"

    # Imprime o resultado
    print(resultado)
else:
    print("Número inválido. Por favor, insira um número inteiro menor que 1000.")

'''

#questao 24

'''
idade1 = int(input("Digite a idade do primeiro aluno: "))
idade2 = int(input("Digite a idade do segundo aluno: "))
idade3 = int(input("Digite a idade do terceiro aluno: "))

media_idades = (idade1 + idade2 + idade3) / 3

if media_idades < 25:
    print("Turma Jovem")
elif 25 <= media_idades <= 40:
    print("Turma Adulta")
else:
    print("Turma Idosa")

'''

#questao 25
'''
nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))
nota3 = float(input("Digite a terceira nota parcial: "))

media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f"Aprovado com Distinção. Média: {media}")
elif media >= 7:
    print(f"Aprovado. Média: {media}")
else:
    print(f"Reprovado. Média: {media}")

'''

#questao 26

'''
valor_saque = int(input("Informe o valor do saque: (entre 10 e 600 reais) "))

if 10 <= valor_saque <= 600:
    notas_100 = valor_saque // 100
    valor_saque %= 100

    notas_50 = valor_saque // 50
    valor_saque %= 50

    notas_10 = valor_saque // 10
    valor_saque %= 10

    notas_5 = valor_saque // 5
    valor_saque %= 5

    notas_1 = valor_saque

    if notas_100 > 0:
        print(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100 reais")
    if notas_50 > 0:
        print(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50 reais")
    if notas_10 > 0:
        print(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10 reais")
    if notas_5 > 0:
        print(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5 reais")
    if notas_1 > 0:
        print(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1 real")
else:
    print("Valor de saque inválido. Por favor, insira um valor entre 10 e 600 reais.")

'''

#questao 27

'''
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

'''

#questao 28
'''
numero = float(input("Digite um número: "))

if int(numero) == numero:
    print(f"{numero} é um número inteiro.")
else:
    print(f"{numero} é um número decimal.")

'''

#questao 29
'''
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação desejada (+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Divisão por zero.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    par_impar = "par" if resultado % 2 == 0 else "ímpar"

    pos_neg = "positivo" if resultado > 0 else ("negativo" if resultado < 0 else "zero")

    if resultado % 1 == 0:
        inteiro_decimal = "inteiro"
    else:
        inteiro_decimal = "decimal"

    print(f"Resultado da operação: {resultado:.2f}")
    print(f"O número é {par_impar}, {pos_neg} e {inteiro_decimal}.")

'''

# questao 30
'''
respostas_positivas = 0

pergunta1 = input("Telefonou para a vítima? (Sim/Não): ")
if pergunta1.lower() == "sim":
    respostas_positivas += 1

pergunta2 = input("Esteve no local do crime? (Sim/Não): ")
if pergunta2.lower() == "sim":
    respostas_positivas += 1

pergunta3 = input("Mora perto da vítima? (Sim/Não): ")
if pergunta3.lower() == "sim":
    respostas_positivas += 1

pergunta4 = input("Devia para a vítima? (Sim/Não): ")
if pergunta4.lower() == "sim":
    respostas_positivas += 1

pergunta5 = input("Já trabalhou com a vítima? (Sim/Não): ")
if pergunta5.lower() == "sim":
    respostas_positivas += 1

#classificação
if respostas_positivas == 2:
    print("Você é suspeito(a)!")
elif 3 <= respostas_positivas <= 4:
    print("Você é cúmplice!")
elif respostas_positivas == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente.")

    
'''

#questao 31

'''
litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ")

preco_alcool = 1.90
preco_gasolina = 2.50

if tipo_combustivel == 'A' or tipo_combustivel == 'a':
    if litros_vendidos <= 20:
        preco_final = litros_vendidos * (preco_alcool * 0.97)
    else:
        preco_final = litros_vendidos * (preco_alcool * 0.95)
elif tipo_combustivel == 'G' or tipo_combustivel == 'g':
    if litros_vendidos <= 20:
        preco_final = litros_vendidos * (preco_gasolina * 0.96)
    else:
        preco_final = litros_vendidos * (preco_gasolina * 0.94)
else:
    print("Tipo de combustível inválido. Use A para álcool ou G para gasolina.")
    preco_final = None

if preco_final is not None:
    print(f"Valor a ser pago: R$ {preco_final:.2f}")

'''

#questão 32 

'''
qte_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
qte_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

preco_morango = 2.50 if qte_morangos <= 5 else 2.20
preco_maca = 1.80 if qte_macas <= 5 else 1.50

custo_total = (qte_morangos * preco_morango) + (qte_macas * preco_maca)

if qte_morangos + qte_macas > 8 or custo_total > 25.0:
    desconto = 0.10 * custo_total
    custo_total -= desconto

print(f"Valor a ser pago: R$ {custo_total:.2f}")


'''