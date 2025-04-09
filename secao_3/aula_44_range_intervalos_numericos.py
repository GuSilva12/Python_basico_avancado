texto = "Python"

for i in range(0, len(texto)):  # dado o intervalo entre 0 e o tamanho da str 'texto', use 'i' como contador para realizar uma ação determinada quantidade de vezes
    print(texto[i])

#for i in range(0, 1000):
#    print(f"Lá ele {i + 1} vezes")

for i in range(0, 25):
    print(i)

for i in range(0, 101):
    if i % 2 == 0:
        print(f"{i} é par")

# ADICIONANDO UM PASSO ("pulos")

for i in range(0, 100, 2):  # contando de 0 a 100, de 2 em 2
    print(i)