# INTERPOLACAO DE STRING COM % EM PYTHON

'''
Interpolação básica de strings

s - string
d/i = int
x/X - hexadecimal(ABCDEF0123456789)
'''

nome = 'Luiz'
preco = 100.95897643
variavel = '%s, o preco é R$%.2f' %(nome, preco)
print(variavel)
print("O hexadecimel de %d é %x" %(150, 150))