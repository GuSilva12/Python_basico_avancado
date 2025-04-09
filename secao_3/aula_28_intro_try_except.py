# INTRODUÇÃO AO TRY/EXCEPT

"""
    try -> tenta executar o código
    except -> ocorreu algum erro ao tentar executar (exceto erro de código)

    EXEMPLIFICANDO COM O TRATAMENTO DE ENTRADA DO USUÁRIO
"""


numero_str = input("Vou dobrar o número que vc digitar: ")      # Solicita que o usuário digite um número para ser dobrado

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DESVIO CONDICIONAL -> checa a lógicado código, sem tratara exceção


"""

if numero_str.isdigit():            # Se o valor inserido for composto APENAS por números, retorna True e acessa o(s) comando(s) do bloco de código 'if'

    numero_float = float(numero_str)                                # Converte o numero em float e armazena em uma nova variável
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")      # Imprime no terminal uma mensagem junto do valor retornado daoperação realizada com a input 'numero'

else:                               # Se o valor inserido NÃO for composto apenas por números, retorna False e acessa o(s) comando(s) do bloco de código 'else'

    print("Isso não é um número")                                   # Imprime uma mensagem no terminal

"""



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TRY
try:        # Tenta executar o código dentro do bloco 'try'

    print(f"STR: {numero_str}")                                     # Imprimindo o valor digitado em seu tipo inicial (str)
    numero_float = float(numero_str)                                # Converte o numero em float e armazena em uma nova variável
    print(f"FLOAT: {numero_float}")                                 # Imprimindo o valor digitado, agora convertido para float
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")      # Imprime no terminal uma mensagem junto do valor retornado daoperação realizada com a input 'numero'

except:     # Se ocorre algum erro (exceção) dentro do bloco 'try', pula imediatamente para o exception
    
    print("Isso não é um número")                                   # Imprime uma mensagem no terminal
