# Verificação de CPF.
#  Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx 
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

numbers=["1","2","3","4","5","6","7","8","9","0"]

cpf = str(input("Digite seu CPF: "))

def validar_cpf(cpf):
    if len(cpf) != 11:
        print("\nCPF invalido.")

    else:
        invalido=False
        for i in range(11):
            if cpf[i] not in numbers:
                invalido=True
            else:
                pass

        if invalido == True:
            return "CPF invalido"                
        else:
            return "CPF valido"

print(validar_cpf(cpf))