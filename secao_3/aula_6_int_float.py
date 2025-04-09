# TIPOS INT E FLOAT

# int -> numero inteiro
# Representa qualquer numero inteiro positivo ou negativo (quando sem sinal, é considerado positivo)
print("'int' representa qualquer numero inteiro positivo ou negativo")
print(11)   # imprimindo um valor int
print(0)    # imprimindo um valor int
print(-11)  # imprimindo um valor int
print(1, 2, 3, 4, 5)# imprimindo dievrsos valores float (para isso, separa-se esses valores por virgula)
print(1, 2, 3, 4, 5, sep=',') # imprimindo diversos float, separados por virgulas visiveis, declaradas atraves da funcao "sep=''""
print()

# float -> numero de ponto flutuante (separado por ponto final '.')
# Representa qualquer numero positivo ou negativo de ponto flutuante (quando sem sinal, considerado positivo)
print("'float' representa qualquer numero de ponto flutuante positivo ou negativo")
print(1.1)  # imprimindo um valor float
print(0.0)  # imprimindo um valor float
print(-1.1) # imprimindo um valor float
print(-3.3, -2.2, -1.1, 0.0, 1.1, 2.2, 3.3) # imprimindo dievrsos valores float (para isso, separa-se esses valores por virgula)
print(-3.3, -2.2, -1.1, 0.0, 1.1, 2.2, 3.3, sep=',') # imprimindo diversos float, separados por virgulas visiveis, declaradas atraves da funcao "sep=''""
print()

# DESCOBRINDO O TIPO INFERIDO A UM VALOR 
# Para se saber o tipo inferido a um valor pelo Python, usa-se a função 'type()'
print("Usamos 'type()' para descobrir o tipo inferido a um valor pelo Python")
print()

print(type(11))     #imprimindo o tipo do argumento passado (int)
print(type(-11))    #imprimindo o tipo do argumento passado (int)

print()

print(type(1.1))    #imprimindo o tipo do argumento passado (float)
print(type(-1.1))   #imprimindo o tipo do argumento passado (float)

print()

print(type('Oficina G3'))   #imprimindo o tipo do argumento passado (str)
print(type("Oficina G3"))   #imprimindo o tipo do argumento passado (str)

print()

print(type(True))   #imprimindo o tipo do argumento passado (bool)
print(type(False))  #imprimindo o tipo do argumento passado (bool)

