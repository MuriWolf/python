# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
# com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá,
# testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento.
# O programa deverá receber um número indeterminado de entradas,
# cada uma contendo: um número de identificação do mouse o tipo de defeito:

# necessita da esfera;
# necessita de limpeza;
# a.necessita troca do cabo ou conector;
# a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
# Ao final o programa deverá emitir o seguinte relatório:

# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

# aviso
print('''
Oque cada numero significa:

1- necessita da esfera                  
2- necessita de limpeza               
3- necessita troca do cabo ou conector 
4- quebrado ou inutilizado   

0- encerra
''')

opcoes = [1,2,3,4,0]
condicao = 123 # numeoro aleatorio
contagemMouses = 0
situacao1 = []
situacao2 = []
situacao3 = []
situacao4 = []

while condicao != 0:
    if condicao == 0:
        break
    else:
        # input
        contagemMouses = contagemMouses + 1
        print(f"\nMouse {contagemMouses}")
        condicao = int(input("Digite a condicao do mouse [0-encerra]: "))

        # erro
        while condicao not in opcoes:
            print('''\nDigite apenas 1, 2, 3 ou 4:\n
1- necessita da esfera, 2- necessita de limpeza,
3- necessita troca do cabo ou conector, 4- quebrado ou inutilizado ''')
            print(f"\nMouse {contagemMouses}")
            condicao = int(input("Digite a condicao do mouse [0-encerra]: "))

        # adicionar na lista correta
        if condicao == 1:
            situacao1.append(1)
        elif condicao == 2:
            situacao2.append(1)
        elif condicao == 3:
            situacao3.append(1)
        elif condicao == 4:
            situacao4.append(1)

total = sum(situacao1) + sum(situacao2) + sum(situacao3) + sum(situacao4)

# printar as informações
print(f'''
Situação                        Quantidade              Percentual
1- necessita da esfera                  {sum(situacao1)}                     {int(((sum(situacao1)) / total) * 100)}%
2- necessita de limpeza                 {sum(situacao2)}                     {int(((sum(situacao2)) / total) * 100)}%
3- necessita troca do cabo ou conector  {sum(situacao3)}                     {int(((sum(situacao3)) / total) * 100)}%
4- quebrado ou inutilizado              {sum(situacao4)}                     {int(((sum(situacao4)) / total) * 100)}%
''')