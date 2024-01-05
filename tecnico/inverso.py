num = int(input().strip())
num_invertido = 0

while num > 0:
    digito = num % 10 
    num_invertido = num_invertido * 10 + digito
    num //= 10 

print(f"{num_invertido}")
