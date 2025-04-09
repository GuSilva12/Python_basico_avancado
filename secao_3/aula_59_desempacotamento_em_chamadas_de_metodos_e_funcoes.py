# DESEMPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕES 

string = 'ABCD'
lista = ["Maria", "Helena", "Eduarda"]
tupla = 'Python', 'é', 'legal'

a, b, c = lista
print(a, c)


# PODEMOS DESEMPACOTAR UM ITERÁVEL, COMO UMA LISTA OU TUPLA, NA PRÓPRIA CHAMADA PRINT()

print(*lista)                                       # imprimindo todos os elementos de 'lista'
print('-'*50)
print(*lista, sep=', ')                             # imprimindo todos os elementos de 'lista', separados por virgula e espaço
print('-'*50)
print(*lista, sep=' - ')                            # imprimindo todos os elementos de 'lista', separados por hífen e espaço
print('-'*50)
print(*lista, sep= '\n')                            # imprimindo todos os elementos de 'lista', separados por quebra de linha
print('-'*50)
print(*lista, sep='\n', end='\n----------')         # imprimindo todos os elementos de 'lista', separados por quebra de linha, e finalizando cada um com 3 hífens
print('-'*50)
print(*lista, sep='\n', end='\n-')                  # imprimindo todos os elementos de 'lista', separados por quebra de linha, e finalizando cada um com 3 hífens
print('-'*50)