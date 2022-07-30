# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.

parte1 = float(input("\nDigite o valor do lado 1 de um triangulo: "))

parte2 = float(input("\nDigite o valor do lado 2 de um triangulo: "))

parte3 = float(input("\nDigite o valor do lado 3 de um triangulo: "))

# Triângulo Equilátero
if parte1 == parte2 and parte2 == parte3:
    print("\nEsse triângulo é um equilátero.")

# Triângulo Isósceles
elif parte1 == parte2 and parte2 != parte3:
    print("\nEsse triângulo é um isóceles.")

# Triângulo Isósceles
elif parte1 != parte2 and parte2 == parte3:
    print("\nEsse triângulo é um isóceles.")

# Triângulo Escaleno
elif parte1 != parte2 and parte1 != parte3 and parte2 != parte3:
    print("\nEssse triângulo é um escaleno.")