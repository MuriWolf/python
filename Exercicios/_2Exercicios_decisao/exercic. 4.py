# Faça um Programa que verifique se uma letra digitada
# é vogal ou consoante.

max = 1

letra = (input("Digite uma letra: "))

# se o usuarios digitar mais que uma letra
while len(letra) > max:
    print("Digite apenas uma letra!")
    letra = (input("Digite uma letra: "))

# se for uma vogal
if (letra != 'a') and (letra != 'e') and (letra != 'i') and (letra != 'o') and (letra != 'u'):
    print(f"A letra {letra} é uma consoante.")

# se for uma consoante
else:
    print(f"A letra {letra} é uma vogal.")