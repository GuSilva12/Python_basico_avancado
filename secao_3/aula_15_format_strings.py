# FORMATACAO DE STRINGS COM MÈTODO format

a = "A"
b = 'B'
c = 1.1

# a str esta armazennada em uma variavel, com placeholders '{}' que preencherao a str com o valor referente a variavel que antecede
string = 'a={nome1} b={nome2} c={nome3:.2f}'           

string2 = 'a={nome2} b={nome1} c={nome3:.2f}'          

string3 = 'a={nome3:.2f} b={nome2} c={nome1}'           


# variavel que recebe o valor da variavel 'formato' e usa o metodo .format() para atribuir as variaveis a serem usadas pelos placeholders
formato = string.format(nome1 =a, nome2 = b, nome3 = c)     

formato2 = string2.format(nome1 =a, nome2 = b, nome3 = c)        

formato3 = string3.format(nome1 =a, nome2 = b, nome3 = c)        


print(formato)
print(formato2)
print(formato3)
