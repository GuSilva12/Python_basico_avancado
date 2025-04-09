# EXPLORANDO O LOOP FOR (NEXT, ITER, ITERÁVEL E ITERADOR)

"""
    ITERÁVEL - str, range, etc (__iter__)
    ITERADOR - quem sabe entregar um valor por vez
    NEXT - me entregue o proximo valor
    ITER - me entregue seu iterador
"""

texto = "Luiz"  # iterável
iterador = iter(texto)  #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)                # imprime a letra no terminal
    except StopIteration:           # catptura o erro StopIteration, originado da falta de elementos para iterar
        break                       # se não houver mais valores para iterar, o erro StopIteration é capturado e tratado com o encerramento da operação