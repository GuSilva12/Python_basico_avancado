# A FUNCAO PRINT
# Imprime uma mensagem (argumento) na tela
    #Argumento: algo passado para uma funcao/metodo



#imprimindo um unico argumento
print(123)    

# IMPRIMINDO MAIS DE UM ARGUMENTO
    #Ao imprimir mais de um argumento, estes devem ser separados por virgulas
print("IMPRIMINDO MAIS DE UM ARGUMENTO\nAo imprimir mais de um argumento, estes devem ser separados por virgulas")
print(12, 34)
print(12, 34)



# DETERMINANDO UM SEPARADOR DE ARGUMENTOS NA FUNCAO PRINT (sep="" ou sep='')
    #Para determinar um separador, usa-se o parametro 'sep="<separador_escolhido>"'
print("DETERMINANDO UM SEPARADOR DE ARGUMENTOS NA FUNCAO PRINT (sep="" ou sep='')\nPara determinar um separador, usa-se o parametro sep='<separador_escolhido>'")
print(12, 34, sep='-')  # Separando os argumentos com sep='-'
print(12, 34, sep="-")  # Separando os argumentos com sep="-"


print(12, 34, sep='')   # Retirando a separacao dos argumentos com sep=''
print(12, 34, sep="")   # Retirando a separacao dos argumentos com sep=""


# DETERMINANDO O FINAL DE UM PRINT (end="" ou end='')
    #Para determinar o final de um print, usa-se o  parametro end="" ou end=''

print("DETERMINANDO O FINAL DE UM PRINT (end="" ou end='')\nPara determinar o final de um print, usa-se o  parametro end='', seja com aspas imples ou duplas")
print(12, 34, end='\r\n') 
print(56, 78, end="\n")

print(12, 34, end="##\n")
print(56, 78, end="**\n")

print(12, 34, end="\n##")
print(56, 78, end="\n**")

print(12, 34, end="\n##\n")
print(56, 78, end="\n**\n")