"""
Compreensão de dicionario

"""



#d1 = {x: y*2 for x, y in lista}
#d1 = {x: y.upper() for x, y in lista}

#print(d1)
print('------------------')

d1 = {f'chave_{x}':x ** 2 for x in range(5)}
print(d1)