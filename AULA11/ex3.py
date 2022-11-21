nome = input('Digite seu nome: ')
tamanho = len(nome) # len contador de string

if tamanho <=4:
    print('Seu nome é curto.')
elif tamanho <=6: # Condição de verificação entre if e else (elif), não precisa de :
    print('Seu nome é normal.')
else:
    print('Seu nome é grande. ')