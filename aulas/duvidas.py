"""
Enumerate - enumarar elementos da lista
"""
lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', ' Aline', 'joana'],
    ['Helena', 'Ed', 'Lu'],
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)


#enumerada = list(enumerate(lista))
#print(enumerada[1][1][2])#convertido em uma lista / typcast trocou o tipo de enumerate