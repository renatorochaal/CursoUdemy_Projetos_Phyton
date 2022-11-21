
usuario = input("Nome de usuário: ")
senha = input("senha do usuário: ")

usuario_bd = "Renato"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema. ')
else:
    print('Usuário ou senha invalidos. ')