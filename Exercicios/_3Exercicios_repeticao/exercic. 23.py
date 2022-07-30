# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.

# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

# Numeros primos de 1 até 100:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 e 97

numero = int(input("\nInforme até qual numero voce deseja descobrir onde existe primos: "))

primos = []
divisoes = 0
primeiroprimo = 2

for i in range(numero + 1):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 9 != 0:
        primos.append(i)
        divisoes += 1
    else:
        divisoes += 1

del primos[0]
primos.insert(0,2)
primos.insert(1,3)
primos.insert(2,5)
primos.insert(3,7)

# arrumarrrrrrrrr
# if numero < 3:
#     print(f"Numeros de primos {primos[0]}")
#
# elif numero < 4:
#     print(f"Numeros de primos {primos[0],[1]}")
#
# elif numero < 6:
#     print(f"Numeros de primos {primos[0][1][2]}")
#
# elif numero < 8:
#     print(f"Numeros de primos {primos[0],[1],[2],[3]}")

# else:
#     print(f"Numeros de primos {primos}")
#     # arrumar o numero de divisoes!!!!!
#     print(f"Numeros de divisões: {divisoes}")
