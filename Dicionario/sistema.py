print()
print("Sistema de perguntas interativo")
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2? ',
        'respostas': {
            'a': '4',
            'b': '3',
            'c': '6',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1? ',
        'respostas': {
            'a': '0',
            'b': '100',
            'c': '1.5',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4? ',
        'respostas': {
            'a': '20',
            'b': '1',
            'c': '2',
        },
        'resposta_certa': 'c',
    },

}
print()

respostas_certas = 0
for chave_p, chave_r in perguntas.items():  # for para exibir apenas as perguntas
    print(f'{chave_p}: {chave_r["pergunta"]}')

    print('Respostas: ')
    for respostas_r, respostas_v in chave_r['respostas'].items():  # respostas_r é opçãp 'a,b,c' e respostas_v sao os valor de 'a,b,c'
        print(f'[{respostas_r}]: {respostas_v}')


    respostas_usuario = input('Sua resposta: ')

    if respostas_usuario == chave_r['resposta_certa']:
        print('Parabéns!! Você acertou!!!! ')
        respostas_certas += 1
    else:
        print('Que pena! Você errou, mais sorte na próxima! ')
    print()

qtd_pergutas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_pergutas *100

print(f'Você acertou { respostas_certas} resposta.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')