"""
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)

a = lambda x, y: x * y  # função anonima
"""

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1])
print(lista)

print(sorted(lista, key=lambda i: i[0], reverse=True))

print(lista)
"""
def func(item):
    return item[1]  # chave de ordenação pelo preço do produto


lista.sort(key=func, reverse=True)
print(lista)
"""