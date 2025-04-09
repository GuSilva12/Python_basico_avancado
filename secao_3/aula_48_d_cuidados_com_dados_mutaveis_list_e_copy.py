# CUIDADOS COM TIPOS DE DADOS MUTÁVEIS - LIST E COPY

"""
     = - copiando o valor (imutáveis)
     = - aponta para o mesmo valor na memória (mutável)
"""

# copiando o valor da variável (imutável)
nome = "Luiz"
noutra_variavel = nome
nome = "João"
print(nome)
print(noutra_variavel)


# apontando para o mesmo valor na memória
lista_a = ["Luiz", "Maria"]
lista_b = lista_a   # lista_b aponta para outra variável (lista_a), que armazena a lista acima
print(lista_a)

lista_b[0] = "Qualquer coisa"   # como 'lista_b' aponta para 'lista_a', a alteração ocorrerá em 'lista_a'
print(lista_b)
print()

# COPY - copiando os valores de uma variável para manipular seu conteúdo sem afetar se estado inicial. Isso pode ser feito em listas
lista_c = ["Mapex", "Alesis", "Pearl", "Roland"]
print(lista_c)
# copiando lista_c para manipular seu conteúdo sem alterar a lista principal
lista_d = lista_c.copy()
# alterando um dos valores da lista copiada
lista_d[0] = "Sabian"
print(lista_d)