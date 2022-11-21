"""
Zip - unindo iteráveis]
Zip_longest - itertools

"""


from  itertools import zip_longest,count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(indice, cidades, estados)

#for valor in cidades_estados:
   # print(valor)

#estados_cidades = zip(estados, cidades)

#print(dict(estados_cidades))

# print('----------------------------')

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)

# cidades_e_estados = zip_longest(
#     indice,
#    estados,
#    cidades,
#    fillvalue='Estado'
# )

