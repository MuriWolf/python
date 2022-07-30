# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:

# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print("\nType (m) for man and (w) for woman!\n")
gender = str(input("Type your gender: "))

while gender != 'm' and gender != 'w':
    print("\nType (m) for man and (w) for woman!\n")
    gender = str(input("Type your gender: "))

if gender == 'm':
    heigth_man = float(input("\nType your height separeted by point (ex: 1.70): "))
    calulation_man = (72.7 * heigth_man) - 58
    int_height_man = int(calulation_man)
    print(f"\nYour ideal weight is {int_height_man} kg.")

elif gender == 'w':
    heigth_woman = float(input("\nType your height separeted by point (ex: 1.70): "))
    calulation_woman = (62.1 * heigth_woman) - 44.7
    int_height_woman = int(calulation_woman)
    print(f"\nYour ideal weight is {int_height_woman} kg.")

