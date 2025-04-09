# O O QUE APRENDEMOS COM WHILE TAMBÉM FUNCIONA NO FOR (continue, break, else etc)

for i in range (10):
    if i == 2:
        print("i é 2, pulando...")
        continue    # voltando ao começo do laço

#      # finaliza o laço e pula para a saída
#
#    for j in range(1, 3):
#        print(i, j)

else:       # else não será executado se 'i' não chegar à 10 (execução completa), que é o fim do range 'i'
    print("For completo com sucesso!")