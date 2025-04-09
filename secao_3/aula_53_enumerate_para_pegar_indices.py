# ENUMERATE PARA ENUMERAR VALORES DE ITERÁVEIS (PEGAR ÍNDICES)

'''
    enumerate - enumera iteráveis (índices)
'''

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")
print(f"Imprimindo a variável 'lista': {lista}")
print()

lista_enumerada = list(enumerate(lista))
print(f"Imprimindo a variável 'lista_enumerada': {lista_enumerada}")                  # retorna o 'iterator'
print()

# ITERANDO A LISTA, DESEMPACOTANDO  ÍNDICE E O VALOR ARMAZENADO NELE
for a, b in lista_enumerada:    # a = índice, b = valor
    print(a, b)
    print()