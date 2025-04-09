# INTRODUÇÃO AO FOR/IN - LAÇO DE REPETILÇAO PARA COISAS FINITAS

"""
    WHILE - realiza uma quantidade indefinida de repetições (enquanto a sentença ser verdadeira)
    RANGE - realiza uma quantidade determindada de repetições (um intervalo pré-definido)
"""

texto = "Python"

# strings são iteráveis, então podemos usá-las diretamente para se iterar, não necessitando da função 'len()'
for letra in texto:     # para cada caractere na str 'texto'
    print(letra)        # imprimir o caractere no terminal
