# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro,

# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
# sua altura e seu peso.
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.

# Ao encerrar o programa também deve ser informados os códigos e valores
# do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes

QtVezes = 0

codigo = 1 # numero aleatorio
pesos = []
alturas = []

alto = [0,0,0]
baixo = [999,999,999]
gordo = [0,0,0]
magro = [999,999,999]

while codigo != 0:
    print("\nDigite 0 na area do código para encerrar o programa.")
    codigo = int(input("Informe seu código: "))
    if codigo != 0:
        peso = float(input("\nDigite seu peso: "))
        altura = float(input("\nDigite sua altura: "))

        QtVezes = QtVezes + 1
        pesos.append(peso)
        alturas.append(altura)
        if peso > gordo[1]:
            del gordo[0]
            gordo.insert(0, codigo)
            del gordo[1]
            gordo.insert(1, peso)
            del gordo[2]
            gordo.insert(2, altura)

        if peso < magro[1]:
            del magro[0]
            magro.insert(0, codigo)
            del magro[1]
            magro.insert(1, peso)
            del magro[2]
            magro.insert(2, altura)

        if altura > alto[2]:
            del alto[0]
            alto.insert(0, codigo)
            del alto[1]
            alto.insert(1, peso)
            del alto[2]
            alto.insert(2, altura)

        if altura < baixo[2]:
            del baixo[0]
            baixo.insert(0, codigo)
            del baixo[1]
            baixo.insert(1, peso)
            del baixo[2]
            baixo.insert(2, altura)

    elif codigo == 0:
        pass

media_pesos = sum(pesos) / QtVezes
media_alturas = sum(alturas) / QtVezes

print(f'''
-------------------------------
Valores do cliente mais gordo:
Codigo:  {gordo[0]}
peso:    {gordo[1]} kilos
altura:  {gordo[2]} metros 

Valores do cliente mais magro:
Codigo:  {magro[0]}
peso:    {magro[1]} kilos
altura:  {magro[2]} metros 

Valores do cliente mais alto:
Codigo:  {alto[0]}
peso:    {alto[1]} kilos
altura:  {alto[2]} metros 

Valores do cliente mais baixo:
Codigo:  {baixo[0]}
peso:    {baixo[1]} kilos
altura:  {baixo[2]} metros 
-------------------------------
Media de pesos:
{media_pesos} kilos

Media de alturas:
{media_alturas} metros
-------------------------------
''')