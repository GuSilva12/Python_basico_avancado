# SPLIT, JOIN E STRIP SÃO MÉTODOS ÚTEIS PARA USAR EM STR

"""
    split - divide uma string,  usando, por padrão, o espaço entre cada palavra como parâmetro

        - Pode ser passado um parâmetro diferente do espaço para se fazer a separação da str, como a vírgula(",")

    join - une uma string

    strip - remove espaçoes de frases - remove outros elementos, se especificado quais. Geralomente retorna uma lista

        - rstrip: remove os espaçamentos da direita
        - lstrip: remove os espaçamentos da esquerda
"""

frase = "Olha só que, coisa interessante"

# DIVIDINDO UMA STR COM SPLIT
lista_frases = frase.split()      # ['Olha', 'só', 'que,', 'coisa', 'interessante']
print(lista_frases)
print()

lista_palavras_virgula = frase.split(',')      # ['Olha só que', ' coisa interessante']
print(lista_palavras_virgula)
print()


# STRIP
for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())
print()


# JOIN
frases_unidas = ''.join("abc")