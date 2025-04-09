# EXERCÍCIOS

"""
    Faça um programa que peça ao usuário para digitar um numero inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que ele não é inteiro
"""
numero_digitado = input("Digite um número e direi se ele é par ou ímpar: ")     # solicitando que o usuário digite um número para verificar se é par ou iímpar


if numero_digitado.isdigit():                               # se o valor inserido for um dígito (número), executa o bloco

    numero_conv_int = int(numero_digitado)                  # convertendo o valor digitado de str para int
    numero_e_par = numero_conv_int % 2                      # verificando se o número digitado é par com o uso do módulo (resto de divisão)
        
    if numero_e_par == 0:                                   # se o módulo for igual a 0, executa o bloco if
        print(f"O número {numero_digitado} é par")               
    else:                                                   # se o módulo NÃO for igual a zero, executa o bloco else
        print(f"O número {numero_digitado} não é par")            
else:                                                       # se o valor inserido NÃO for um dígito (número), executa o bloco
    print("Você não digitou um número inteiro")                    


"""
    Faça um programa que pergunte a hora ao usuário e, baseado no horário descrito, exiba a saudação apropriada.1
    BOM DIA: 0-11
    BOA TARDE: 12-17
    BOA NOITE: 18-23
"""
hora_digitada = input("Digite a HORA atual: ")                                  # solicita que o usuário digite a hora atual (apenas a hora)

if hora_digitada.isdigit():                            # se o valor inserido for um dígito (número), executa o bloco

    hora_convertida = int(hora_digitada)                           # convertendo o valor digitado de str para int

    if (hora_convertida >= 0) and (hora_convertida <=11):          # se a hora estiver entre 0 e 11, executa o bloco if
        print("Bom dia")
    elif (hora_convertida >= 12) and (hora_convertida <= 17):       # se a hora estiver entre 12 e 17, executa o bloco elif
        print("Boa tarde")
    elif (hora_convertida >= 18) and (hora_convertida <= 23):                                                          # se a hora for igual ou maior que 18, executa o segundo bloco elif
        print("boa noite")
    else:
        print("Não conheço essa hora")

else:                                                   # se o valor inserido NÃO for um dígito (número), executa o bloco
    print("O valor inserido não é composto exclusivamente por dígitos (números)")


"""
    Faça um programa que peça o primeiro nome do usuário Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
    maior que 6 escreva "Seu nome é muito grande"
"""
nome_digitado = input("Digite seu nome: ")                                      # solicita que o usuário insira seu nome
tamanho_nome = len(nome_digitado)                                               # verificando e armazenando o tamanho do nome digitado

if tamanho_nome >= 1:
    if tamanho_nome <= 4:                                                   # se o tamanho do nome for menor ou igual a 4, executa o bloco if
        print(f"Seu nome possui {tamanho_nome} letras...é muito curto")
    elif (tamanho_nome > 4) and (tamanho_nome <= 6):                        # se o tamanho do nome for maior que 4 e menor ou igual a 6, executa o bloco elif
        print(f"Seu nome possui {tamanho_nome} letras...é normal")                  
    else:                                                                   # se o tamanho do nome for maior que 6, executa o bloco else
        print(f"Seu nome possui {tamanho_nome} letras...é muito grande")            
else:
    print("Digite mais de uma letra")

