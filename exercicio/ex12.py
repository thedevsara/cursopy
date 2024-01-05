valor_mercadoria = float(input("Valor a pagar pelo cliente:"))
porcentagem = float(input("Porcentagem do desconto da mercadoria:"))

desconto = valor_mercadoria * (porcentagem/100)
novo_valor = valor_mercadoria - desconto

print("O valor atualizado da mercadoria é: R$" , novo_valor)