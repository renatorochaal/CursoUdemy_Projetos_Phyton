'''
Conição IF, ELIF e ELSE - NEWAULA4
Operadores
== > >= < <= !=
'''

'''
if False:
    print("Verdadeiro. ")
elif False:#junção de IF e ELSE
    print("Agora é verdadeiro.")
elif True:
    print('Mais uma verdadeira')
else:
    print("Não é verdadeiro")
'''

nome = input('Qual seu nome? ')
idade = input("Qual sua idade? ")
idade = int(idade)

#Limite para pega empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} NÃO pode pega o empréstimo. ')