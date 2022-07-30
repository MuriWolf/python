# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = str(input("Digite um nome: "))

tamanho =len(nome)

menos_um=nome
for i in range(tamanho):
    print(nome[:(i+1)])
