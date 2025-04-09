# LISTAS EM PYTHON

'''
    Tipo list -> mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis: índices e fatiamento
    Métodos úteis: append, insert, pop, del, clear, extend, +

    para criar uma lista vazia, usamos colchetes. Ex: lista = []

    sobre boolean: se lista vazia, retorna False. Se há elementos, retorna True


    A lista é um objeto, portanto, é capaz de realizar ações (métodos)
'''

#        +01234
#        -54321
string = "ABCDE"    # 5 caracteres
print(f"quantidades de caracteres da avriável 'string': {len(string)}")

lista = []                  # criando uma lista vazia
print(lista, type(lista))   # imprimindo uma lista vazia, seguida do seu tipo de estrutura de dado

# FAZENDO UMA VERIFICAÇÃO LÓGICA COM A LISTA. SE VAZIA, RETORNA FALSE. SE POPULADA, RETORNA TRUE
print(bool([]))             # Falsy
print()

# CRIANDO OUTRA LISTA, DESSA VEZ COM ELEMENTOS
#           0     1         2         3    4
lista_2 = [123, True, 'Luiz Otávio', 1.2, []]
print(lista_2)          # imprimindo os elementos da lista_2
print(bool(lista_2))    # True - lista possui elementos
print()

# ACESSANDO ELEMENTOS DA LISTA PELO ÍNDICE (ASSIM COMO FAZEMOS COM CARACTERES DE UMA STRING)
print(lista_2[0])
print(lista_2[1])
print(lista_2[2])
print(lista_2[3])
print(lista_2[4])