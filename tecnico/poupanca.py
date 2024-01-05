depositoInicial = float(input().strip())
jurosAnual = float(input().strip())

jurosDecimal = jurosAnual / 100

totalAcumulado = depositoInicial
anos = 0

while totalAcumulado < (depositoInicial * 2):
    totalAcumulado += totalAcumulado * jurosDecimal
    anos += 1

print(f"{anos}")


