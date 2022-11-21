#  mutável Lista, Dicionario,
# imutável: Tuplas, string, números,TRue,FAlse, None


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_cliente_1 = ['João']
clientes1 = lista_de_clientes(['Cássio', 'Renato', 'Andressa'], lista_cliente_1)
clientes2 = lista_de_clientes(['Renan','Caique', 'Mateus'])
clientes3 = lista_de_clientes(['Pedro'])

print(clientes1)
print(clientes2)
print(clientes3)