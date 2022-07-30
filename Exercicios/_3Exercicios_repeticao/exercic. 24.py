# Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []

print("\nDigite n para parar de digitar e o programa calcular a média.")

QtNotasWhile = int(input("\nInforme quantas notas serão informadas: "))
QtNotas = QtNotasWhile

while QtNotasWhile > 0:
    QtNotasWhile = QtNotasWhile - 1
    nota = int(input("\ninforme a nota: "))
    notas.append(nota)

conta = sum(notas) / QtNotas

print(f"\nMédia: {conta:.1f}")