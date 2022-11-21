try:
    a ={}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:  # Sempre sera executado 
    pass  # a = ' '

print('Bora continuar...')