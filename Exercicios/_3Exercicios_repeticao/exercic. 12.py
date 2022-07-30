# Desenvolva um gerador de tabuada,
# capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:
#
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

numTabuada = int(input("\nInforme qual tabuada voce deseja ver (1 a 10): "))
while numTabuada > 10 or numTabuada < 1:
    numTabuada = int(input("\nInforme qual tabuada voce deseja ver (1 a 10): "))

num = numTabuada
maxTabuada = num * 10
conta = 0
numVezes = 0

while maxTabuada > num - 1:
    maxTabuada = maxTabuada - num
    numVezes = numVezes + 1
    conta = num * numVezes
    print(f"\n{num} x {numVezes} = {conta}")