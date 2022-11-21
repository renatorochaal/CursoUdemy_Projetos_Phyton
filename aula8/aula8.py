'''
exercicios proposto
imprimir nome, idade, imc(2 casas decimais), data de nascimento, ano atual.
exibir usando F-String com chaves
'''

nome = 'Renato'
idade = 24
altura = 1.77
peso = 96.25
ano = 2022
nascimento = ano - idade-1
imc = peso / (altura **2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
