"""
Lista de números inteiros
listas internas tem o tamanho de 10 elementos
Listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercicio

--> Crie uma funcção que encontra o primeiro duplicado. Considerando o segundo número como duplicação
    Requisitos:
                A ordem dos numeros duplicados é considerada a partir da segunda ocorrencia  (o número duplicado em si)
                exemplo [ 1, 2, 3, ->3-<, 2, 1] 3
                se nãp econtrar na lista retone -1
"""

lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

]


def encontrar_primeiro_duplicado(param_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicato = -1  # -1 caso não ache nada

    for numero in param_lista_de_inteiros:  # for na lista que recebeu
        if numero in numeros_checados:  # encontrar duplicato
            primeiro_duplicato = numero
            break

        numeros_checados.add(numero)  # cada numero que passar aqui joga em set()

    return primeiro_duplicato


for lista_de_inteiros in lista_de_lista_de_inteiros:
    print(lista_de_inteiros, encontrar_primeiro_duplicado(lista_de_inteiros))  # Passando lista de inteiros na função
