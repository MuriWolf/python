# Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
# A entrada é dada em dois inteiros.
#
# Deve haver pelo menos duas funções:
# uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
# Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
# Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversaoHora(horas, minutos):
    if 25 > horas >= 12 and 60 > minutos > 1:
        print(f"\n{horas - 12}:{minutos} P.M")
    elif 12 > horas > 1 and 60 > minutos > 1:
        print(f"\n{horas}:{minutos} A.M")

    else:
        print("\nEsse horario não existe.")

denovo = ''
while denovo != 'n':
    horas = int(input("\nDigita a hora: "))
    minutos = int(input(f"\nDigite os minutos: {horas}:"))

    conversaoHora(horas, minutos)
    denovo = input("\n\nDeseja utiizar o programa denovo? [s/n]: ")