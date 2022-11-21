'''
Entrada de dados.
'''

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

ano_nascimento = 2022-int(idade)-1 #cast convertendo string em inteiro
print()
print (f'{nome} tem {idade} anos e nasceu em {ano_nascimento}. ')