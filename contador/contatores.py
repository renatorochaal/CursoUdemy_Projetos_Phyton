"""
count - Itertools

from types import GeneratorType

#variavel = zip('Alo', 'Alo')

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))

print(isinstance(variavel, GeneratorType))
print(list(variavel))
"""

# um Contador que é um iterador

###
from itertools import count

contador = count
# contador = count()
#
# lista = ['Renato', 'Cássio', 'Mateus', 'Caique', 'Renan']
#
# lista = zip(contador, lista)
# print(list(lista))

# contador = count(start=9, step=-1)
#
#  print(next(contador))
#
# for valor in contador:
#     print(round(valor, 2))
#
#     if valor >= 10 or valor <= -10:
#         break
