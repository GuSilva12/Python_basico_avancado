# TIPOSBULT-IN, DOCUMENTAÇÃO, TIPOS IMUTÁVEIS, MÉTODOS DE STRING

"""
    https://docs.python.org/pt-br/3/library/stdtypes.html

    Tipos imutáveis mais comuns: str, int, float, bool
"""

string = "Luiz Otávio"

print(string[3])       # retorna o elemento que ocupa o index 3 da str 'string'

"""
    IMUTÁVEL = não se pode mudar o valor

    EX: não se pode alterar qualquer elemento da variável 'string' acima exibido.

    string[3] = 'ABC'
    print(string[3])


    NESSE CASO, O QUE PODEMOS FAZER É ATRIBUIR O VALOR DE 'string' EM OUTRA VARIÁVEL 'outra_variavel' EXECUTAR NELA A ALTERAÇÃO DA STRING
"""
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)


"""
    OBJETOS: elementos (dados/variáveis) capazes de realizar uma ação (método)
"""
print(string.capitalize())      # retorna uma cópia da string com o seu primeiro caractere em maiúsculo e o restante em minúsculo
print(f"Usando o método 'capitalize()', que imprime a str com o primeiro caractere em maiúsculo: {string.capitalize()}")

print(string.isdigit())         # retorna True se todos os caracteres na string são dígitos e existe pelo menos um caractere, e False caso contrário
print(f"Usando o método 'isdigit()', que retorna True se todos os caracteres na string são dígitos e existe pelo menos um caractere, e False caso contrário: {string.isdigit()}")

print(string.isupper())         # retorna True se todos os caracteres que permitem maiúsculas ou minúsculas na string estão com letras maiúsculas, e existe pelo menos um caractere 
print(f"Usando o método 'isupper()' que retorna True se todos os caracteres que permitem maiúsculas ou minúsculas na string estão com letras maiúsculas, e existe pelo menos um caractere: {string.isupper()}")

print(string.isascii())         # retorna True se a string é vazia ou se todos os caracteres na string são ASCII, e False caso contrário
print(f"Usando o método 'isascii()' que retorna True se a string é vazia ou se todos os caracteres na string são ASCII, e False caso contrário: {string.isascii()}")