# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numeros = []
print("\nQUANTIDADE DE VALORES")
quantNum = int(input("Informe quantos numeros deseja digitar: "))
while quantNum > 1000 or quantNum < 1:
    quantNum = int(input("\nInforme quantos numeros deseja digitar: "))

print("\nINPUT DOS VALORES")
for i in range(quantNum):
    num = int(input("Infome um numero: "))

    if num > 1000 or num < 1:
        while num > 1000 or num < 1:
            print("\nInfome apenas numeros acima de 1 e menores que 1000!")
            num = int(input("Infome um numero: "))
    numeros.append(num)

maxNumeros = max(numeros)
minNumeros = min(numeros)
somaNumeros = sum(numeros)

print("\nINFORMAÇÕES DOS VALORES")
print(f"O maior valor entre essa numeros é o ({maxNumeros})")
print(f"O menor valor entre essa numeros é o ({minNumeros})")
print(f"O valor da soma desses numeros é ({somaNumeros})")