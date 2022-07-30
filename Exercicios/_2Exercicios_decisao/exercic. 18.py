# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

print("\nDigite um dia/mes/ano de cada vez.")

dia = int(input("\nDigite um dia: "))

mes = int(input(f"\nDigite um mes: {dia}/"))

ano = int(input(f"\nDigite um ano: {dia}/{mes}/"))

print(f"\nData: {dia}/{mes}/{ano}")

if dia > 31 or dia < 0 or mes > 12 or mes < 0 or ano > 9999 or ano < 0:
    print("\n* Essa data não é valida *")

else:
    print("\n* Essa data é valida *")
