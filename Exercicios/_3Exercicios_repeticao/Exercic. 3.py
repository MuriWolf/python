# Faça um programa que leia e valide as seguintes informações
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# nome
min = 3

nome = str(input("Digite seu nome: "))

while len(nome) < min:
    print("Digite um nome maior ou igual a 3 caracteres!")
    nome = str(input("Digite seu nome: "))


# idade
idade = int(input("Digite sua idade: "))

while (idade < 0) or (idade > 150):
    print("Digite um numero de 0 até 150!")
    idade = int(input("Digite sua idade: "))


#salario
salario = float(input("Informe seu salário: "))

while (salario < 0):
    print("Informe um numero maior que 0!")
    salario = int(input("Informe seu salário: "))


# sexo
sexo = str(input("Informe a inicial do seu sexo: "))

while (sexo != 'm') and (sexo != 'f'):
    print("Informe se seu sexo é m (masculino) ou f (feminino)!")
    sexo = str(input("Informe a inicial do seu sexo: "))


# estado
estado = str(input("Informe a inicial do seu estado civil: "))

while (estado != 's') and (estado != 'c') and (estado != 'v') and (estado != 'd'):
    print("Informe se seu estado civil é s (solteiro), c (casado), v (viuvo) ou  d (divorciado)!")
    estado = str(input("Informe a inicial do seu estado civil: "))