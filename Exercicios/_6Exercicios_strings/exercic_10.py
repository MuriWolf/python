# Número por extenso.
# Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso

def numero_extenso(num):
    dicionario_numerico = {
            0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
            6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
            11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
            16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
            30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
            80: 'oitenta', 90: 'noventa', 100: "cento", 200: "duzentos",
            300: "trezentos", 400: "quatrocentos", 500: "quinhentos", 600: "seiscentos",
            700: "setecentos", 800: "oitocentos", 900: "novecentos", 1000: "mil"
            }       

    if num < 20 or num % 10 == 0 and num != 100:
        return dicionario_numerico.get(num)

    elif num == 100:
        return "cem"

    elif num > 20 and num < 100:
        unidade = num % 10
        decimal = num // 10 * 10
        numero_extenso = f"{dicionario_numerico.get(decimal)} e {dicionario_numerico.get(unidade)}"

        return numero_extenso

    elif num > 99 and num < 1000:
        centezimo = num // 100 * 100
        decimal = (num - centezimo) // 10 * 10
        unidade = num % 10
        numero_extenso = f"{dicionario_numerico.get(centezimo)} e {dicionario_numerico.get(decimal)} e {dicionario_numerico.get(unidade)}"
        return numero_extenso

    else:
        print()

while True:
    num = int(input("\nDigite um numero de 0 até 1000: "))

    print(f"\n{num} = {numero_extenso(num)}")

    again = str(input("\nDeseja usar o programa novamente? [s/n]: "))
    again = again.casefold()
    if again == "n":
        break
    elif again == "s":
        continue
    else:
        continue
