# Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

numeros = []
numero = 0

print("\nDigite a quantidade de numeros que voce quiser.\n")
while numero != -1:
    numero = float(input("Digite um numero (-1 para encerrar): "))
    if numero != -1:
        numeros.append(numero)

# Mostre a quantidade de valores que foram lidos;
QtdeNumeros = len(numeros)
print(f"\nQuantidade de numeros lidos:\n{QtdeNumeros}")

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print("\nvalores na ordem em que foram informados")
for i in range(QtdeNumeros):
    print(f"{numeros[i]}, ",end='')

# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
numeracao = 0
print("\n\nValores na ordem inversa à que foram informados")
for i in range(QtdeNumeros):
    numeracao = numeracao + (-1)
    print(numeros[numeracao])

# Calcule e mostre a soma dos valores;
print("\nSoma dos valores")
somaNumeros = sum(numeros)
print(somaNumeros)

# Calcule e mostre a média dos valores;
print("\nMédia dos valores")
mediaNumeros = somaNumeros / QtdeNumeros
print(mediaNumeros)

# Calcule e mostre a quantidade de valores acima da média calculada;
acimaMedia = []
for i in range(QtdeNumeros):
    if numeros[i] > mediaNumeros:
        acimaMedia.append(1)
print("\nQuantidade de valores acima da média calculada")
print(sum(acimaMedia))

# Calcule e mostre a quantidade de valores abaixo de sete;
menoresSete = []
for i in range(QtdeNumeros):
    if numeros[i] < 7:
        menoresSete.append(1)
print("\nQuantidade de valores abaixo de sete")
print(sum(menoresSete))

# Encerre o programa com uma mensagem;
print("\nPrograma encerrado. :)")