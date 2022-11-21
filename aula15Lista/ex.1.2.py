"""
for / else em python

"""
variavel = ['Renato Russo', 'Joãozinho', 'Maria']# ',' fora das aspas pula linha

for valor in variavel: #percorre a lista
    if valor.lower().startswith('j'):#Checando variavel que comeca com j / lower verifica tanto maiuscula e miniscula
        continue
    print(valor)#imprimiu por conta do continue
#else:
 #   print('Não existe uma palavra que começa com J.')

'''
comeca_com_j = False #Já tem valor booleano
for valor in variavel:
    if valor.lower().startswith('j'):#lower converte a string maiuscula
        comeca_com_j = True

if comeca_com_j : #Fazendo uma checagem
    print("Existe uma palavra que começa com J.", )
else:
    print("Não existe palavra que começa com J.", )
'''
#    if valor.startswith("J"): #checa se valor da string começa com determinada letra
 #       print('Começa com J', valor)
  #  else:
   #     print('Não começa com J', valor)


#    print(valor)
#    continue
#    print(valor) Pulou pois tem a palavra "continue"
#adicionando "break" ele para no primeiro valor

