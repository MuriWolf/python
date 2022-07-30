# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
tempMeses = []

# pedir as medias dos meses
print("\nDigite a média de temperatura de cada mês do ano (Em Celsius) .\n")
for i in range(12):
    tempMes = float(input(f"Digite a média do mês {i + 1} (C°): "))
    tempMeses.append(tempMes)

# descobir a media anual
mediaAnual = (sum(tempMeses)) / (len(tempMeses))
acimaMediaAnual = []

# descobir quais meses tem a media de temperatura maior q a media anual
for i in range(12):
    if tempMeses[i] > mediaAnual:
        acimaMediaAnual.append(meses[i])

# printar os meses quao a media maior que a media anual
print("\nMeses com a temperatura maior que a média anual:\n")
for i in range(len(acimaMediaAnual)):
    print(f"{i + 1} - {acimaMediaAnual[i]}, ", end='')