# Altere o programa anterior permitindo ao usuário informar
# as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.


# pedir o numero de habitantes e a taxa inicial de crescimento
popA = float(input("Digite a poplulação da cidade A: "))

cresA = float(input("Digite a taxa de crescimento inicial da cidade A (em decimal): "))

popB = float(input("Digite a população da cidade B: "))

cresB = float(input("Digite a taxa de crescimento da cidade B (em decimal): "))

anos = 0

# a conta
while popA < popB:
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)
    anos = anos + 1

# o resultado

# transformar o resultado em inteiro
intA = int(popA)
intB = int(popB)

print()
print(f"Em {anos} anos a cidade A ultrapassou a B com {intA} habitantes, enquanto a cidade B ficou com {intB} habitantes.")

# 515033 habitantes, enquanto a B ficou com 510964 habitantes.