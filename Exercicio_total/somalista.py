
lista1 = [1, 2, 3, 44, 5, 6, 7]
lista2 = [1, 2, 3, 4]

#somalista = zip(sum(lista1,lista2))

#print(somalista)
from itertools import zip_longest

listasoma = [x + y for x, y in zip(lista1, lista2)]
print(listasoma)
#for i in range(len(lista2)):
#   listasoma.append(lista1[i] + lista2[i])
#print(listasoma)

print('----------------------')

#  for i, _ in enumerate(lista2):  # _ p
#   listasoma.append(lista1[i] + lista2[i])
#  print(listasoma)

#  usando zip_longest

lista3 = [10, 2, 3, 4, 5]
lista4 = [12, 2, 3, 6, 50, 60, 70]

somalista = [ x+ y for x, y in zip_longest(lista3, lista4, fillvalue = 0)]
print(somalista)