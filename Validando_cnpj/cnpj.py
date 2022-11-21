import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    if eh_sequencia(cnpj):
        # print('É uma sequencia')
        return False

    novo_cnpj = calcula_digito(cnpj=cnpj, digito = 1)
    novo_cnpj = calcula_digito(cnpj=cnpj, digito = 2)

    if novo_cnpj == cnpj:
        return True
    else:
       return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivo = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivo = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0

    for indice, regressivo in enumerate(regressivo):
        total += int(cnpj[indice] * regressivo)

    digito = 11 - (total % 11)
    digito = digito if digito <=  9 else 0

    return f'{novo_cnpj}{digito}'

def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)  # Remover tudo que não é número
