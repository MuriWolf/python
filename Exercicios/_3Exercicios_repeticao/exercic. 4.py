# Supondo que a população de um país A
# seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva
# o número de anos necessários para que
# a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.

# Os dados
popA, popB, anos = 80000, 200000, 0
cresA, cresB = 0.03, 0.015

# A conta
while popA < popB:
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)
    anos = anos + 1

# O resultado
int_popA = int(popA)
int_popB = int(popB)
print(f"Em {anos} anos a população da cidade A ultrapassou a B com {int_popA} habitantes, enquanto a B ficou com {int_popB} habitantes.")