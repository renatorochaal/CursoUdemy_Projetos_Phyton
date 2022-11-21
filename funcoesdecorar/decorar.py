# # def fala_oi():
# #     print('Oi')
# #
# # variavel = fala_oi
# #
# # print(type(variavel))
#
# def master(funcao):  # Funcção master
#     def slave(*args, **kwargs):
#         print('Agora estou decorada')# função escrava
#         funcao(*args, **kwargs)
#     return slave
#
# @master  # Decorador
# def fala_oi():
#     print('Oi')
#
# @master
# def outra_funcao(msg):
#     print(msg)
# # fala_oi = master(fala_oi)
# # fala_oi()
#
# outra_funcao('Olá, eu sou Renato')
from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado =  funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print((f'\nA função{funcao.__name__} levou {tempo:.2f}ms para executar'))
    return interna

@velocidade
def demora ():
    for i in range(100000):
        print(i, end='')
        # sleep(1)

demora()