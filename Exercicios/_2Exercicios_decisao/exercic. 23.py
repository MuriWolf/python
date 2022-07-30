# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

numero = float(input("\nInfome um numero inteiro ou decimal: "))

int_numero = int(numero)

qual_tipo = numero != int_numero

if qual_tipo == True:
    print("\nDecimal")

elif qual_tipo == False:
    print("\nInteiro")