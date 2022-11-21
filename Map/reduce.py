from dados import produtos,pessoas,lista
from functools import reduce

# soma_lista = reduce(lambda ac, i: i + ac, lista, 0)  # execuando a lista e somando a cada laço
# print(soma_lista)

# soma_preco = reduce(lambda ac, p : p['preco'] + ac, produtos, 0)
# print(soma_preco/len(produtos))  # media de preços ( usando len que pega a quantidade total de itens)

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(round(soma_idade/len(pessoas)))