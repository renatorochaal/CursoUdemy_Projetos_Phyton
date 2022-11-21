""" Professor
def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)
"""

def soma():
    return 1+2

def mostrar(resultado):  # se tora a def soma
    return resultado()
somar = mostrar(soma)  # recebeu funçao soma
print(somar)
