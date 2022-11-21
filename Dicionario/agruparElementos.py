"""
Agrupando Dicionarios

"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Renato', 'nota': 'A'},
    {'nome': 'Cássio', 'nota': 'B'},
    {'nome': 'Mateus', 'nota': 'C'},
    {'nome': 'Renan', 'nota': 'A'},
    {'nome': 'Gabrielly', 'nota': 'D'},
    {'nome': 'Anna Luiza', 'nota': 'E'},
    {'nome': 'Paulo Henrique', 'nota': 'F'},
    {'nome': 'Iury', 'nota': 'B'},
    {'nome': 'Laura', 'nota': 'C'},
    {'nome': 'Thais', 'nota': 'F'},
]


ordena = lambda item: item['nota']  # Ordena o dicionario pelas notas com uma função
alunos.sort(key=ordena)  # Manipula o dicionario original
alunos_agrupados = groupby(alunos, ordena)

#    notas        alunos
for agrupamento, valores_agrupados in alunos_agrupados:  # tuplas com dois valores
    va1, va2 = tee(valores_agrupados)  # cria uma copia do iterados para não esgotar o mesmo

    print(f'Agrupamento: {agrupamento}')  # tuplas agrupadas com as notas com intertools

    for aluno in va1:  # iterando com o dicionario
        print(f'\t{aluno}')

    quantidade = len(list(va2))  # como era um obajeto ouve a conversão para lista
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()


print('------------------------')

# for agrupamento, valores_agrupados in alunos_agrupados:  # tuplas com dois valores
#     print(f'Agrupamento: {agrupamento}') # separa por notas
#     for aluno in valores_agrupados:  # traz o dicionario
#         print(aluno)
#     print()
# for aluno in alunos:  # for de exibição
#     print(aluno)

# for aluno in alunos:
#     print(aluno)
