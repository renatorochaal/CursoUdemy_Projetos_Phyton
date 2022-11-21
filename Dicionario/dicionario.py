"""
#  d1 = {'cahve1': 'valor da chave'}
d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1 ['nova_chave'] = 'Valor da nova chave'
print(d1)
"""

d1 = {
    'chave1': 'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla',
}

print('str' in d1)
print('str' in d1.keys())  # checa  por chaves
print('valor' in d1.values())  # Checa  por valores
print(len(d1))
print('-----------')

for v in d1.values():  # exibindo valores
    print(v)
print('-----------')
for k in d1.items():
    print(k[0], k[1])
print('------------')

for k, v in d1.items():
    print(k, v)
    