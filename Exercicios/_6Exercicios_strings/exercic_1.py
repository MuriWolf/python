# Tamanho de strings
# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento
# informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!

# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

str1 = "Brasil Hexa 2006"

str2 = "Brasil! Hexa 2006!"

tamanho_str1 = len(str1)

tamanho_str2 = len(str2)

print(f"A string 1 tem {tamanho_str1} caracteres")

print(f"A string 2 tem {tamanho_str2} caracteres")

print("As duas tem tamanhos e conteudos diferentes.")