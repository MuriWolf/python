# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário
#  e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

from datetime import datetime

now = datetime.now()
dia_atual, mes_atual, ano_atual  =now.day, now.month, now.year

# coleta de informacoes
nome, sobrenome = input("\nDigite seu nome completo: ").split(" ", 1)

print("\nDigite a data do seu nascimento.\n")
dia, mes, ano = int(input("Dia: ")), int(input("Mes: ")), int(input("Ano: "))
idade = ano_atual - ano

meses = ("Janeiro","Fevereiro","Março",
            "Abril","Maio","Junho",
            "Julho","Agosto","Setembro",
            "Outubro","Novembro","Dezembro")

# descobrir mes por extenso
for i in range(12):
    if mes == i+1:
        mes_extenso = meses[i]

# print das infromacoes   
print(f"\nOlá {nome}, aqui tem algumas informações sobre você.\n")
print(f"Nome: {nome}")
print(f"Data de nascimento: {dia}/{mes}/{ano}")
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")
print(f"Você tem {idade} anos")
print(f"Faltam {12 - (mes_atual - mes)} meses e {30 - (dia_atual - dia)} dias para o seu aniversario. (talvez não seja exatamente)")

if idade >= 18:
    print("Você é maior de idade")
    print("Você pode dirigir")
    print("Você pode consumir bebidas alcoolicas")
else:
    print("Você é menor de idade")
    print("Você não pode dirigir")
    print("Você não pode consumir bebidas alcoolicas")
    
#! adiconar mais informacoes dps :)