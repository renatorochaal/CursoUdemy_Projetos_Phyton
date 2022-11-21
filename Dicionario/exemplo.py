
cliente = {
    'clientes1': {
        'nome': 'Renato',
        'sobrenome': 'Russo',
    },
    'clientes2': {
        'nome': 'Andressa',
        'sobrenome': 'Rodrigues',
    },
    'clientes3': {
        'nome': 'Cássio',
        'sobrenome': 'Erick',
    },
}

for cliente_k, clitentes_v in cliente.items():  # responsavel pelo loop do dicionario 'clinte'
    print(f'Exibindo {cliente_k}')
    for dados_k, dados_v in clitentes_v.items():
        print(f'\t {dados_k} = {dados_v}')