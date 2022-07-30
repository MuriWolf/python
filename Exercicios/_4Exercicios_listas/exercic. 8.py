# Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

alturas = []
idades = []

for i in range(5):
    print(f"\nPessoa {i + 1}")
    idade = int(input("Digite sua idade: "))
    idades.append(idade)

    altura = float(input("Digite sua altura: "))
    alturas.append(altura)

contagem = -1
print("\nIDADES: ")
for i in range(len(idades)):
    print(idades[contagem])
    contagem = contagem - 1

contagem = -1
print("\nALTURAS: ")
for i in range(len(alturas)):
    print(alturas[contagem])
    contagem = contagem - 1