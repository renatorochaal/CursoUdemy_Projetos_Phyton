"""
For in em Python
iterando string com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':

#       continue#apagando letra 't'
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break#terminou o laço(não completa a frase
    else:
        nova_string += letra

print(nova_string)



"""

for n in range(5 , 10, 2):# usando - ele decrementa 
    print(n)


texto = 'Python'

for n, letra in enumerate(texto):#numerando as letras
    print(n, letra) #pegou cada iteração do laço

c = 0
while c < len(texto):
    print(texto[c])
    c += 1
"""
