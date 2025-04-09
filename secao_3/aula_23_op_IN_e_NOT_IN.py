# OPERADORES IN E NOT IN

# Strings sao iteraveis (pode-se navegar item por item)
#  0 1 2 3 4 5  
#  O t á v i o
# -6-5-4-3-2-1  

nome = 'Otávio'

print(nome[0])      # O
print(nome[1])      # t
print(nome[2])      # á
print(nome[3])      # v
print(nome[4])      # i
print(nome[5])      # o
#----------------------
print(10 * "-")
print(nome[-6])      # O
print(nome[-5])      # t
print(nome[-4])      # á
print(nome[-3])      # v
print(nome[-2])      # i
print(nome[-1])      # o
#----------------------
# Operador in
print(10 * "-")
print('O' in nome)      # True
print('t' in nome)      # True
print('á' in nome)      # True  
print('v' in nome)      # True  
print('i' in nome)      # True  
print('o' in nome)      # True  

#----------------------
# Operador not in
print(10 * "-")
print('O' not in nome)      # False
print('t' not in nome)      # False
print('á' not in nome)      # False
print('v' not in nome)      # False
print('i' not in nome)      # False
print('o' not in nome)      # False
#----------------------
print(10 * "-")

nome_digitado = input("Digite um nome: ")
busca = input("Digite o que deseja encontrar no nome digitado: ")

if busca in nome_digitado:
    print(f'{busca} está em {nome_digitado}')
else:
    print(f'{busca} não está em {nome_digitado}...')