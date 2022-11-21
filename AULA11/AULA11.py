num1 = input('Digite um número: ')
'''
if num1.isdigit(): #Verifica se é um numeral
    num1 = int(num1)
    if (num1 % 2 == 0):
        print('O número é par ')
    else:
        print('O número é impar')

else:
    print('Isso não é um número inteiro')
'''
if not num1.isdigit():
    print('Isso não é um número inteiro. ')
else:
    num1=int(num1)
    if not num1%2 == 0:
        print('Numero é ímpar ')
    else:
        print('Número é par ')