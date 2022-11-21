'''
hora=input('Digíte um horário: ')
hora=float(hora)

if(hora>0 and hora <11):
    print('Bom dia! ')
if(hora>12 and hora<17):
    print('Boa tarde! ')
if(hora>18 and hora <23):
    print('Boa noite! ')
'''
horario=input('Digite um hórario entre (0-23): ')

if horario.isdigit():# Veirifica se é um numeral
    horario=int(horario)

    if horario < 0 or horario > 23: #Condição de erro
        print('Horário deve estar entre 0 e 23. ')
    else:
        if horario <= 11:#logica de condição
            print('Bom dia! ')
        elif horario<=17: #Condição de verificação entre if e else (elif)
            print('Boa Tarde! ')
        else:
            print('Boa noite!')
else:
    print("Por favor, digite um horário entre 0 e 23. ")