# CRIANDO UM GERADOR DE CPF

import random

quant_sorteios = int(input("Quantos CPFs deseja gerar?: "))     # digita-se a qunatidade de CPFs que se desja gerar

for contador in range(quant_sorteios):
    nove_digitos = ''    # definindo uma variável vazia para armazenar o CPF

    for i in range(9):                                  # para cada item em um intervalo de 0 à 9 (lembrando que o loop for não conta o último número do range - no caso, 9)
        nove_digitos += str(random.randint(0, 9))       # sorteia-se (biblioteca 'random') um número aleatório inteiro (randint), no intervalo entre 0 e 9, que são concatenados em uma variável

    print(nove_digitos)                                 # imprime o resultado na tela