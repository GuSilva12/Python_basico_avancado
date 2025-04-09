# WHILE/ELSE

string = "Valor qualquer"

i = 0

while i < len(string):
    letra = string[i]

    print(letra)

    i += 1

else:   # após while ser executado por completo e sem interrupção forçada, será execitado o else do laço while
    print("Laço else foi executado")
print("Fora do while")