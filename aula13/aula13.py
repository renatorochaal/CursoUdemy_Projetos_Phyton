"""
While em python
utilizdo para realizar ações enquanto uma condição for verdadeira
Requisitos: Entender condições e operações
"""
"""
while True:
    nome = input("Qual o seu nome ? ")
    print(f'Ola {nome}! ')

x = 0
  while x < 100:
    print(x)
    x = x + 1

print('Acabou!')

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1
print(' Acabou! ')

x = 0

while x < 10:
    y = 0#zerada a incio de repetição de X
    while y < 5:
        print(f'({x},{y})')
        y += 1

 #   print(x)
    x += 1

print('Acabou! ')
"""
while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input("Deseja sair ? [s]im ou [n]ão: ")

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():#Verifica se opque foi digitado é um numero.
        print('Você precida digitar um número. ')
        continue

    num1 = int(num1)#conversão de string em inteiro.
    num2 = int(num2)
    # + - / *
    if operador == '+':
        print(num2 + num2)
    elif operador == '-':#chegando mais de um "se"
        print(num1 - num2)
    elif operador == '/':#chegando um se sem erro
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador inválido! ')
