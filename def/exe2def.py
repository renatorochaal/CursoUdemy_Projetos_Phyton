
def mestre(funcao, *args, **kwargs):  # Repassar os argumentos de uma função
    return funcao(*args, **kwargs)  # Passo oque receber


def fala_oi(nome):  # recebe apenas 1 argumento
    return f'oi {nome}'


def saudacao(nome, saudacao):  # 2 Argumentos
    return f'{saudacao} {nome}'

executando = mestre(fala_oi,'Renato')
executando2 = mestre(saudacao, 'Renato', saudacao = ' Boa tarde!')
print(executando)
print(executando2)