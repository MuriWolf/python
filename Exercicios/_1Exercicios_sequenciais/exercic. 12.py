# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58


height = float(input("\nType your height separeted by point (ex: 1.63): "))

calculation = (72.7 * height) - 58
weight = int(calculation)

print(f"\nYour ideal weight is {weight} kg.")

