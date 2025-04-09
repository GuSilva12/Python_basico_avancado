# INTRODUÇÃO AO EMPACOTAMENTO E DESEMPACOTAMENTO

"""
    A quantidade incorreta de variáveis ou de valores para tais resultará em:
    
            ValueError: not enough values to unpack (expected 'x' got 'y')
"""


nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
print(nome2)

# SE queremos um valor em uma variável, e os demais em outra, usamos "*_" para selecionar os demais valores

nome4, *_ = ["Mateus", "Marcos", "Lucas"]
print(nome4)

# se queremos pular algum valo da lista, usamos "_" para fazer isso. Insira-o na posição (index) em que deseja pular

_, nome5, *_ = ["Paulo", "Pedro", "Silas"]  # Vai pular "Paulo", imprimir "Pedro" e ignorar "`Lucas"
print(nome5)