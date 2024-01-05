nome = input("Nome do vendedor: ")
qte_carros = int(input("Informe o número de carros vendidos:"))
total_vendas = float(input("Informe o valor total de vendas: "))

salario_base = 500
comissao = qte_carros * 50
extra = 0.05 * total_vendas
salario_final = salario_base + comissao + extra

print("Olá" ,nome, ",seu salário final é de: R$ ", salario_final)