"""
Funções = *args **kwargs
"""


def funcao(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

funcao(1,2,3,4,5)
# lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista # *n empacotando o resto da lista
#print(*lista, sep='-')
