# FATIAMENTO DE STRINGS E A FUNCAO LEN()

"""
 012345678
 Olá mundo
-987654321

Fatiamento [1:f:p] [::]

ONDE:
i = inicio
f = final
p = passo (de quantos em quantos caracteres vai "pular")

len() -> retorna a quantidade de caracteres da str
"""

variavel = 'Olá mundo'

print(10*"-")
print("OBTENDO CADA ITEM DA STR A PARTIR DO SEU INDEX POSITIVO E IMPRIMINDO NO TERMINAL")
print(variavel[0])
print(variavel[1])
print(variavel[2])
print(variavel[3])
print(variavel[4])
print(variavel[5])
print(variavel[6])
print(variavel[7])
print(variavel[8])
print(10*"-")
print("OBTENDO CADA ITEM DA STR A PARTIR DO SEU INDEX NEGATIVO E IMPRIMINDO NO TERMINAL")
print(variavel[-9])
print(variavel[-8])
print(variavel[-7])
print(variavel[-6])
print(variavel[-5])
print(variavel[-4])
print(variavel[-3])
print(variavel[-2])
print(variavel[-1])
print(10*"-")
print("FATIANDO A STRING")
print(variavel[4:])             # fatiando a partir do index 4, indo até o final da string (para isso, não se fornece o final)
print(variavel[:5])             # para fatiar desde o início da string, oculta-se o index de inpicio, fornecendo apenas o index de final do fatiamento
print(variavel[1:6])            # fatiando a partir do index 1, indo até o index 6, que é ocultado (para aparecer, coloque um index à mais, nesse caso, 7)
print(variavel[1:7])            # fatiando a partir do index 1, indo até o index 7, que é ocultado (para aparecer, coloque um index à mais, nesse caso, 8)
print(variavel[-8:-2])          # usando indexes negativos para realizar o fatiamento
print(variavel[0:9:1])          # fatiando a partir do index 0, indo até o index 9, pulando de um em um
print(variavel[0:9:2])          # fatiando a partir do index 0, indo até o index 9, pulando de dois em dois
print(variavel[0:9:3])          # fatiando a partir do index 0, indo até o index 9, pulando de três em três
print(variavel[-1:-10:-1])      # usando index negativo para inverter a frase
print(10*"-")
print("A FUNÇÃO LEN()")
print(len(variavel))        # usando a função len() para obter a quantidade de caracteres da variável