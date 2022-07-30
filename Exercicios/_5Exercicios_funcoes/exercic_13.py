# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘|‘.
# Esta função deve receber dois parâmetros, linhas e colunas,
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
# Se valores fora da faixa forem informados,
#  eles devem ser modificados para valores dentro da faixa de forma elegante.

def retangulo(larg, alt):
    # tratamento de dados (numeros maiores que 20 viram 20, numeros menores que 1 viram 1)
    if larg>20:
        larg=20
    if alt>20:
        alt=20

    print(f"\nRetangulo\nLargura = {larg}\nAltura = {alt}\n")

    # retangulo
    print("===" *larg)
    for i in range(alt):
        l = "|"
        print(f"{l} {l:>{larg*3 - 2}}")
    print("===" *larg)

while True:    
    print("\nTamanho do retangulo\n")
    larg = int(input("Digite a largura do retangulo (1-20): "))
    alt = int(input("Digite altura do retangulo (1-20): "))

    retangulo(abs(larg), abs(alt))

    denovo = str(input("\nDeseja usar o programa denovo? [s/n]: "))
    if denovo == "n":
        break

