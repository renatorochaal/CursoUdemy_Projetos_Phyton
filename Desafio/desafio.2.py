"""
CPF = 023.532.811-17
_____________________
 True:
    cpf = '16899535009'
    novo_cpf = cpf[:9]  # ou [:-2]
    reverso = 10  # valores reverso
    total = 0

    for index in range(19):  # contator reverso
      if index > 8:  # a partir da 8 casa começa do 0 de novo
           index -= 9  # index = index -

        total += int(novo_cpf[index] * reverso)  # novo_cpf acessa os numeors do cpf

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
                total = 0
                novo_cpf += str(d)
        if cpf == novo_cpf:
             print('Válido')
        else:
            print('Inválido')
"""

while True:
    cpf = input("Digite um CPF: ")
    novo_cpf = cpf[:-2]  # elimando a ultima casa
    reverso = 10
    total = 0

    for index in range(19):  # contador reverso
        if index > 8:  # conta ate 8 casas, apos isso começa a contar de novo
            index -= 9  # dimunui 9 do index

        total += int(novo_cpf[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0  # para inicar a conta mais uma vez no indez partindo de 11
            novo_cpf += str(d)
    if cpf == novo_cpf:
        print(" Válido!")
    else:
        print(" Inválido")
