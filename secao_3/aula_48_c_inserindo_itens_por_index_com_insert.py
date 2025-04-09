# INSERINDO ITENS EM QUALQUER INDICE DA LISTA COM INSERT

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

#         0   1   2   3
lista = [10, 20, 30, 40]
lista_para_usar_clear = [10, 20, 30, 40, 50, 60, 70, 80, 90]


# APPEND -adicionando um item ao final da lista
lista.append('Luiz')
print(lista, lista.pop())   # imprimindo a lista, seguida do elemento que fora removido desta
lista.append(1233)

# DEL - apagando um indice da lista
del lista[-1]   # apagando o último index da lista
print(lista)

# CLEAR - limpando uma lista
lista_para_usar_clear.clear()
print(lista_para_usar_clear)

# INSERT - adicionando um item no índice escolhido (<index>, <valor>)
lista.insert(0, 5)
print(lista)