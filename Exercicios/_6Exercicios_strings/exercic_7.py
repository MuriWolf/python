# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

#ideia
frase = input("\nDigite uma frase: ")
frase = frase.casefold()

vogais = ["a","e","i","o","u"]

espaco = 0
vogal = 0

for i in range(len(frase)):
    if frase[i] == " ":
        espaco += 1
    elif frase[i] in vogais:
        vogal += 1

print(f"\nEspaços nessa frase: {espaco}") 
print(f"\nVogais nessa frase: {vogal}")
