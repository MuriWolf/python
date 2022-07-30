# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.


value1 = int(input("\nType the first value: "))
value2 = int(input("Type the second value: "))

print("\nWhat do you want to do?")
option = int(input('1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n'))

if option == 1:
    result = value1 + value2
    print(f"\nResult = {result}")
    print("\nEven or Odd:")
    if result % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    print("\nPositive or Negative:")
    if result > 0:
        print("Positive number")
    else:
        print("Negative number")

    int_result = int(result)
    what_type = result != int_result
    print("\nInterger or float")
    if what_type == True:
        print("Float")
    else:
        print("Integer")

elif option == 2:
    result = value1 - value2
    print(f"Result = {result}")
    print("\nEven or Odd:")
    if result % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    print("\nPositive or Negative:")
    if result > 0:
        print("Positive number")
    else:
        print("Negative number")

    int_result = int(result)
    what_type = result != int_result
    print("\nInterger or float")
    if what_type == True:
        print("Float")
    else:
        print("Integer")


elif option == 3:
    result = value1 * value2
    print(f"Result = {result}")
    print("\nEven or Odd:")
    if result % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    print("\nPositive or Negative:")
    if result > 0:
        print("Positive number")
    else:
        print("Negative number")

    int_result = int(result)
    what_type = result != int_result
    print("\nInterger or float")
    if what_type == True:
        print("Float")
    else:
        print("Integer")


elif option == 4:
    result = value1 / value2
    print(f"\nResult = {result}")
    print("\nEven or Odd:")
    if result % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    print("\npositivo ou negativo:")
    if result > 0:
        print("Positive number")
    else:
        print("Negative number")

    int_result = int(result)
    what_type = result != int_result
    print("\nInterger or float")
    if what_type == True:
        print("Float")
    else:
        print("Integer")
