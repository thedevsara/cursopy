altura = float(input().strip())
comp = float(input().strip())
largura = float(input().strip())

area_piso = largura * comp
volume_sala = largura*comp*largura
area_parede_sala = 2*altura*largura + 2*altura*comp

print(f"{area_piso:.2f}")
print(f"{volume_sala:.2f}")
print(f"{area_parede_sala:.2f}")