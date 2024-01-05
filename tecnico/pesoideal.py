altura = float(input().strip())
sexo = int(input().strip())  #("\nInforme seu sexo: \n1-Masculino \n2-Feminino "))

if(sexo == 1):
    peso_ideal_homens = (72.7 * altura) - 58
    print(f"{peso_ideal_homens:.2f}")
elif(sexo == 2):
    peso_ideal_mulheres = (62.1 * altura) - 44.7
    print(f"{peso_ideal_mulheres:.2f}")
else:
    input("Opçao inválida.")
    



