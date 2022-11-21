
# def divide(n1, n2):
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print('Log: ', error)
#         raise  # capturando exeção
#
# try:
#     print(divide(2,0))
# except ZeroDivisionError as error:
#     print(error)

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("N2 não pode ser 0.")
    return n1/n2

try:
    print(divide(2,0))
except ValueError as error:
    print('Você esta tentando dividir por 0.')
    print('Log: ', error)