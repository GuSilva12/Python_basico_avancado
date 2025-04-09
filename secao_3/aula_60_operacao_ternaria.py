# OPERAÇÃO TERNÁRIA COM PYTHON (IF E ELSE DE UMA LINHA) 

"""
    Operação ternária (condicional de uma linha)

    <valor> if <condicao> else <outro_valor>
"""
# EXEMPLO 1
condicao_verdadeira = 10 == 10      # True
condicao_falsa = 10 == 20           # False

variavel_verdadeira = "valor " if condicao_verdadeira else "Outro valor"    # True
variavel_falsa = "Bora" if condicao_falsa else "sei lah"                    # False

print(variavel_verdadeira)          # True
print(variavel_falsa)               # False
print("-"*50)

# EXEMPLO 2
digito1 = 9
digito2 = 10

novo_digito_true = digito1 if digito1 <= 9 else 0       # True -- novo_digito_true assumirá o valor de digito1 se este for menor ou igual à 9, senão, assumirá o valor 0
novo_digito_false = digito2 if digito2 >= 20 else 15    # False -- novo_digito_false assumirá o valor de digito2 se este for maior ou igual à 20, senão, assumirá o valor 15

print(novo_digito_true)
print(novo_digito_false)