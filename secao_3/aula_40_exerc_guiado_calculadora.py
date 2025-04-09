# EXERCICIO GUIADO - CALCULADORA

while True:
    # CABEÇALHO
    print("CALCULADORA COM WHILE\n")
    
    # OPÇÃO DE SAIR DO PROGRAMA
    sair = input("Para sair, digite [s]. Para continuar, qualquer tecla: \n").lower().startswith("s")   # coleta uma str e retorna bool após o valor ser modificado para minúsculo e verificado se é o caracter "s"

    if sair is True:    # se opção de sair for true
        break           # interrompe o programa

    # solicitando os valores e o operador aritmético para realização do cálculo matemático
    num_1 = input("Digite um número: \n")
    op = input("Agora, digite a operação (+  -  * ou  /): \n")
    num_2 = input("Digite outro número: \n")
    
    num1_valido = num_1.isdigit()   # verificando se o valor inserido é um dígito
    num2_valido = num_2.isdigit()   # verificando se o valor inserido é um dígito


    # CONJUNTO QUE ARMAZENA OS VALORES VÁLIDOS PARA REALIZAR OPERAÇÕES
    SINAIS_VALIDOS = ["+", "-", "*", "/"]   # sinais válidos para se realizar operações matemáticas

    op_valido = op in SINAIS_VALIDOS    # se operador inserido for válido, retorna True

    if num1_valido and num2_valido and op_valido:   # se todas as condições forem atendidas, acessa o bloco
        # CASTING
        valor_1 = float(num_1)  # convertendo o valor para float
        valor_2 = float(num_2)  # convertendo o valor para float

        # VERIFICA O OPERADOR ESCOLHIDO, E COM BASE NELE, REALIZA O CÁLCULO
        if op == "+":
            soma = valor_1 + valor_2
            print(f"A soma de {num_1} com {num_2} é: {soma}\n")

        elif op == "-":
            sub = valor_1 - valor_2
            print(f"A subtração de {num_1} com {num_2} é: {sub}\n")

        elif op == "*":
            mult = valor_1 * valor_2
            print(f"A multiplicação de {num_1} com {num_2} é: {mult}\n")
        else:
            div = valor_1 / valor_2
            print(f"A divisão de {num_1} com {num_2} é: {div}\n")
    else:
        print("Argumento inválido inserido!!!\n")   # Informa ao usuário que os valores inseridos são inválidos
        continue                                    # volta para o inicio do programa