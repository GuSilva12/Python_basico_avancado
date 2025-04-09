# ALTERANDO UMA LISTA COM INDICES, DEL, APPEND E POP (Tipo list)

'''
   Tipo list - Mutável
   Suporta vários valores de qualquer tipo
   Conhecimentos reutilizáveis - índices e fatiamento

   Métodos úteis:
    append, insertm pop, del, clear, extend, +

    CRUD - Create, Read, Update and Delete
           Criar, Ler, Apagar, Atualizar e Deletar 
'''

#         0   1   2   3
lista = [10, 20, 30, 40]
print(lista[2]) # 30
print()

# PODEMOS ARMAZENAR O VALOR DE UM ELEMENTO DA LISTA EM UMA VARIAVEL
numero = lista[2]
print(numero)
print()

# SUBSTITUINDO O ELEMENTO DO INDICE 2 POR OUTRO VALOR
lista[2] = 300
print(lista)
print()

# DELETANDO UM ELEMENTO DA LISTA
del lista[2]
print(lista)
print()


# ADICIONANDO ELEMENTOS À LISTA (append) - por padrão, a adição é feita no final da lista
lista.append(50)
print(lista)
lista.append(60)
print(lista)
lista.append(70)
print(lista)

# REMOVENDO ELEMENTOS DE UMA LISTA (pop) - por padrão, remove  último elemento da lista
lista.pop()
print(lista)
lista.pop()
print(lista)

# Podemos armazenar o último valor removido para exibí-lo após sua remoção
ultimo_valor = lista.pop()
print(f"{lista} removido: {ultimo_valor}")
