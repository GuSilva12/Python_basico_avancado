# FLAGS, IS, IS NOT E NONE

"""
    FLAG (bandeira) - MARCAR UM LOCAL
    None = não-valor
    is e is not = é ou não é (tipo, valor, identidade)
    id = identidade
"""



condicao = True
passou_no_if = None         # setando uma variável para ser usada como flag

if condicao:
    passou_no_if = True     # Marcando a passagem (flag) pelo bloco de código if
    print("Faça algo")
else:
    print("Não faça algo")


print(f"Passou no if: {passou_no_if is None}")
print(f"Passou no if: {passou_no_if is not None}")
