# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.


lista = [n for n in range (1, 21)]

cont = 0

while cont < len(lista):
    print(lista[cont])
    cont = cont + 1

print(lista)

# ou do jeito mais facil

for i in range(1,21):
    print(i)

print(list(range(1,21)))