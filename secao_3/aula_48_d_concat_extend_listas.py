"""
    Conhecimentos reutilizáveis - índices e fatiamento

    Métodos úteis:

        append - adiciona um item ao final
        insert - adiciona um item no indice escolhido
        pop - remove do final ou do indice escolhido
        del - apaga um indice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# CONCATENANDO LISTAS COM +
lista_c = lista_a + lista_b
print(lista_c)

# EXTEND - extendendo uma lista
lista_a.extend(lista_b)     # extendendo lista_a para armazenar também os valores da lista_b
print(lista_a)