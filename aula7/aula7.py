"""
Variaveis
"""
nome = 'Renato'
idade = 24
altura = 1.77
e_maior =  idade > 18 #bool
peso = 96.5
imc = peso/(altura ** 2)

"""
print('Nome:',nome)
print('Idade:',idade)
print('Altura:',altura)
print('É maior',e_maior)
"""

print(nome, 'tem', idade, 'anos de idade e seu imc é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {}.'.format(nome, idade, imc))
'''pareametro variavel recebe leitura'''
