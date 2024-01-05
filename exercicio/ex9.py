entrada_hora = int(input("Informe a hora de entrada(0-23):"))
entrada_minutos = int(input("Informe o minuto de entrada(0-59):"))
saida_hora = int(input("Informe a hora de saída(0-23):"))
saida_minutos = int(input("Informe o minuto de saída(0-59):"))

horas_totais = saida_hora - entrada_hora
minutos_totais = saida_minutos - entrada_minutos

print("O empregado ficou na empresa: " ,horas_totais, "horas e " ,minutos_totais, "minutos.")

