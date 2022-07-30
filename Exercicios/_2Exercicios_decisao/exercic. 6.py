# Faça um Programa que leia três números e mostre o maior deles.

numero = input("digite 3 numeros separados por um espaço cada: ").split(' ')

num1 = int(numero[0])
num2 = int(numero[1])
num3 = int(numero[2])

if num1 > num2 and num3:
    print(f"{num1} é o maior numero.")

elif num2 > num1 and num3:
    print(f"{num2} é o maior numero.")
elif num3 > num1 and num2:
    print(f"{num3} é o maior numero.")

else:
    print("Digite apenas 3 numeros!")

# another way to do / (this way is better)

lista = []

for i in range(0,3):
    n = int(input("Digite um numero: "))
    lista.append(n)
bigger = max(lista)

print(f"O maior numero entre esses: {lista} é o {bigger}.")