# OPERADOR LOGICO OR (OU)

# OR - qualquer condicao verdadeira satisfaz a expressao, retornando True

entrada = input("[E] ou [e] para Entrar, [S] ou [s] para Sair: ")       # Entrada de dados com mensagem de orientacao, onde o usuario deve fornecer 'E' ou 'e' para entrar, e 'S' ou 's' para sair
senha_digitada = input("Digite a senha: ")                              # Entrada de dados com mensagem de orientacao, onde o usuario deve fornecer a senha de acesso ao sistema

senha_permitida = '123456'              # Senha que permite acesso amazenada em uma variavel

if (entrada == "E" or entrada == 'e') and senha_digitada == senha_permitida:    # Se a entrada e a senha estiverem corretas, imprime uma mensagem no terminal
    print("Entrou")
else:                                                                            # Se a entrada e/ou senha estiverem incorretos, imprime uma mensagem no terminal
    print("Saiu")