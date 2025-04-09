# POSPIVIS PROBLEMAS E SOLUÇÕES PARA O ALGORITMO DO CPF


"""
    Podemos usar 'replace()' para remover as pontuações do CPF (passar de XXX.XXX.XXX-XX para XXXXXXXXXXX), ou, inclusive, usar a biblioteca 're' (regular expressions), que consiste em sequencias 
    de caracteres que permitem encontrar e substituir oadrões em strings ou arquivos.
"""

# IMPORTANDO A BIBLIOTECA RE
import re


# cáculo do segundo sígito do CPF
# EXEMPLIFICANDO COM FUNÇÃO REPLACE()
#cpf_enviado_usuario = '74682489070'.replace('.', '').replace('-', '').replace(' ', '')

# EXEMPLIFICANDO COM BIBLIOTECA RE
entrada = input("Digite seu CPF (ex: 746.824.890-70):")
cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)

nove_digitos = cpf_enviado_usuario[:9]      # obtendo os 9 primeiros dígitos do CPF
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(f'valor do primeiro dígito: {digito_1}')

# cáculo do segundo sígito do CPF
dez_digitos = nove_digitos + str(digito_1)  # concatenando os 9 dígitos do CPF com o primeiro digito
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

    
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')