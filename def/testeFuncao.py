"""
Exercicio teste com def, *args e **kwargs
"""

def funcao(*args, **kwargs):
    print(args, type(lista))
    print(kwargs)

lista = []

lista = input("Digite os valores da lista: ")
nome = input("Digite alguns nomes: ")

funcao(lista, nome)