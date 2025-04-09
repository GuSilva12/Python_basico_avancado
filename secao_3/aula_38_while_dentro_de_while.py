# WHILE + WHILE - laços internos

# declaração de variáveis
qtd_linhas = 5          # definindo uma quantidade de linhas para ser atingido
qtd_colunas = 5         # definindo uma quantidade de colunas para ser atingido

linha = 1               # setando o valor inicial de linhas

# laço while n°1
while linha <= qtd_linhas:          # enquanto linha for menor ou igual a quantidade de linhas definida, executa a ação do laço while n°1
    coluna = 1          # setando o valor inicial de colunas
    # laço while n°2
    while coluna <= qtd_colunas:    # enquanto coluna for menor ou igual a quantidade de colunas definidom executa a ação do laço while n°2
        print(f"{linha=}, {coluna=}")   # imprimindo os valores das linhas e colunas no terminal
        coluna += 1     # somando 1 à quantidade de colunas

    linha += 1          # somando 1 à quantdade de linhas

print("Acabou") # imprimindo uma mensagem de encerramento do programa no terminal