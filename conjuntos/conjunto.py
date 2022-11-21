"""
add (adiciona), update ( atualizar), clear, discard
union | (une)
intersection & ( todos os elementos presentes no dois setes
difference - (elementos apenas no set esquerda)
symmetric_difference ^ ( Elementos que estão nos dois sets, mas não em ambos
"""


s1 = {1, 2, 3, 4, 5}

for v in s1:
    print(v)

s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)
s1.update('Python')

print(s1)

print('----------')

l1 = [1, 2, 1, 1, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 'Renato', 'Andressa']
l1 = set(l1)
l1 = list(l1)

print(l1[-1])

print('-------------')
