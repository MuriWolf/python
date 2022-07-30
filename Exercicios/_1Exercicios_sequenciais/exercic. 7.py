# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.


# perguntar metros ou centimetros
metro_cent = (input("Digite 'm' se for digitar em metros ou 'c' se for digitar em centimetros: "))

while (metro_cent != 'm') and (metro_cent != 'c'):
    print("Digite 'm' ou 'c'!")
    metro_cent = (input("Digite 'm' se for digitar em metros ou 'c' se for digitar em centimetros: "))


area = float(input("Digite o tamanho da area do quadrado: "))

conta = area ** 2

conta_Final = conta * 2

# resultado
if metro_cent == 'm':
    print(f"{conta} metros (area normal) {conta_Final} metros (dobro da area).")

elif metro_cent == 'c':
    print(f"{conta} centimetros (area normal) {conta_Final} centimetros (dobro da area).")
