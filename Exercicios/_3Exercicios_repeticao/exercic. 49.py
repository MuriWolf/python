# Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

# Imprima no final a soma da série.

n1 = 1
n2 = 1

n1Lista = []
n2Lista = []

while n1 <= 9:
    print(f"{n1}/{n2} + ", end="")
    n1Lista.append(n1)
    n2Lista.append(n2)
    n1 = n1 + 1
    n2 = n2 + 2

print(f"{n1}/{n2} = {sum(n1Lista)}/{sum(n2Lista)}")