# GERAR O PRIMEIRO DIGITO DE UM CPF COM PYTHON

"""
    CÁLCULO DO PRIMEIRO DÍGITO DO CPF

    CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF, multiplicando cada um dos valores por uma contagem regressiva começando de 10

    
    Ex: 746.824.890-70 (746824890)

    10  9  8  7  6  5  4  3  2
 *  7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:

    70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10

    301*10 = 3010

Obter o resto da divisão da conta anterior por 11

    301 % 11 = 7

Se o resultado anterior for maior que 9:

    resultado é 0

Contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = "74682489070"
nove_digitos = cpf[:9]                                              # obtendo os 9 primeiros dígitos do cpf


# LOOP DE MULTIPLICAÇÃO DOS DÍGITOS DO CPF
contador_regressivo = 10                                            # contador regressivo para multiplicação dos dígitos
resultado = 0                                                       # váriável de valor inicial 0 que guardará o resultado da multiplicação

for digito in nove_digitos:   
    resultado += int(digito) * contador_regressivo                  # convertendo 'digito' de str para int e multipicando pelo contadpr regressivo
    contador_regressivo -= 1                                        # subtraindo 1 do contador regressivo, para ser usado no dígito seguinte


# multiplicando o resultado da multiplicação por 10, e, em seguida, descobrindo seu módulo
primeiro_digito = ((resultado * 10) % 11)

print(primeiro_digito)

# determinando o primeiro dígito do cpf
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0    # o primeiro dígito será o resultado do cálculo, se este for menor ou igual à 9, senão, 0

# imprimindo o resultado
print(f'O primeiro dígito do CPF é: {primeiro_digito}')

