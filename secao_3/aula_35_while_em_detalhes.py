# WHILE - EM DETALHES  

"""
    LAÇOS DE REPETIÇÃO

    While = enquanto

    Exeuta uma ação enquanto a condição for True.
    Portanto, se um laço While possuir valor inicial False, este NÂO SERÁ EXECUTADO

    
    exemplo:
    
    while False:
        print("Vish...")
 """
while False:
        print("Vish...")

print("Uma vez que o laço While possui valor False, este não será executado, encerrando ou seguindo diretamente para a próxima parte do programa")
print("-----"*20)


"""
    Sabendo que, uma vez True, o laço continuará sendo executado, podemos usar um contador, por exemplo para que, enquanto a condição for True, execute uma ação, e pare quando for False
"""

contador = 0

while contador <= 10:    # enquanto a condição for True, executa o bloco de código
    print("A condição para execução desse laço é que o mesmo seja executado até que o contador atinja o número 10")
    print(f"O laço está sendo executado, porque a condição do laço ainda é True,. Esse laço foi executado {contador} vezes")
    print()
    contador += 1   # incrementando 1 ao contador
    
# imprime uma mensagem no terminal quando o programa sai do bloco while
print(f"Saimos do laço While, pois a condição passou de True para False quando o contador atingiu {contador}, que é maior que {contador - 1}")  