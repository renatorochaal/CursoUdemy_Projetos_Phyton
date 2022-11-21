"""
Formatando valores com modificadores

:s - Texto (string)
:d = Inteiros (int)
:f - Números de ponto flutuantes (float)
:. (número) f - Quantidade de casas decimais (float)
: (caractere) (> ou < ou ^) Quantidade ( tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print(f'{divisao:.2f}')# Mostrando casa decimais
print('{:.2f}'.format(divisao))# Mostrando casa decimais

nome = 'Renato Russo'
print(f'{nome:s}')
"""
"""
num1 = 1
print(f'{num1:0>10}')
print(f'{num1:0<10}')#comanod q adiciona um numeral a frente, atras ou centrliza um valor
print(f'{num1:0^10}')#adicona cada decimal no numero.
num2=115
print(f'{num2:0>10.2f}')#usando formatação para transforma em float
nome='Renato Russo'
sobrenome = 'Rocha Alcantara'
print(len(nome))
#print(f'{nome:#^50}')
nome_formatado = '{0:$^50}{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)
"""