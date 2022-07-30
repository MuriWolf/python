from random import shuffle

string = str(input("Digite uma palavra ou uma frase: "))

def embaralhar(palavra):
    a = list(palavra)
    shuffle(a)
    a = "".join(a)
    print(a)

embaralhar(string)
