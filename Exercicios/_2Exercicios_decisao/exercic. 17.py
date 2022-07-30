# Faça um Programa que peça um número correspondente a um determinado ano
# e em seguida informe se este ano é ou não bissexto.


print("\nDescubra se o ano que voce digitar será ou não um nao bissexto!")

ano = int(input("\nDigite algum ano: "))

if ano % 4 == 0:

    if ano % 100 == 0:

        if ano % 400 == 0:
            print("\nEsse ano é bissexto")

        else:
            print("\nEsse ano não é um ano bissexto")

    else:
        print("\nEsse ano é bissexto")

else:
    print("\nEsse ano não é um ano bissexto")