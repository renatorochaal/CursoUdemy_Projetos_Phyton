"""
While / Else
contadores
acumuladores

"""
contador = 1
acumulador = 1

while contador <= 10:#quando for falsa executa o else
    print(contador, acumulador)
    if contador > 5:
        break #interrompe a ida ao else

    acumulador = acumulador + contador
    contador += 1
else:#quando expressão do while for falsa entra o else
    print('Cheguei no else.')
print("Isso sera executado")# como teve um break imprimiu isso
