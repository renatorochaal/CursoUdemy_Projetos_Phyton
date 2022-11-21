import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Cássio', 'Erick']}
v = copy.deepcopy(d1)  # copia correta importando biblioteca
#  v = d1.copy()  # Copia o dicionario

v[1] = 'Renato'
v['d'][0] = 'Andressa'
print(d1)
print(v)
