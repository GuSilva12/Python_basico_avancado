# OPERADOR LOGICO NOT

# Usado para invrter expressoes
#  not True = False
#  not False = True

senha = input("Senha: ")

if not senha:                       # Se NAO foi digitada uma senha, imprime uma mensagem de aviso
    print("Senha não digitada!")
elif senha == '123456':             # Se a senha digitada esta CORRETA, imprime 'acesso concedido'
    print("Acesso concedido.")
else:                               # Se a senha estiver INCORRETA, imprime "Senha incorreta!"
    print("Senha incorreta!")