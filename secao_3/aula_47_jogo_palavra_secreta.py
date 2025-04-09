# JOGO DA PALAVRA SECRETA

"""
    Faça um jogo para o usuário adivinhar qual é a palavra secreta.
    - Proponha uma palavra secreta qualquer, e dê a possibilidade para o usuário digitar apenas uma letra
    - Quando o usuário digitar uma letra, confira se esta consta na palavra secreta
        - se a letra digitada estiver na palavra secreta, exiba a letra
        - Se a letra não estiver na palavra secreta, exiba *
    - Faça a contagem de tentativas do seu usuário
"""

# PALAVRA SECRETA
palavra_secreta = "musicalidade"
letras_acertadas = ""

while True:
    # CONTADOR DE TENTATIVAS
    cont_tentativas = 0
    # CABEÇALHO
    print("JOGO DA PALAVRA SECRETA")
    # LETRA DIGITADA
    letra_digitada = input("Digite uma letra: ")
    # VERIFICANDO SE FOI DIGITATA UMA ÚNICA LETRA NA INPUT
    uma_letra = len(letra_digitada) == 1    # Retorna True se for digitado uma única letra

    # Se digitada uma única letra, acessa o blocos
    if uma_letra:
        if letra_digitada in palavra_secreta:   # Se a letra digitada consta na palavra secreta, concatena em uma variável e exibe
            letras_acertadas += letra_digitada
            print(f"Palavra formada: ")
        
        # EXIBINDO A LETRA VALIDADA, DE FORMA A OCULTAR AS DEMAIS AINDA NÃO DESCOBERTAS
        palavra_formada = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += "*"

        print("Palavra formada: ", palavra_formada)

        if palavra_formada == palavra_secreta:
            print("VOCÊ GANHOU! PARABÉNS!")
            print(f"A palavra era {palavra_formada}")

    else:
        print("Digite UMA letra!!!")
        continue
    
    cont_tentativas += 1