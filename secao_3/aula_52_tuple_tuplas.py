# TIPO TUPLE (Tuplas)

"""
    Tuple = Lista imutável

    Diferentemente da lista, a tupla é imutável, portanto, não pode ter seu valor alterado
"""

nomes = ("Maria", "Helena", "Luiz")

# nomes[1] = "outro"    ----------> TypeError: 'tuple' object does not support item assignment

print(nomes)

# CONVERTENDO UMA TUPLA EM LISTA E UMA LISTA EM TUPLA
nomes_lista = list(nomes)
print(f"Conevrtida em lista: {nomes}")
nomes_tuple = tuple(nomes_lista)
print(f"Convertida em tupla: {nomes_tuple}")