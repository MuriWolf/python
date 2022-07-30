# O Departamento Estadual de Meteorologia
# lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas,
# bem como a média das temperaturas.

print("\ninforme as temperaturas em (Celsius) para descobir a (maior), (menor) e a (média).")
print("Digite (s) para encerrar.")

temperatura = 'e'
temperaturas = []

while temperatura != 's':
    temperatura = input("\nInforme a temperatura em Celsius: ")
    if temperatura != 's':
        temperaturas.append(int(temperatura))

maiorTemp = max(temperaturas)
menorTemp = min(temperaturas)
MediaTemp = sum(temperaturas) / len(temperaturas)

print(f'''

INFORMAÇÕES DAS TEMPERATURAS

Maior temperatura = {maiorTemp}°C

Menor temperatura = {menorTemp}°C

Média temperatura = {MediaTemp}°C
''')