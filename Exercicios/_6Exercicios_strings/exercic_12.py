# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
# O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133  

while True:
    telefone = str(input("Digite o numero de telefone: "))
    if "-" in telefone:
        telefone.replace("-", "")

    if len(telefone) < 7 or len(telefone) > 8:
        novamente = str(input("Numero inválido. Deseja digitar novamente? [s/n]: "))
        if novamente != "n":
            break
        else:
            continue

    elif len(telefone) == 7:
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        telefone = "3" + telefone
        telefone_formatado = telefone[0:4] + "-" + telefone[4:8]
        print(f"\nTelefone corrigido sem formatação: {telefone}")
        print(f"Telefone corrigido com formatação: {telefone_formatado}")
    