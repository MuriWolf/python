# Faça um Programa que verifique se uma letra digitada é
# "F" ou "M"
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = (input("Digite a inicial do seu sexo: "))

while letra != 'm' and letra != 'f':
    print("Sexo invalido")
    letra = (input("Digite a inicial do seu sexo: "))

if letra == 'f':
    print("Feminino")

elif letra == 'm':
    print("Masculino")
