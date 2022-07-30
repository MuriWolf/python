# Leet spek generator.
# Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo.
# A própria palavra leet admite muitas variações, como l33t ou 1337. 
# O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, 
# sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
# Pesquise sobre as principais formas de traduzir as letras. 
# Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak

texto = str(input("Digite um texto ou palavra: "))
texto = texto.casefold()

texto = texto.replace("l", "1")
texto = texto.replace("i", "1")
texto = texto.replace("r", "2")
texto = texto.replace("z", "2")
texto = texto.replace("e", "3")
texto = texto.replace("a", "4")
texto = texto.replace("s", "5")
texto = texto.replace("b", "6")
texto = texto.replace("g", "9")
texto = texto.replace("o", "0")

print(texto)
