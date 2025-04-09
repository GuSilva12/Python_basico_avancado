# ITERANDO STRINGS COM WHILE - QUAL LETRA APARECEU MAIS VEZES

frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum"

i = 0   # definido um contador
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""

while i < len(frase):   # enqanto valor do contador menor que o tamanho da frase
    letra_atual = frase[i]                                          # acessando o elemento em um index da str
    qtd_atual = frase.count(letra_atual)        # contando a quantidade de cada letra acessada atavés do index

    # TRATANDO ESPAÇOS NA FRASE
    if letra_atual == ' ':  # se houver um espaço na frase
        i+=1        # soma 1 ao contador 'i'
        continue    # retoma o laço do início

    # VERIFICANDO QUAL LETRA APARECEU MAIS VEZES    
    if qtd_apareceu_mais_vezes < qtd_atual:         # se quant no contador 'qtd_apareceu_mais_vezes' menor que a ocorrência verificada ao vivo
        qtd_apareceu_mais_vezes = qtd_atual         # contador 'qtd_apareceu_mais_vezes' asume o valor de "qtd_apareceu_mais_vezes_atual"
        letra_apareceu_mais_vezes = letra_atual     # armazena a letra atual que é a que, no momento, possui a maior quantidade de ocorrencias

    i += 1      # soma 1 ao contador 'i'

print("A letra que apareceu mais vezes foi "f'"{letra_apareceu_mais_vezes}" que apareceu {qtd_apareceu_mais_vezes}x')