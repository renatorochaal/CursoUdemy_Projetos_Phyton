#        Índice
#        0123456789......................33
frase = 'O rato roeu a roupa do rei de roma'#iterar passando por cada letra da string
tamanho_frase = len(frase)
contador = 0
nova_string = ''

#iteração
input_do_usuario = input("Qual letra deseja colocar maiúscula: ")
while contador < tamanho_frase:
    letra=frase[contador]
    if letra == input_do_usuario:#capitura letra
        nova_string += letra.upper()#função para letra maiúscula
    else:
        nova_string += letra
    contador += 1
print(nova_string)

"""
while contador<tamanho_frase:
#    print(frase[contador], contador)
    nova_string += frase[contador]#copiei os elementos da string
   # print(nova_string) mostrando a string sendo formada
    contador += 1

print(nova_string)
"""