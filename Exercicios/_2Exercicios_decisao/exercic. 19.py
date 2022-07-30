# Faça um Programa que leia um número inteiro menor que 1000
# e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades

# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

a = 3 # minha versao nova

numero = int(input("\nDigite um numero de 1 até 999: "))

numero_str = str(numero)

qtnumero = len(numero_str)

if qtnumero == 1:
    unidade = numero_str[0:1]
    print(f"{numero} = {unidade} unidade(s)")

if qtnumero == 2:
    dezena = numero_str[0:1]
    unidade = numero_str[1:2]
    print(f"{numero} = {dezena} dezena(s) e {unidade} unidade(s)")

if qtnumero == 3:
    centena = numero_str[0:1]
    dezena = numero_str[1:2]
    unidade = numero_str[2:3]
    print(f"{numero} = {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)")

b = 1 # jeito que nao deu certo kkk

# numero = int(input("\nDigite um numero inteiro: "))
#
# numero_real = numero
#
# unidades = 0
#
# dezenas = 0
#
# centenas = 0
#
# # numero menor que uma dezena
# if numero < 10 and numero > 0:
#     while numero > 0:
#         numero = numero - 1
#         unidades = unidades + 1
#
#     if numero_real == 1:
#         print(f"\n{numero_real} = {unidades} unidade")
#
#     elif numero_real > 1:
#         print(f"\n{numero_real} = {unidades} unidades")
#
# # numero igual a uma dezena
# elif numero == 10:
#     while numero > 0:
#         numero = numero - 10
#         dezenas = dezenas + 1
#
#     print(f"\n{numero_real} = {dezenas} dezena")
#
# # numero maior que uma dezena
# elif numero > 10 and numero < 100:
#     while numero > 10 or numero > 0:
#         numero = numero - 10
#         dezenas = dezenas + 1
#
#         if numero < 10:
#             while numero > 0:
#                 numero = numero - 1
#                 unidades = unidades + 1
#
#             if numero_real == 11:
#                 print(f"\n{numero_real} = {dezenas} dezena e {unidades} unidade")
#
#             elif numero_real < 20:
#                 print(f"\n{numero_real} = {dezenas} dezena e {unidades} unidades")
#
#             elif numero_real == numero_real == 21 or numero_real == 31 or numero_real == 41 or numero_real == 51 or numero_real == 61 or numero_real == 71 or numero_real == 81 or numero_real == 91:
#                 print(f"\n{numero_real} = {dezenas} dezenas e {unidades} unidade")
#
#             elif numero_real > 19 and numero_real != 11 and numero_real != 21 and numero_real != 31 and numero_real != 41 and numero_real != 51 and numero_real != 61 and numero_real != 71 and numero_real != 81 and numero_real != 91:
#                 print(f"\n{numero_real} = {dezenas} dezenas e {unidades} unidades")
#
#
# # numero igual a 100
# elif numero == 100:
#     while numero > 0:
#         numero = numero - 100
#         centenas = centenas + 1
#
#     print(f"\n{numero_real} = {centenas} centena")
#
# # numero que terminam com dois zeros
# if numero_real == 200 or numero_real == 300 or numero_real == 400 or numero_real == 500 or numero_real == 600 or numero_real == 700 or numero_real == 800 or numero_real == 900:
#     while numero > 100 or numero > 0:
#         numero = numero - 100
#         centenas = centenas + 1
#
#     if numero_real == 200 or numero_real == 300 or numero_real == 400 or numero_real == 500 or numero_real == 600 or numero_real == 700 or numero_real == 800 or numero_real == 900:
#         print(f"{numero_real} = {centenas} centenas")
#
# # numero que temina com um zero
#
#
# # numero maior que 100
# elif numero > 100 and numero != 200 and numero != 300 and numero != 400 and numero != 500 and numero != 600 and numero != 700 and numero != 800 and numero != 900:
#     while numero > 100:
#         numero = numero - 100
#         centenas = centenas + 1
#
#         if numero < 10:
#             while numero > 0:
#                 numero = numero - 1
#                 unidades = unidades + 1
#
#             if numero_real == 101:
#                print(f"{numero_real} = {centenas} centena e {unidades} unidade")
#
#             elif numero_real > 101 and numero_real < 110:
#                 print(f"{numero_real} = {centenas} centena e {unidades} unidades")
#
#         elif numero < 100:
#             while numero > 10 or numero > 11:
#                 numero = numero - 10
#                 dezenas = dezenas + 1
#
#             if numero < 10:
#                 while numero > 0:
#                     numero = numero - 1
#                     unidades = unidades + 1
#
#                 if numero_real == 110:
#                     print(f"{numero_real} = {centenas} centena e {dezenas} dezena")
#
#                 elif numero_real == 111:
#                     print(f"{numero_real} = {centenas} centena, {dezenas} dezena e {unidades} unidade")
#
#                 elif numero_real > 111 and numero_real < 120:
#                     print(f"{numero_real} = {centenas} centena, {dezenas} dezena e {unidades} unidades")
#
#                 elif numero_real > 120 and numero_real < 200:
#                     print(f"{numero_real} = {centenas} centena, {dezenas} dezenas e {unidades} unidades")
#
#                 elif numero_real > 200 and numero_real < 999 and numero_real != 300 and numero_real != 400 and numero_real != 500 and numero_real != 600 and numero_real != 700 and numero_real != 800 and numero_real != 900:
#                     print(f"{numero_real} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades")

c = 2# parte certa kkkkkk (NAO É O MELHOR JEITO DE FAZER)

# numero = input("digite um numero menor que 1000 ---> ")
# numeroStr = str(numero)
# qtNumero = len(numeroStr)

# if qtNumero == 3:
#     centena = numeroStr[0:1]
#     dezena = numeroStr[1:2]
#     unidade = numeroStr[2:3]
#     print(numeroStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")
#
# if qtNumero == 2:
#     dezena = numeroStr[0:1]
#     unidade = numeroStr[1:2]
#     print(numeroStr+" = "+dezena+" dezenas, "+unidade+ " unidades")
#
# if qtNumero == 1:
#     unidade = numeroStr[0:1]
#     print(numeroStr+" = "+unidade+ " unidades")



