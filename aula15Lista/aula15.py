"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, min, max
range
"""

secreto = input("Digite a palavra a ser adivinhada: ")

digitadas = []

chances = 3
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahh isso não vale, Digite apenas uma letra.')
        continue  # não sai do laço
    digitadas.append(letra)  # Vai guardian/adicionando letra na lista

    if letra in secreto:
        print(f'Parabéns, a letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'Que pena! a letra "{letra}" NÃO EXISTE na palavra secreta. ')
        digitadas.pop()  # Removendo a ultima letra digitada. Letra incorreta

    print(digitadas)

    # checa a letra e preenche na onde a letra esta
    secreto_aux = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_aux += letra_secreta
        else:
            secreto_aux += '*'

    if secreto_aux == secreto:
        print(f"PARABÉNS VOCÊ GANHOU!! A palavra era {secreto_aux}")
        break
    else:
        print(f'A palavra secreta esta assim : {secreto_aux}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances. ')
    print()
