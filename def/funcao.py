"""
varialvel = 'valor'


def func():
    print(varialvel)


def func2():
    global varialvel # muda o valor da varialvel em um todo
    varialvel = 'Outro valor'
    print(varialvel)


func()
func2()
print(varialvel)
"""


"""
variavel = 'valor'


def func():
    print(variavel)
    

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg
    
func()
outra_Variavel = func2(arg = variavel)

print(outra variavel
"""


def func():
    outra_variavel = 'to com sono'
    return outra_variavel


def func2(arg):  # outra_varivel é setada pois func2() recebeu 'var'
    print(arg)


var = func()
func2(var)
