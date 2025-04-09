# WHILE E BREAK - ESTRUTURAS DE REPETIÇÃO

"""
    WHILE - executa uma operação enquanto a condição foir verdadeira (True)


    while <condição for True>:
        <comando do laço while>

    OBS: se atentar para não cair em LOOP (execução 'infinita' de código)        
"""

condicao = True                             # valor True armazenado dentro da variável 'condicao'

while condicao:                             # enquanto a condição 'condicao' for True, executa o comando dentro do laço
    nome = input('Qual o seu nome: ')                               # solicita uma entrada de dados pelo usuário
    print(f'Seu nome é {nome}')                                     # imprime uma mensagem com o nome fornecido na input 'nome'
    break
print('Saiu do bloco do exemplo 1')

# EXEMPLIFICANDO, AGORA, ADICIONANDO UMA CONDICIONAL QUE VERIFICA SE O USUÁRIO DIGITOU 'sair' PARA SAIR DO PROGRAMA
condicao2 = True

while condicao2:
    print("Para sair desta parte do programa, digite 'sair'")       # imprime uma mensagem na tela
    nome = input('Qual o seu nome: ')                               # solicita uma entrada de dados pelo usuário

    # verificando se o usuário digitou 'sair', para encerrar o programa
    if nome == 'sair':                                              # se na input for digitado 'sair'
        condicao2 = False                                           # valor de 'condicao2' passara a ser False, encerrando o programa
        print("Você saiu do programa")                              # imprime uma mensagem no terminal

print('Saiu do bloco do exemplo 2')