# LISTAS DENTRO DE LISTAS (ITERÁVEIS DENTRO DE ITERÁVEIS)

"""
    lista de listas e seus índices

    COMO ACESSAR O VALOR DE UM ITERÁVEL DENTRO DE OUTRO ITERÁVEL?
        - coloque o nome da lista principal, seguido pelo índice da lista a ser acessada da lista principal, seguido do índice da posicçao do elemento nessa lista acessada da lista principal
"""

salas = [
    #   0         1
    ["Maria", "Helena", ],          # 0
    #   0
    ["Elaine", ],                   # 1
    #   0      1         2
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],  # 2
]


print('_'*20)
print("Acessando listas dentro de listas")

print(salas)            # imprime uma lista de listas -> [['Maria', 'Helena'], ['Elaine'], ['Luiz', 'João', 'Eduarda']]
print()
print(salas[1])         # imprime a lista 1 da lista principal -> ['Elaine']
print()
print(salas[1][0])      # imprime o item 0 da lista 1 da lista principal -> Elaine
print()
print(salas[2][2])      # imprime o item 2 da lista 2 da lista principal -> Eduarda
print()
print(salas[2][3])      # imprime o item 3 da lista 2 da lista principal -> (0, 10, 20, 30, 40)
print()
print(salas[2][3][2])   # imprime o item 2 da tupla, que está no índice 3 da lista 2, pertencente à lista principal
print()
print('_'*20)


# É POSSÍVEL ITERAR AS LISTAS INTERNAS COM LOOP FOR
print("Iterando listas")
for sala in salas:
    print(sala)

print()
print('_'*20)
print("Iterando listas dentro de listas")

for sala_aula in salas:
    print(f'A sala de aula é: {sala_aula}')

    for aluno in sala_aula:
        print(aluno)

print('_'*20)