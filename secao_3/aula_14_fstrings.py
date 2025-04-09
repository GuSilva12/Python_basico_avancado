# f-strings (formatação de strings)

# Para evitar 'quebrar' uma string varias vezes para inserir valores de variaveis, declara-se a variável entre chaves {} ao longo das strings, 
# onde deve aparecer seu respectivo valor

# USANDO COMO EXEMPLO A STRING RETORNADA NO EXERCIO DO IMC
# declaracao de variaveis
nome = 'Luiz Otávio'                # string
altura = 1.80                       # float
peso = 95                           # int
imc = peso/(altura**2)              # armazena o resultado do quadrado da altura dividido pelo pesso da pessoa

# imprimindo os dados e o retorno do calculo
print('INDICE DE MASSA MUSCULAR')
print("Nome: ", nome, "\nAltura: ", altura, "\nPeso: ", peso, "\n")
print(nome, " tem ", altura ," de altura, pesa ", peso, " quilos e seu IMC é ", imc)


# Usando f-strings para formarar a string
linha_1 = f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}'
print(linha_1)