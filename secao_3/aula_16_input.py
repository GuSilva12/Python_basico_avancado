# INPUT PARA COLETA DE DADOS DO USUARIO

# A funcao 'input()' sempre reetorna uma string

nome = input('Qual o seu nome: ')

print(nome)
print(f'Seu nome é {nome}')         # imprimindo uma mensagem usando f-strings para adicionar e formatr o valor da var 'nome' a mensagem que sera impressa
print("Seu nome é", nome)           # imprimindo uma mensagem usando uma str 'padrao', seguida da var que armazena o valor a ser exibido apos a str do print

# EXEMPLOS -------------------------------------------------------------------------------------

# Solicitando dois numeros para soma

numero_1 = input("Digite um número: ")                          # Recebe uma entrada do usuario
numero_2 = input("Digite outro número: ")                       # Recebe uma entrada do usuario

soma = numero_1 + numero_2                                      # Uma vez que nao foi feito o casting, oas valores, por padrao ,sao str, portando, nao serao somados, mas concatenados

print(f'A concatenação de {numero_1} com {numero_2} é :{soma}\n')      


# solicitando dois numeros para soma e convertendo as inputs de str para int

numero_3 = input("Digite um número: ")                          # Recebe uma entrada do usuario
numero_4 = input("Digite outro numero: ")                       # Recebe uma entrada do usuario

# casting
numero_3_convertido = int(numero_3)                             # Recebe a str da var 'numero_3', convertida para int e armazenada em uma nova variavel com outro nome
nuemro_4_convertido = int(numero_4)                             # Recebe a str da var 'numero_3', convertida para int e armazenada em uma nova variavel com outro nome

soma_convertida = numero_3_convertido + nuemro_4_convertido     # feito o casting para conversao dos valores de str para int, sera impressa a soma dos vlores fornecidos

print(f"Após a conversão de str para int, o valor da soma de {numero_3_convertido} com {nuemro_4_convertido} é:{soma_convertida}\n")