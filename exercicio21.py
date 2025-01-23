temperatura_celsius = print("Digite a temperatura em Celsius: ")
try:
    temperatura_celsius = int() 

except ValueError:
    print("Só é permitido valor numérico")

print(temperatura_celsius*1.8+32)
