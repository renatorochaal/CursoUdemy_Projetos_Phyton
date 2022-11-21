import cnpj

cnpj1 = '04.252.011/0001-11'
#cnpj1 = '11.111.111/1111-11'
if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')