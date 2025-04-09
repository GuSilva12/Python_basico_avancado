# EXERCICIO - CRIE UMA LIUSTA DE COMPRAS COM LISTAS

"""
    Faça uma lista de compras com listas.
    O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
    Não permita que o programa quebre com erros de índices inexistentes em sua lista
"""

import os

# DECLARANDO AS VARIÁVEIS
lista_compras = []  # lista vazia



# INÍCIO DO PROGRAMA
while True:
    lista_enumerada = list(enumerate(lista_compras))    # enumerando a lista passada como parâmetro

    
    opcao = input("LISTA DE COMPRAS \n [i]nserir, [a]pagar ou [l]istar?: ")
    print()

    # INSERINDO DADOS NA LISTA
    if opcao == 'i':
        inserir_item = input("Digite o item a ser adicionado: ")
        lista_compras.append(inserir_item)      # adicionando o elemento digitado pelo usuário
        os.system('cls')
        continue


    # APAGANDO DADOS DA LISTA, USANDO COMO PARÂMETRO O ÍNDICE DO ELEMENTO A SER REMOVIDO
    elif opcao == 'a':
        for index, item in lista_enumerada:     # iterando sob a lista, para imprimir seus elementos
            print(index,"-", item)
           
        index_item = input("Digite a posição em que está o item a ser apagado: ")   # solicita que o usuário digite o índice em que se encontra o elemento a ser removido

        try:
            index_item_int = int(index_item)        # convertendo a str da input para int, a fim de ser usado como índice para remoção do valor que armazena n lista
            del lista_compras[index_item_int]       # removendo o item da lista com base no índice
            continue
            
        except ValueError:     # Se ocorre algum erro (exceção) dentro do bloco 'try', pula imediatamente para o exception
            os.system("cls")
            print("POR FAVOR, DIGITE NÚMEROS INTEIROS!!!\n")

        except IndexError:
            os.system("cls")
            print("ÍNDICE INEXISTENTE. DIGITE UM DOS VALORES CONFORME A LISTA EXIBIDA!!!\n")

    # ITERANDO E IMPRIMINDO OS ITENS DA LISTA
    elif opcao == 'l':      
        
        print("LISTA:")

        for index, item in lista_enumerada:
            print(index,"-", item)
            continue
    else:
        os.system('cls')
        print('Por favor, escolha "i", "a" ou "l"\n')