# pedir a medida de temperatura
ask = (input("Digite f para selecionar Fahrenheit, digite c para selecionar Celsius: "))

# se for fahrenheit
if ask == "f":
    fahAsk = int(input("Digite o valor em Fahrenheit: "))
    fahConta1 = fahAsk - 32
    fahConta2 = fahConta1 / 1.8
    intFah = int(fahConta2)
    print(f"{intFah} graus Celsius.")

# se for celsius
elif ask == "c":
    celAsk = int(input("Digite o valor em Celsius: "))
    celConta1 = celAsk + 32
    celConta2 = celConta1 * 1.8
    intCel = int(celConta2)
    print(f"{intCel} graus Fahrenheit.")

# se digitar errado
else:
    print("Digite os valores corretos para funcionar!")