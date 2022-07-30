# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F

nome = str(input("Digite um nome: "))

tamanho =len(nome)

menos_um=nome
for i in range(tamanho):
    print(menos_um, end="\n")
    menos_um= nome = nome[:-1]
    
menos_um=nome
for i in range(tamanho):
    print(menos_um, end="\n")
    menos_um= nome = nome[:-1]