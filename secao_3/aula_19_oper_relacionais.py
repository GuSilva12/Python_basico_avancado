# OPERADORES RELACIONAIS (DE COMPARACAO) EM PYTHON

'''
OPERADORES DE COMPARACAO (RELACIONAIS)

OP      SIGNIFICADO        EXEMPLO (SAIDA = TRUE)
>           maior                   2 > 1
<           menor                   2 < 1
>=     maior ou igual               2 >= 1
<=     menor ou igual               2 <= 1
==          igual                 'a' == 'a'
!=        diferente               'a' != 'a'

-> Retornam um booleano (True/False)
'''

maior = 2 > 1                    # Se valor maior, retorna True
maior_ou_igual = 2 >= 1          # Se valor maior ou igual, retorna True
menor = 1 < 2                    # Se valor menor, retorn True
menor_ou_igual = 2 <= 2          # Se valor menor ou igual, retorna True
igual = 'a' == "a"               # Se valor igual, retorna True
diferente = 'a' != "a"           # Se valor diferentem retorns True


print("Valor é maior: ", maior)                            
print("Valor é maior ou igual: ", maior_ou_igual)           
print('Valor é menor: ', menor)                             
print('Valor é menor ou igual: ', menor_ou_igual)           
print("Valor é igual: ", igual)                             
print('Valor è diferente: ', diferente)                     