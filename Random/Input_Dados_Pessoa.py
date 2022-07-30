denovo = 'abc'
dados = []
contagem = 0

while denovo != 'n':
     nome = input("Digite seu nome: ")
     idade = int(input("Digite sua idade: "))
     liguagem = input("Digite qual linguagem voce programa: ")

     dados_pessoa = {'Nome' : nome,
          'Idade' : idade,
          'Linguagem' : liguagem,
          }
     dados.append(dados_pessoa)

     denovo = input("\nOutra pessoa irá usar? [s/n]: ")
     if denovo == 'n':
          for i in range(len(dados)):
               print(f"\nInformações Pessoa {contagem + 1}")
               print(dados[contagem])
               contagem = contagem + 1