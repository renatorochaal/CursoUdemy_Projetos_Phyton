def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
while True:
    numero = converte_numero( input("Digite um número: "))

    if numero is None:
        print('Erro: Isso não é um numero.')
    else:
        print(numero*2)
    # if numero is not None:
    #     print(numero * 5)
    # else:
    #     print('Isso não é número.')