import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)  # cnpj recebe a função para remover os pontos

    if eh_sequencia(cnpj):
        return False

    novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)

def calcula_digito(cnpj, digito):
    for regressivo in REGRESSIVOS:
        print(regressivo)


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False
    print(sequencia)


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)  # diferente de 0 ate 9 substitui por nada

