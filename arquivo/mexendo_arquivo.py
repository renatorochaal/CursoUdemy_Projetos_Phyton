


# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0, 0)
#     print(file.read())
# # file.write('Linha 1\n')
# # file.write('Linha 2\n')
# # file.write('Linha 3\n')
# #
# # file.seek(0, 0)  # posição do cursor
# #
# # print('Lendo Linhas:')
# # print(file.read())
# # print('##########')
# #
# # file.seek(0, 0)
# # print(file.readline(),end = '')
# # print(file.readline(), end= '')
# # print(file.readline(), end= '')
# # print('################')
# #
# # file.seek(0, 0)
# # for linha in file.readlines():
# #     print(linha, end= '')
# finally:
#     file.close()
#  with open('abc.txt', 'w+') as file:
#      file.write('Linha 1\n')
#      file.write('Linha 2\n')
#      file.write('Linha 3\n')
#
#      file.seek(0, 0)
#      print(file.read())

# with open('abc.txt', 'a+') as file:
#     file.write('Outra linha \n')
#     file.seek(0)
#     print(file.read())
import os
os.remove('abc.txt')