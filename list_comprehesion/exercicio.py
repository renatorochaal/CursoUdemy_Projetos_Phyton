
string = '0123456789012345678901234567890123456789012345678901234567890123456789'

n= 10
contadores = [i for i in range(0, len(string), n)]  # conador inicail

tuplas = [(i, i + n) for i in range(0, len(string), n)]  # contador incial ate final

lista = [string[i:i + n] for i in range(0, len(string), n)]  # separar a strin pulando de n em n (10 em )

raw = [f'string [{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)


print(contadores)
print('----------------------------')
print(tuplas)
print('----------------------------')
print(lista)
print('----------------------------')
print(raw)
print('----------------------------')
print(retorno)


