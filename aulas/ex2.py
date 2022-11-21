"""
split, Join, Enumerate em Python
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista
"""
lista = [ 'Renato', 'Cássio', 'Renan']

n1, n2, n3 = lista

print(n3)


'''
lista = ['Renato','João','Maria']
for indice, nome in enumerate(lista):# coloca valor nas string da lista
    print(indice, nome)
'''
"""
string = 'O Brasil é penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):# desempacotando a variavel
    print(indice, valor, lista[indice])
"""
"""
string = 'O Brasil é penta.'
string3 = 'e melhor do mundo'
lista = string.split(' ')#Gerou lista baseada por ' ' (espaço)
string2 = ' '.join(lista)#junta tudo por caracetere

print(string)
print(lista)
print(string2)
"""
"""
string = "O Brasil é o o o país do futebol, o Brasil é penta."
lista = string.split(' ') #Todas a palavras separadas em uma lista
lista_2 = string.split(',')#separou pela virgula

for valor in lista_2:
print(valor.strip().capitalize())# Remove espaços do inicio de do fim/Deixa a primeira letra maiscula
"""
"""
palara = ''
contagem = 0
for valor in lista: #Valor referente aos numeros da lista/ valor ligado a variavel
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem: #Checagem de quantas vezes a palavra aparece
        contagem = qtd_vezes # contador
        palara = valor

print(f'A palavra que apareceu mais vezes é {palara} ({contagem})x ')
"""
#    print(f'A palavra {valor} apareceu {lista.count(valor)}x va frase.')#fstring {} chaves executa a variavel
#    #print(lista)
#print(lista_2)
