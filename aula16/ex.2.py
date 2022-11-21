"""
Operador ternário em Python
"""
idade = input('Qual sua idade? ')

if not idade.isnumeric():
     print('Você precisa digitar somente números')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Pode acessar' if maior else 'Não pode acessar.'
    print(msg)

'''
logger_user = False
msg = 'Usuário logado.' if logger_user else 'Usuário precisa logar.'

print(msg)
'''