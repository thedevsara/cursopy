custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))
percent_distribuidor = 0.12 
percent_impostos = 0.45     

custo_distribuidor = custo_fabrica * percent_distribuidor
custo_impostos = custo_fabrica * percent_impostos
custo_consumidor = custo_fabrica + custo_distribuidor + custo_impostos

print(f"O custo ao consumidor de um carro novo é: R$ {custo_consumidor:.2f}")
