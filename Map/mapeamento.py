from dados import produtos, pessoas, lista
from itertools import groupby

#  nova_lista = map(lambda  x: x*2, lista)
# nova_lista = [ x*2 for x in lista]
# print(lista)
# print(list(nova_lista))

# for produto in produtos:
#     print(produto)

# ordena = lambda item: item['preco']
# produtos.sort(key=ordena)
# produtos_agrupados = groupby(produtos, ordena)
#
# for produto in produtos_agrupados:
#     print(produto)
# precos = map(lambda p: p['preco'], produtos) # traz somente os preços
#
# for preco in precos:
#     print(preco)

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2 )  # multiplica apenas os preços
#     return p
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.2)
    return p

nomes = map(aumenta_idade, pessoas)


for pessoa in nomes:
    print(pessoa)