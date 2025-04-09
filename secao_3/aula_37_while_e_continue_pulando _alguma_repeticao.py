# WHILE E CONTINUE - PULANDO ALGUMA REPETIÇÃO

"""
    REPETIÇÕES

    While - enquanto

    -> executa a ação enquanto a condição for verdadeira

    BREAK - para IMEDIATAMENTE o laço

    CONTINUE - volta ao começo do laço e continua o script
"""

contador = 0    # setando um contador para exemploficar o uso do contiune

while contador <= 100:    # enquanto o valor do contador for menor que 100, realiza as ações do bloco while
    contador += 1         # soma 1 ao contador

    if contador == 6:   # se contador atingir 6, realiza o comando do bloco if
        print("Não vou mostrar o 6")    # imprime uma mensagem no terminal
        continue                        # após realizadas as ações do bloco, volta ao início do bloco while e continua a ação do mesmo

    if contador >= 10 and contador <= 27:   # enquanto o contador for maior ou igual a 10 e menor ou igual 27, executa o bloco if
        print(f'não vou mostrar o {contador}')  # imprime uma mensagem no terminal, junto do valor atual do contador
        continue                        # após realizadas as ações do bloco, volta ao início do bloco while e continua a ação do mesmo

    print(contador)                     # imprime o valor atual do contador no terminal

    if contador == 40:  # se o contador chegar a 40, executar ação do bloco if
        break                           # para imediatamente de executar o laço while

print(contador)                         # imprime o valor atual e, consequentemente, final, do contador