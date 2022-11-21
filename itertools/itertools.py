"""

Combinations, Permutations e Product - Itertols
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produtp - Oredem importa e repete valores únicos

"""
from itertools import combinations, permutations, product


pessoas = ['Renato', 'Cássio', 'Mateus', 'Caique', 'Renan']

for grupo in product(pessoas, repeat=2):
    print(grupo)