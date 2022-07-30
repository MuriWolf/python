def welcome():
    print("\nWelcome to the calculator!\nMade by: MuriWolf.")

def again():
    calc_again = input("\nDo you want to calculate again?\nPlease type Y for YES or N for NO: ")
    if calc_again == 'Y' or calc_again == 'y':
        calculate()

    if calc_again == 'N' or calc_again == 'n':
        print("\nSee you later!")
        pass

# ====================================================================================================================
def calculate():
    welcome()
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division

Answer here: ''')
    while operation != '+' and operation != '+' and operation != '*' and operation != '/':
        operation = input('''
Answer here: ''')

    numero_um = int(input("Digite o primeiro numero: "))
    numero_dois = int(input("Digite o segundo numero: "))

    if operation == '+':
        print('{} + {} = '.format(numero_um, numero_dois))
        print(numero_um + numero_dois)

    elif operation == '-':
        print('{} - {} = '.format(numero_um, numero_dois))
        print(numero_um - numero_dois)

    elif operation == '*':
        print('{} * {} = '.format(numero_um, numero_dois))
        print(numero_um * numero_dois)

    elif operation == '/':
        print('{} / {} = '.format(numero_um, numero_dois))
        print(numero_um / numero_dois)


    again()
# ================================================================================================================

# THE START
welcome()
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division

Answer here: ''')

while operation != '+' and operation != '-' and operation != '*' and operation != '/':
    operation = input('''
Answer here: ''')

numero_um = int(input("Digite o primeiro numero: "))
numero_dois = int(input("Digite o segundo numero: "))



if operation == '+':
    print('{} + {} = '.format(numero_um, numero_dois))
    print(numero_um + numero_dois)

elif operation == '-':
    print('{} - {} = ' .format(numero_um, numero_dois))
    print(numero_um - numero_dois)

elif operation == '*':
    print('{} * {} = '.format(numero_um, numero_dois))
    print(numero_um * numero_dois)

elif operation == '/':
    print('{} / {} = '.format(numero_um, numero_dois))
    print(numero_um / numero_dois)


again()