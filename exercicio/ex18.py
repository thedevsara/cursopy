preco_hamburguer = 3.00
preco_cheeseburger = 2.50
preco_fritas = 2.50
preco_refrigerante = 1.00
preco_milkshake = 3.00

qte_hamburguer = int(input("Quantidade de hambúrgueres: "))
qte_cheeseburger = int(input("Quantidade de cheeseburgers: "))
qte_fritas = int(input("Quantidade de porções de fritas: "))
qte_refrigerante = int(input("Quantidade de refrigerantes: "))
qte_milkshake = int(input("Quantidade de milkshakes: "))

total = (qte_hamburguer * preco_hamburguer) + (qte_cheeseburger * preco_cheeseburger) + (qte_fritas * preco_fritas) + (qte_refrigerante * preco_refrigerante) + (qte_milkshake * preco_milkshake)


print(f"Total a pagar: R$ {total:.2f}")
