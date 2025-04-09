# FORMATACAO BASICA DE STRINGS COM F-STRINGS

"""
s - string

d - int

f - float

.<número de dígitos>f - definir quantidade de casas decimais de um float

x ou X - hexadecimal

(Caractere)(><^)(Quantidade)

> - esquerda

< - direita

^ - centro

Sinal - + ou -

Ex.: 0>-100,.1f

Conversion flags - !r !s !a
"""

variavel  = 'ABC'
print(f'{variavel}')                # imprimindo  a variavel no terminal
print(f'{variavel: >10}.')          # imprimindo a variavel no terminal, dessa vez, preenchendo 10 caracteres (nesse caso, espaço) à esquerda (incluindo a propria string)
print(f'{variavel:.<10}.')          # imprimindo a variavel no terminal, dessa vez, preenchendo 10 caracteres (nesse caso, ponto final) à direita (incluindo a propria string)
print(f'{variavel:.^10}.')          # imprimindo a variavel no terminal, dessa vez, preenchendo 10 caracteres (nesse caso, ponto final) ao centro (incluindo a propria string)
print(f'{variavel:!<10}.')          # imprimindo a variavel no terminal, dessa vez, preenchendo 10 caracteres (nesse caso, exclamação) à direita (incluindo a propria string)

print(f"O hexadecimal de 1500 é {1500:08X}")    # valor pasado para ser impresso é formatado de maneira que possua 8 casas