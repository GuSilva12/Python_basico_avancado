"""
EXERCÍCIO

Peça ao usuário para digitar deu nome
Peça ao usuário para digitar sua idade

Se nome e idade forem digitados:

    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Seu noome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
    Se nada for digitado nem nome ou idade:
        Exiba: "Desculpe, você deixou campos vazios"
"""

nome = input("Digite seu nome: ")               # solicitando que o usuário forneca um nome para armazenar na variavel 'nome'
idade = input("Digite sua idade: ")             # solicitando que o usuário forneca uma idade para armazenar na variavel 'idade'

if (not nome) or (not idade):                   # se campos 'nome' ou 'idade' não foram preenchidos é exibida uma notificação no termina
    # imprimindo a notificação de pendência de dados nos campos solicitados
    print("Desculpe, você deixou campos vazios")
else:
    # imprimindo o nome ornecido pelo usuário no terminal
    print(f'Seu nome é {nome}')
    
    # invertendo o nome fornecido, iniciando do primeiro index negativo, percorrendo toda a string de trás para frente (-1), e imprimindo no terminal
    print(f'Seu nome invertido é {nome[-1::-1]}')
    
    # verificando se o nome fornecido possui espaços
    if ' ' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
        
    # imprimindo a quantidade de letras que o nome fornecido possui
    print(f'Seu nome tem {len(nome)} letras')

    # imprimindo a primeira letra do nome fornecido pelo usuário
    print(f"A primeira letra do seu nome é {nome[0]}")
    
    # imprimindo a última letra do nome fornecido pelo usuário
    print(f'A última letra do seu nome é {nome[-1]}')