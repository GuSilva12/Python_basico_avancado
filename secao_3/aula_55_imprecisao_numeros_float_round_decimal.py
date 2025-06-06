# IMPRECIOSÃO DOS NÚMEROS DE PONTO FLUTUANTE + ROUND E decimal.Decimal

"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

# IMPORTANDO O MÓDULO 'DECIMAL'
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)                 # 0.7999999999999999
print(f"{numero_3:.2f}")        # 0.80

# ARRENDONDANDO UM NÚMERO COM ROUND
print(round(numero_3, 3))       # 0.8 - formatação que o round gera


# USANDO O MÓDULO 'DECIMAL'
numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5
print(numero_6)                 # 0.7999999999999999611421941381