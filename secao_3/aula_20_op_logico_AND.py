# OPERADOR LOGICO 'AND'

# AND = E
# OR = OU
# NOT = NAO

# AND - Todas as condicoes precisam ser verdadeiras
# Se QUALQUER valor for considerado falso, toda a expressao e falsa (False)

# Sao considerados falsy
# 0  00.0     ''      False
# 
# None -> representa um não-valor


entrada = input("[E]ntrar ou [S]air: ")                 # Entrada de dados com mensagem de orientacao, onde o usuario deve fornecer 'E' para entrar ou 'S' para sair
senha_digitada = input("Digitr a senha: ")              # Entrada de dados com mensagem de orientacao, onde o usuario deve fornecer a senha de acesso ao sistema

senha_permitida  ='123456'                              # Senha que permite acesso amazenada em uma variavel

if entrada == 'E' and senha_digitada == senha_permitida:        # Se a entrada e a senha estiverem corretas, imprime uma mensagem no terminal
    print("Entrou")
else:                                                           # Se a entrada e/ou senha estiverem incorretos, imprime uma mensagem no terminal
    print("Saiu")


print(True and True)    # retorna True
print(True and True and True)    # retorna True
print(True and False and True)    # retorna False assim que False for constatado, e nao checara mais nada, pois ja deitou de satisfazer a condicao
print(True and True and False)    # retorna False
print(bool(0.0))    # retorna False
print(bool(0))    # retorna False
print(bool(""))    # retorna False
print(bool(''))    # retorna False
