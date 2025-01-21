# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

digite_data = input("Digite a data no formato dd/mm/aaaa: ")
lista = digite_data.split("/")

print(f"o primeiro elemento é: {lista[0]}")
print(f"o segundo elemento é: {lista[1]}")
print(f"o terceiro elemento é: {lista[2]}")

